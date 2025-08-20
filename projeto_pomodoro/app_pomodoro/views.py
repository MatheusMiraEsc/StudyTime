from django.shortcuts import get_object_or_404, render, redirect
from datetime import timedelta, timezone, datetime
from .models import Ciclo, Materia, Sessao
from django.http import HttpResponse
from .forms import Registroform
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'app_pomodoro/home_integrado.html')

def menu(request):
    return render(request, 'app_pomodoro/menu.html')

# id_sessao = models.IntegerField()
#     id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)
#     data_hora_inicio = models.TimeField()
#     data_hora_fim = models.TimeField()
#     ciclos_completos = models.IntegerField()

def iniciar_sessao(request): # ativar função ao iniciar sessao e terminar sessao
    if request.method == 'POST':
        sessoes_teste = request.POST.get("sessoes")
        ciclos_teste = request.POST.get("ciclos")
        id_sessao_teste = request.POST.get("id_sessao")
        id_ciclo_teste = request.POST.get("id_ciclo")

        qntd_sessoes = int(sessoes_teste) if sessoes_teste else 0
        qntd_ciclos = int(ciclos_teste) if ciclos_teste else 0
        ID_sessao = int(id_sessao_teste) if id_sessao_teste else None
        ID_ciclo = int(id_ciclo_teste) if id_ciclo_teste else None
        
    sessao = Sessao.objects.filter(id=ID_sessao) #Encontrar forma de alterar id no front?
    ciclo= Ciclo.objects.filter(id=ID_ciclo) #Encontrar forma de alterar id no front?
    # Enquanto estuda
    if not ciclo and not sessao: # se não existe #não precisa atualizar se já existe pq atualização é feita no final e se for pausar não muda
        inicio = datetime.now() #recorda hora atual
        qntd_sessoes = 0
        sessao = Sessao.objects.create(
            id_ciclo = ID_ciclo,
            data_hora_inicio = inicio,
        )
        ciclo = Ciclo.objects.create(
            qntd_sessoes = qntd_sessoes,
        )
    return render(request, "app_pomodoro/home_integrado.html", {"sessoes": qntd_sessoes, "ciclos":  qntd_ciclos})

def finalizar_sessao(request):
    if request.method == 'POST':
        qntd_sessoes = int(request.POST.get("sessoes", 0)) 
        qntd_ciclos = int(request.POST.get("ciclos", 0)) 
        ID_sessao = int(request.POST.get("id_sessao", ""))
        ID_ciclo = request.POST.get("id_ciclo","")
    sessao = Sessao.objects.filter(id=ID_sessao) #Encontrar forma de alterar id no front?
    ciclo= Ciclo.objects.filter(id=ID_ciclo) #Encontrar forma de alterar id no front?
    if ciclo and sessao: #se ja existe
        fim = datetime.now() #recorda fim da sessao
        if(qntd_sessoes == 4): # 1 ciclo = 4 sessoes ou seja final do ciclo
            qntd_ciclos +=1
            sessao = Sessao.objects.update(
            data_hora_fim = fim,
        )
        ciclo = Ciclo.objects.update(
            qntd_sessoes = qntd_sessoes
        )
        return render(request, "app_pomodoro/home_integrado.html", {"sessoes": qntd_sessoes, "ciclos":  qntd_ciclos})

    qntd_sessoes+=1
    sessao = Sessao.objects.update(
        data_hora_fim = fim,
    )
    ciclo = Ciclo.objects.create(
        qntd_sessoes = qntd_sessoes
    )
    return render(request, "app_pomodoro/home_integrado.html", {"sessoes": qntd_sessoes, "ciclos":  qntd_ciclos})

def registrar(request):
    if request.method == 'POST':
        form = Registroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_integrado')
    else:
        form = Registroform()
    return render(request, 'app_pomodoro/registrar.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_integrado')
        else:
            return render(request, 'app_pomodoro/logar.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'app_pomodoro/logar.html')

# -----------------------------
# CRUD DE MATERIA
# -----------------------------

def listar_materias(request):
    materias = Materia.objects.all()
    return render(request, "app_pomodoro/materias_listar.html", {"materias": materias})

def criar_materia(request):
    if request.method == "POST":
        nome = request.POST.get("nome_materia")
        assuntos = request.POST.get("assuntos")
        Materia.objects.create(nome_materia=nome, assuntos=assuntos)
        return redirect("listar_materias")
    return render(request, "app_pomodoro/materias_form.html")

def editar_materia(request, id):
    materia = get_object_or_404(Materia, id=id)
    if request.method == "POST":
        materia.nome_materia = request.POST.get("nome_materia")
        materia.assuntos = request.POST.get("assuntos")
        materia.save()
        return redirect("listar_materias")
    return render(request, "app_pomodoro/materias_form.html", {"materia": materia})

def excluir_materia(request, id):
    materia = get_object_or_404(Materia, id=id)
    if request.method == "POST":
        materia.delete()
        return redirect("listar_materias")
    return render(request, "app_pomodoro/materias_confirmar_exclusao.html", {"materia": materia})
