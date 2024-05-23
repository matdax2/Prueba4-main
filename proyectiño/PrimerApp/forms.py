from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    grupo = forms.IntegerField()

class ProfeFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class Estudiante_Form(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

#class Registro(UserCreationForm):
    #usuario = forms.CharField()
    #contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #contraseña2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    #class Meta:
        #model = User
        #fields  = ['usuario', 'contraseña', 'contraseña2']
        #help_texts = {k:"" for k in fields}