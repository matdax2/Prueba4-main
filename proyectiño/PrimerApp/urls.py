from django.urls import path
from PrimerApp import views

urlpatterns = [
    path('PrimerApp/', views.inicio, name="Principal"),
    path('formulario/', views.cursoFormulario, name="Formulario de cursos"),
    path('profForms/', views.profFormulario, name="Formulario de profesores"),
    path('estForms/', views.formEstudiante, name="Formulario de estudiantes"),
    path('busqueda/', views.busqueda, name="busqueda"),
    path('buscar/', views.buscar, name="Buscador"),
    path('gerardo/', views.Geralt_De_Rivia, name="gerardito"),
    path('LecturaProf/', views.leerProf, name="Profesores"),
    path('listEstudiantes/', views.leerEstudiante, name="Estudiantes"),
]
