from datetime import datetime as dt 
from django.http import HttpResponse
from django.template import Template, Context, loader


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
    # mi_html = open('./Porta/plantillas/index.html')
    # plantilla = Template(mi_html.read()) 
    # mi_html.close() 
    # mi_contexto = Context(diccionario) 
    plantilla = loader.get_template('index.html') 
    dic = plantilla.render(diccionario)
    return HttpResponse(dic) 
