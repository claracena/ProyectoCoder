from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

# def profesores(request):
#     return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def curso_formulario(request):

    # request.POST = {'curso': 'lo que escriba el usuario en el formulario', 'camada': 'lo que escriba el usuario en el formulario'}
    # if request.method == 'POST':
    #     nuevo_curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
    #     nuevo_curso.save()
    #     return redirect('inicio')

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            nuevo_curso.save()
            return redirect('inicio')
        
    mi_formulario = CursoFormulario()
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

def busqueda_camada(request):
    return render(request, 'AppCoder/busqueda-camada.html')

def buscar(request):
    
    if request.GET['camada']:
        mi_camada = request.GET['camada']
        resultado = Curso.objects.filter(camada__icontains = mi_camada)

        return render(request, 'AppCoder/resultados-busqueda.html', {'cursos': resultado, 'camada': mi_camada})

    respuesta = 'No se encontro esa camada'
    return HttpResponse(respuesta)

def profesores(request):
    profesores = Profesor.objects.all()
    contexto = {'profesores': profesores}
    return render(request, 'AppCoder/profesores.html', contexto)

def eliminar_profesor(request, profesor_id):
    profesor = Profesor.objects.get(id=profesor_id)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {'profesores': profesores}
    return render(request, 'AppCoder/profesores.html', contexto)

def editar_profesor(request, profesor_id):

    profesor = Profesor.objects.get(id=profesor_id)

    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()

            profesores = Profesor.objects.all()
            contexto = {'profesores': profesores}
            return render(request, 'AppCoder/profesores.html', contexto)
    else:
        mi_formulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
        contexto = {'mi_formulario': mi_formulario, 'profesor_id': profesor.id}
        return render(request, 'AppCoder/editar-profesor.html', contexto)

class CursoList(ListView):

    model = Curso
    template_name = 'AppCoder/cursos-list.html'

class CursoDetalle(DetailView):

    model = Curso
    template_name = 'AppCoder/curso-detalle.html'

class CursoCreacion(CreateView):

    model = Curso
    template_name = 'AppCoder/curso-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):

    model = Curso
    template_name = 'AppCoder/curso-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):

    model = Curso
    template_name = 'AppCoder/curso-eliminar.html'
    success_url = reverse_lazy('inicio')
