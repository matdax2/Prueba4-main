from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from PrimerApp.forms import *

def inicio(request):
    return render(request, "PrimerApp/base.html")

def cursoFormulario(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            curso = Curso(nombre = informacion["grupo"], grupo = informacion["grupo"])
            curso.save()
            return render(request, "PrimerApp/base.html")
    else:
        formulario = CursoFormulario()
    return render(request, "PrimerApp/cursoFormulario.html", {"formulario": formulario})

def profFormulario(request):
    if request.method == "POST":
        prof_formulario = ProfeFormulario(request.POST)
        print(prof_formulario)
        if prof_formulario.is_valid:
            informacion = prof_formulario.cleaned_data
            profesor = Profesor(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"], profesion = informacion["profesion"])
            profesor.save()
            return render(request, "PrimerApp/base.html")
    else:
        prof_formulario = ProfeFormulario()
    return render(request, "PrimerApp/profeFormulario.html", {"prof_formulario": prof_formulario})

def formEstudiante(request):
    if request.method == "POST":
        formulario_est = Estudiante_Form(request.POST)
        print(formulario_est)
        if formulario_est.is_valid:
            informacion = formulario_est.cleaned_data
            estudiante = Estudiante(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"])
            estudiante.save()
            return render(request, "PrimerApp/base.html")
    else:
        formulario_est = Estudiante_Form()
    return render(request, "PrimerApp/estFormulario.html", {"formulario_est": formulario_est})

def busqueda(request):
    return render(request, "PrimerApp/buscador.html")

def buscar(request):
    if request.GET["grupo"]:
        grupo = request.GET["grupo"]
        cursos = Curso.objects.filter(grupo__icontains=grupo)
        return render(request, "PrimerApp/busqueda.html", {"cursos":cursos, "grupo": grupo})
    else:
        respuesta = "No enviastes datos"
    return HttpResponse(respuesta)

def Geralt_De_Rivia(request):
    return render(request, "PrimerApp/Gerardo.html")