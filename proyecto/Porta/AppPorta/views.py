from datetime import datetime as dt 
from django.http import HttpResponse
from django.template import Template, Context, loader
from AppPorta.models import Curso
from django.shortcuts import render

def saludo(request):
    dia = dt.now()
    texto = f"Hola Como estas? <br> Yo bien <br> {dia}"
    return HttpResponse(texto)

def mi_nombre(request,nombre):
    texto = f"Bienvenido, {nombre} a Coder House"
    return HttpResponse(texto)

def probando_template(request):
    notas = [8,6,9,5,7,8]
    diccionario = {"nombre":"Iñaki","apellido":"Serrano","ahora":dt.now(),"notas":notas}
    return render(request,"AppPorta/index.html")

def curso(request,nombre,numero):
    curso = Curso(nombre=nombre,camada=int(numero))
    curso.save()
    documento = f"Curso: {curso.nombre} <br>Camada: {curso.camada}"
    return HttpResponse(documento)