from django.shortcuts import render
from AppSamuel.models import Curso
from AppSamuel.forms import CursoFormulario

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

def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(
            nombre=request.POST['curso'],
            camada=request.POST['camada']
        )
        curso.save()

        return render(request, "AppSamuel/index.html")

    return render(request,"AppSamuel/curso_formulario.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "AppSamuel/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "AppSamuel/form_con_api.html", {"mi_formulario": mi_formulario})