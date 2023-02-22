from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario, MyUserCreationForm, UserEditForm

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

class CursoCreacion(LoginRequiredMixin, CreateView):

    model = Curso
    template_name = 'AppCoder/curso-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'camada']

class CursoUpdate(LoginRequiredMixin, UpdateView):

    login_url = 'login/'
    model = Curso
    template_name = 'AppCoder/curso-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'camada']

class CursoDelete(LoginRequiredMixin, DeleteView):

    model = Curso
    template_name = 'AppCoder/curso-eliminar.html'
    success_url = reverse_lazy('inicio')

def login_request(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            cont = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=cont)

            if user is not None:
                login(request, user)
                contexto = {'mensaje': f'Bienvenido {usuario}'}
                return render(request, 'AppCoder/inicio.html', contexto)
            else:
                contexto = {'mensaje': f'El usuario no existe', 'form': form}
                return render(request, 'AppCoder/login.html', contexto)
        else:
            contexto = {'mensaje': f'Los datos son erroneos', 'form': form}
            return render(request, 'AppCoder/login.html', contexto)
    
    contexto = {'form': form}
    return render(request, 'AppCoder/login.html', contexto)

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            contexto = {'mensaje': 'Usuario creado satisfactoriamente'}
            return render(request, 'AppCoder/inicio.html', contexto)
    else:
        # form = UserCreationForm()
        form = MyUserCreationForm()
        contexto = {'form': form}
        return render(request, 'AppCoder/registro.html', contexto)

@login_required
def editar_perfil(request):
    usuario = User.objects.get(username=request.user)

    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']

            usuario.save()

            return redirect('/')
    
    else:
        mi_formulario = UserEditForm(initial={'username': usuario.username,
                                    'email': usuario.email,
                                    'last_name': usuario.last_name,
                                    'first_name': usuario.first_name})

    return render(request, 'AppCoder/editar-perfil.html', {'mi_formulario': mi_formulario})
