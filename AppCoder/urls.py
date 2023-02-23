from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    # path('', inicio, name='inicio'),
    # path('cursos/', cursos, name='cursos'),
    # path('profesores/', profesores, name='profesores'),
    # path('estudiantes/', estudiantes, name='estudiantes'),
    # path('entregables/', entregables, name='entregables'),
    # path('curso-formulario/', curso_formulario, name='curso-formulario'),
    # path('profesor-formulario/', profesor_formulario, name='profesor-formulario'),
    # path('busqueda-camada/', busqueda_camada, name='busqueda-camada'),
    # path('buscar/', buscar, name='buscar'),
    # path('eliminar-profesor/<profesor_id>', eliminar_profesor, name='eliminar-profesor'),
    # path('editar-profesor/<profesor_id>', editar_profesor, name='editar-profesor'),
    path('', inicio, name='inicio'),
    path('cursos/', CursoList.as_view(), name='cursos'),
    path('detalle/<pk>', CursoDetalle.as_view(), name='detalle'),
    path('nuevo/', CursoCreacion.as_view(), name='nuevo'),
    path('editar/<pk>', CursoUpdate.as_view(), name='editar'),
    path('eliminar/<pk>', CursoDelete.as_view(), name='eliminar'),
    path('login/', login_request, name='login'),
    path('registro/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('editar-perfil/', editar_perfil, name='editar-perfil'),
    path('agregar-avatar/', agregar_avatar, name='agregar-avatar'),
]
