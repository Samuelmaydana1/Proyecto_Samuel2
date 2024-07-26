from django.urls import path
from AppSamuel import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('profesores/', views.profesores, name='Profesores'),
    path('entregables/', views.entregables, name='Entregables'),
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    path('form-con-api/', views.form_con_api, name="FormConApi")
]
