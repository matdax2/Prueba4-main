from django import forms

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