from django.db import models

# Create your models here.
class Ciclo(models.Model):
    id_ciclo = models.IntegerField(null=True)
    tempo_estudo = models.DurationField()
    tempo_descanso = models.DurationField()

    def __str__(self):
        return f"Estudo: {self.tempo_estudo} min, Descanso: {self.tempo_descanso} min"
    

class Materia(models.Model):
    id_materia = models.IntegerField()

class Sessao(models.Model):
    id_sessao = models.IntegerField()
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)
    data_hora_inicio = models.TimeField()
    data_hora_fim = models.TimeField()
    ciclos_completos = models.IntegerField()