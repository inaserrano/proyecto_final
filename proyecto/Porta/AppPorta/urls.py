from django.urls import path
from AppPorta import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('cursos/',views.cursos, name='curso'),
    path('profesores/',views.profesores, name='profesor'),
    path('estudiantes/',views.estudiantes, name='estudiante'),
    path('entregables/',views.entregables, name='entregable')
]
