
from django.contrib import admin
from django.urls import path
from app_pomodoro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #rota, view responsavel, nome referencia
    path('', views.home, name='home'),
]
