from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuario(UserCreationForm):
    email = forms.EmailField(label = "Email de usuario")
    PROFESIONES = (
        ("Cineasta", "Cineasta"),
        ("Actor", "Actor"),
        ("Escritor", "Escritor"),
        ("Escultor", "Escultor"),
        ("Fotografo", "Fotógrafo"),
        ("Grabador", "Grabador"),
        ("Musico", "Músico"),
        ("Animador", "Animador"),
        ("Pintor", "Pintor"),
        ("Ilustrador", "Ilustrador"),
        ("Ninguno", "Ninguno"),
    )
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES)
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "profesion",  "password1", "password2"]


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = "Email de usuario")
    PROFESIONES = (
        ("Cineasta", "Cineasta"),
        ("Actor", "Actor"),
        ("Escritor", "Escritor"),
        ("Escultor", "Escultor"),
        ("Fotografo", "Fotógrafo"),
        ("Grabador", "Grabador"),
        ("Musico", "Músico"),
        ("Animador", "Animador"),
        ("Pintor", "Pintor"),
        ("Ilustrador", "Ilustrador"),
        ("Ninguno", "Ninguno"),
    )
    profesion = forms.ChoiceField(label="Profesion", choices=PROFESIONES)
    
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)


    class Meta:
        model = User
        fields = ["email", "profesion", "password1", "password2", "first_name", "last_name"]


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)