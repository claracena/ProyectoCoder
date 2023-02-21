from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Avatar

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class MyUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

class UserEditForm(UserCreationForm):

    # Agregamos las opciones que dejamos editar
    email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    username = forms.CharField(label='Nombre de usuario')
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k: '' for k in fields}

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = '__all__'
        exclude = ['user']


