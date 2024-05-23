from django.urls import path
from PrimerApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('PrimerApp/', views.inicio, name="Principal"),
    path('formulario/', views.cursoFormulario, name="Formulario de cursos"),
    path('profForms/', views.profFormulario, name="Formulario de profesores"),
    path('estForms/', views.formEstudiante, name="Formulario de estudiantes"),
    #path('busqueda/', views.busqueda, name="busqueda"),
    path('buscar/', views.buscar, name="Buscador"),
    path('gerardo/', views.Geralt_De_Rivia, name="gerardito"),
    path('LecturaProf/', views.leerProf, name="Profesores"),
    path('listEstudiantes/', views.leerEstudiante, name="Estudiantes"),
    path('listCursos/', views.leerCurso, name="Cursos"),
    path('borrarProf/<profesor_nombre>', views.borrarProfe, name="Borrar Profesor"),
    path('borrarEst/<estudiante_nombre>', views.borrarEstudiante, name="Borrar Estudiante"),
    path('borrarCurso/<curso_curso>', views.borrarCurso, name="Borrar Curso"),
    path('updateProfe/<profesor_nombre>', views.updateProfe, name="Update Profe"),
    path('updateEst/<estudiante_nombre>', views.updateEstudiante, name="Update Estudiante"),
    path('updateCurso/<curso_curso>', views.updateCurso, name="Update Curso"),
    path('curso/lista', views.CursoListView.as_view(), name="ListaCursos"),
    path('curso/crear', views.CursoCreateView.as_view(), name="CreateCurso"),
    path('curso/<pk>', views.CursoDetailView.as_view(), name="CursoDetalle"),
    path('curso/<pk>/update', views.CursoUpdateView.as_view(), name="CursoUpdate"),
    path('curso/<pk>/borrar', views.CursoDeleteView.as_view(), name="CursoDelete"),
    path('login', views.LoginRequest, name="Login"),
    path('registro', views.registrarse, name="Registrarse"),
    path('cerrarSesion', LogoutView.as_view(template_name='PrimerApp/CerrarSesion.html'), name="Cerrar Sesion")
]
