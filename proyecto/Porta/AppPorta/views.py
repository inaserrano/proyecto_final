from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,"AppPorta/index.html")

def cursos(request):
    return render(request,"AppPorta/cursos.html")

def profesores(request):
    return render(request,"AppPorta/profesores.html")

def estudiantes(request):
    return render(request,"AppPorta/estudiantes.html")

def entregables(request):
    return render(request,"AppPorta/entregables.html")