
from django.contrib import admin
from django.urls import path
from app_pomodoro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #rota, view responsavel, nome referencia
    path('', views.home, name='home_integrado'),
    path('iniciar_sessao/', views.iniciar_sessao, name='iniciar_sessao'),

     # Rotas de Matérias
    path('materias/', views.listar_materias, name='listar_materias'),
    path('materias/nova/', views.criar_materia, name='criar_materia'),
    path('materias/editar/<int:id>/', views.editar_materia, name='editar_materia'),
    path('materias/excluir/<int:id>/', views.excluir_materia, name='excluir_materia'),
]
