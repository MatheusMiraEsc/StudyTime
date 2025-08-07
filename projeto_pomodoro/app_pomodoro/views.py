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

def iniciar_sessao(request):
    if request.method == 'POST':
        nome_M = request.POST.get("materia", "")#.strip()
        ciclos = int(request.POST.get("ciclos", 0))

        # materia = None
        # if nome_M:
        #     materia = Materia.objects.filter(nome_materia__iexact=nome_M).first()# ajustar para não precisar de nome e para selecionar a materia certa caso aja mais de um ou não exista
        
        hora_inicio = datetime.now()
        hora_fim = hora_inicio + timedelta(minutes=25)
        sessao = Sessao.objects.create(
            #id_materia = nome_M, em branco pois Funcionalidade de materia ainda não foi iniciada
            data_hora_inicio = hora_inicio,
            data_hora_fim = hora_fim,
            ciclos_completos = ciclos,
        )
        return redirect("iniciar_sessao")
    sessoes = Sessao.objects.all()#.order_by("-id")

    sessoes_formatadas=[]
    for sessao in sessoes:
        if sessao.data_hora_inicio and sessao.data_hora_fim:
            inicio = sessao.data_hora_inicio#int(sessao.data_hora_inicio.total_seconds // 60)
            fim =  sessao.data_hora_fim#int(sessao.data_hora_fim.total_seconds // 60)
            duracao = fim - inicio
            minutos_total = int(duracao.total_seconds()) // 60
            horas = minutos_total // 60
            minutos = minutos_total % 60

            if horas > 0:
                duracao_formatada = f"{horas}h {minutos}min"
            else:
                duracao_formatada = f"{minutos}min"
        else:
            duracao_formatada = "Sessão em andamento"
        materia = request.POST.get("materia", "").strip()
        sessoes_formatadas.append({
            #"id":sessao.id, em branco até materia ser adicionada
            "materia": materia,#em branco até materia ser adicionada - sessao.id_materia.nome_materia if sessao.id_materia else "Não informada",
            "duracao":duracao_formatada,
            "ciclos":sessao.ciclos_completos,
        })


    return render(request, "app_pomodoro/iniciar_sessao.html", {"sessoes": sessoes_formatadas})


#def iniciar_sessao_vazia(request):
