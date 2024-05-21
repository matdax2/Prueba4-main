from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from PrimerApp.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "PrimerApp/base.html")

def cursoFormulario(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            curso = Curso(curso = informacion["curso"], grupo = informacion["grupo"])
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
    return render(request, "PrimerApp/busqueda.html")

def buscar(request):
    query = request.GET.get("grupo")
    if query:
        resultado = Curso.objects.filter(grupo__icontains=query)
    return render(request, "PrimerApp/busqueda.html", {"resultado": resultado, "query": query})

def Geralt_De_Rivia(request):
    return render(request, "PrimerApp/Gerardo.html")

def leerProf(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "PrimerApp/leerProf.html", contexto)

def leerEstudiante(request):
    estudiantes = Estudiante.objects.all()
    contexto = {"estudiantes": estudiantes}
    return render(request, "PrimerApp/leerEstudiante.html", contexto)

def leerCurso(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "PrimerApp/leerCurso.html", contexto)

def borrarProfe(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "PrimerApp/leerProf.html", contexto)

def borrarEstudiante(request, estudiante_nombre):
    estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    contexto = {"estudiantes": estudiantes}
    return render(request, "PrimerApp/leerEstudiante.html", contexto)

def borrarCurso(request, curso_curso):
    curso = Curso.objects.get(curso=curso_curso)
    curso.delete()
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "PrimerApp/leerCurso.html", contexto)

def updateProfe(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == "POST":
        formulario = ProfeFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            profesor.nombre = informacion["nombre"]
            profesor.apellido = informacion["apellido"]
            profesor.email = informacion["email"]
            profesor.profesion = informacion["profesion"]
            profesor.save()
            return render(request, "PrimerApp/base.html")
    else:
        formulario = ProfeFormulario(initial={"nombre": profesor.nombre, "apellido": profesor.apellido,
                                              "email": profesor.email, "profesion": profesor.profesion})
    return render(request, "PrimerApp/updateProfe.html", {"formulario": formulario, "profesor_nombre": profesor_nombre})

def updateEstudiante(request, estudiante_nombre):
    estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
    if request.method == "POST":
        formulario = Estudiante_Form(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion["nombre"]
            estudiante.apellido = informacion["apellido"]
            estudiante.email = informacion["email"]
            estudiante.save()
            return render(request, "PrimerApp/base.html")
    else:
        formulario = Estudiante_Form(initial={"nombre": estudiante.nombre, "apellido": estudiante.apellido,
                                              "email": estudiante.email})
    return render(request, "PrimerApp/updateEstudiante.html", {"formulario": formulario, "estudiante_nombre": estudiante_nombre})

def updateCurso(request, curso_curso):
    curso = Curso.objects.get(curso=curso_curso)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            curso.curso = informacion["curso"]
            curso.grupo = informacion["grupo"]
            curso.save()
            return render(request, "PrimerApp/base.html")
    else:
        formulario = CursoFormulario(initial={"curso": curso.curso, "grupo": curso.grupo})
    return render(request, "PrimerApp/updateCurso.html", {"formulario": formulario, "curso_curso": curso_curso})

class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "PrimerApp/listCurso.html"

class CursoDetailView(DetailView):
    model = Curso
    template_name = "PrimerApp/cursoDetalle.html"

class CursoCreateView(CreateView):
    model = Curso
    template_name = "PrimerApp/CreateCurso.html"
    success_url = reverse_lazy("ListaCursos")
    fields = ["curso", "grupo"]

class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "PrimerApp/CursoUpdate.html"
    success_url = reverse_lazy("ListaCursos")
    fields = ["curso", "grupo"]

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "PrimerApp/cursoDelete.html"
    success_url = reverse_lazy("ListaCursos")