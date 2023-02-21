from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return self.nombre + ' (' + str(self.camada) + ')'

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        verbose_name_plural = 'Profesores'

class Entregable(models.Model):
    
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

class Avatar(models.Model):
    # vínculo con el perfil del usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # subcarpeta avatares
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username



