from django.shortcuts import render, redirect
from datetime import timedelta, timezone, datetime
from .models import Ciclo, Materia, Sessao
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'app_pomodoro/home_integrado.html')

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
