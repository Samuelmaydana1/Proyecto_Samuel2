from django.urls import path
from AppSamuel import views

urlpatterns = [
    path('', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables)
]
