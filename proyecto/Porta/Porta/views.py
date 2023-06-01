from datetime import datetime as dt 
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    dia = dt.now()
    texto = f"Hola Como estas? <br> Yo bien <br> {dia}"
    return HttpResponse(texto)

def mi_nombre(request,nombre):
    texto = f"Bienvenido, {nombre} a Coder House"
    return HttpResponse(texto)

def probando_template(request):
    diccionario = {"nombre":"Iñaki","apellido":"Serrano"}
    mi_html = open('./Porta/plantillas/index.html') #Abrimos el archivo html
    plantilla = Template(mi_html.read()) #Creamos el template usando la funcion
    mi_html.close() #Cerramos el archivo ya que lo tenemos en la variable plantilla
    mi_contexto = Context(diccionario) #Creamos un contexto
    documento = plantilla.render(mi_contexto) #Terminamos de construir el template renderizandolo con su contexto
    return HttpResponse(documento) #Corremos
