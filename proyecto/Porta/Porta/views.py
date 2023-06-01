from datetime import datetime as dt 
from django.http import HttpResponse

def saludo(request):
    dia = dt.now()
    texto = f"Hola Como estas? <br> Yo bien <br> {dia}"
    return HttpResponse(texto)

def mi_nombre(request,nombre):
    texto = f"Bienvenido, {nombre} a Coder House"
    return HttpResponse(texto)