from django.db import models

# Create your models here.
class Ciclo(models.Model):
    qntd_sessoes = models.IntegerField(null=True, blank=True)

class Sessao(models.Model):
    id_ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, null=True, blank=True)
    data_hora_inicio = models.DateTimeField(null=True, blank=True)
    data_hora_fim = models.DateTimeField(null=True,blank=True)


class Materia(models.Model):
    id_usuario = models.IntegerField(null=True)
    nome_materia = models.CharField(max_length=100, null=True, blank=True)  # antes era TextField
    assuntos = models.TextField(null=True, blank=True)  
    tempo_estudado = models.DurationField(null=True, blank=True)  # antes era TimeField

    def __str__(self):
        return self.nome_materia if self.nome_materia else "Matéria sem nome"
