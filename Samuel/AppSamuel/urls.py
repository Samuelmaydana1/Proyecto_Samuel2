from django.urls import path
from AppSamuel import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('profesores/', views.profesores, name='Profesores'),
    path('entregables/', views.entregables, name='Entregables'),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]
