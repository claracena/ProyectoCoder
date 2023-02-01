from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre='Backend', camada='12345')
    curso.save()
    respuesta = f'Curso: {curso.nombre}, Camada: {curso.camada}'

    return HttpResponse(respuesta)
