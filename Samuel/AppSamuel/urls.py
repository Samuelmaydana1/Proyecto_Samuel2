from django.urls import path
from AppSamuel import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('profesores/', views.profesores, name='Profesores'),
    path('entregables/', views.entregables, name='Entregables'),
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    path('estudiante-formulario/', views.estudiante_formulario, name="EstudianteFormulario"),
    path('profesor-formulario/', views.profesor_formulario, name="ProfesorFormulario"),
    path('entregable-formulario/', views.entregable_formulario, name="EntregableFormulario"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]
