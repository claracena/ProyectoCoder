from django.shortcuts import render, redirect

from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def curso_formulario(request):

    if request.method == 'POST':
        # Aquí recibiremos toda la información enviada mediante el formulario
        mi_formulario = CursoFormulario(request.POST)

        # Validaremos que los datos correspondan con los esperados
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return redirect('inicio')

    else:
        # Inicializamos un formulario vacío para construir el HTML
        mi_formulario = CursoFormulario()

    # Mostramos la vista del formulario pero pasando el formulario vacío como contexto
    return render(request, 'AppCoder/curso-formulario.html', {'formulario_curso': mi_formulario})

def profesor_formulario(request):
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                email=informacion['email'],
                                profesion=informacion['profesion'])
            profesor.save()
            return redirect('inicio')
    else:
        mi_formulario = ProfesorFormulario()
        return render(request, 'AppCoder/profesor-formulario.html', {'formulario_profesor': mi_formulario})



