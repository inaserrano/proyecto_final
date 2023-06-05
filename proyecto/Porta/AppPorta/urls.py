
from django.urls import path
from .views import(
    saludo,
    mi_nombre,
    probando_template,
    curso
)
urlpatterns = [
    path('saludo/',saludo),
    path('nombre/<nombre>',mi_nombre),
    path('probando_template/',probando_template),
    path('curso/<nombre>/<numero>/',curso)
]
