from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=20,default="Python")
    camada = models.IntegerField(default=10000)
    fecha_create = models.DateTimeField(auto_now=True,null=True)
    fecha_update = models.DateTimeField(auto_now=True,null=True)