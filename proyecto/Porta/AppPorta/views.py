from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from AppPorta.forms import CursoFormulario, BuscaCursoForm


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

def formulario(request):
    if request.method == 'POST':
        print(f"\n\n{request.POST}\n\n")
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        curso.save()
        return render(request, "AppPorta/index.html")        
    return render(request, "AppPorta/formulario.html")

def curso_formulario(request):
 
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppPorta/index.html")
      else:
            miFormulario = CursoFormulario()
      return render(request, "AppPorta/formulario_api.html", {"miFormulario": miFormulario}) 
  
def buscar_curso(request):
    if request.method == "POST":
        busca_curso = BuscaCursoForm(request.POST)
        if busca_curso.is_valid():
            info = busca_curso.cleaned_data
            cursos = Curso.objects.filter(nombre__icontains=info["curso"])
            return render(request, "AppPorta/lista.html", {"cursos":cursos})
    else:
        busca_curso = BuscaCursoForm()
        return render(request, "AppPorta/buscar_curso.html", {"miFormulario": busca_curso})