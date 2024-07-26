from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppSamuel/index.html')

def cursos(request):
    return render(request, 'AppSamuel/cursos.html')

def estudiantes(request):
    return render(request, 'AppSamuel/estudiantes.html')

def profesores(request):
    return render(request, 'AppSamuel/profesores.html')

def entregables(request):
    return render(request, 'AppSamuel/entregables.html')