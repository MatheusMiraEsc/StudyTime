from django.shortcuts import render
from datetime import timedelta
# Create your views here.

def home(request):
    return render(request, 'app_pomodoro/home.html')

# def iniciar_sessao():
