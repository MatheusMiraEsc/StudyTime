from django.db import models

class Materia(models.Model):
    id_usuario = models.IntegerField(null=True)  # colocar como ForeignKey e criar model Usuario futuramente
    nome_materia = models.CharField(max_length=100, null=True, blank=True)
    assuntos = models.TextField(null=True, blank=True)
    tempo_estudado = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.nome_materia if self.nome_materia else "Matéria sem nome"

class Ciclo(models.Model):
    qntd_sessoes = models.IntegerField(null=True, blank=True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)

class Sessao(models.Model):
    id_ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, null=True, blank=True)
    data_hora_inicio = models.DateTimeField(null=True, blank=True)
    data_hora_fim = models.DateTimeField(null=True, blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='sessoes', null=True, blank=True)