from django.db import models

# Create your models here.
class Ciclo(models.Model):
    #id_ciclo = models.IntegerField(null=True)
    tempo_estudo = models.DurationField(null=True)
    tempo_descanso = models.DurationField(null=True)

    def __str__(self):
        return f"Estudo: {self.tempo_estudo} min, Descanso: {self.tempo_descanso} min"
    

class Materia(models.Model):
    #id_materia = models.IntegerField(null=True)
    id_usuario = models.IntegerField(null=True)
    nome_materia = models.TextField(null=True) # confirmar se o field ta certo
    assuntos = models.TextField(null=True) #ajustar para pegar todos assuntos
    tempo_estudado = models.TimeField(null=True)

class Sessao(models.Model):
    #id_sessao = models.IntegerField(null=True) aparentemente o proprio django faz o id automatico
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)
    data_hora_inicio = models.TimeField(null=True)
    data_hora_fim = models.TimeField(null=True)
    ciclos_completos = models.IntegerField(null=True)