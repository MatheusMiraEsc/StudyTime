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
        nome_M = request.POST.get("materia", "").strip()
        ciclos = int(request.POST.get("ciclos", 0))

        materia = None
        if nome_M:
            materia = Materia.objects.filter(nome_materia__iexact=nome_M).first()# ajustar para não precisar de nome e para selecionar a materia certa caso aja mais de um ou não exista
        
        hora_inicio = datetime.now().time()
        #hora_fim = datetime.strptime(request.POST.get("fim"), "%H:%M:%S").time()
        
        sessao = Sessao.objects.create(
            id_materia = materia, #ou Materia.objects.get(id)??, mesmo com materia, encontrar como pegar de outra tabela
            data_hora_inicio = hora_inicio,
            data_hora_fim = hora_inicio,
            ciclos_completos = ciclos,
        )
        return redirect("iniciar_sessao") #À ajustar
    sessoes = Sessao.objects.all().order_by("-id")
    return render(request, "app_pomodoro/iniciar_sessao.html", {"sessoes": sessoes}) # O que fazer??


#def iniciar_sessao_vazia(request):
