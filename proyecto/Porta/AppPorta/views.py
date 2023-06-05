from django.shortcuts import render
from AppPorta.resources.utils import fecha
from django.http import HttpResponse

def pag_(request):
    devuelve_fecha = fecha
    return HttpResponse(f"Esta es la fecha{devuelve_fecha}")