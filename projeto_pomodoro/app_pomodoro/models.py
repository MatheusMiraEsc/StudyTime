from django.db import models

# Create your models here.
class Ciclo(models.Model):
    qntd_sessoes = models.IntegerField(null=True, blank=True)

class Sessao(models.Model):
    id_ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, null=True, blank=True)
    data_hora_inicio = models.DateTimeField(null=True, blank=True)
    data_hora_fim = models.DateTimeField(null=True,blank=True)


class Materia(models.Model):
    #id_materia = models.IntegerField(null=True)
    id_usuario = models.IntegerField(null=True)
    nome_materia = models.TextField(null=True) # confirmar se o field ta certo
    assuntos = models.TextField(null=True) #ajustar para pegar todos assuntos
    tempo_estudado = models.TimeField(null=True)
