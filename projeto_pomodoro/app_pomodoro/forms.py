from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registroform(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Informe um endereço de e-mail válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')