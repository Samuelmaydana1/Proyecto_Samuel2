from django.shortcuts import render
from AppSamuel.models import Curso, Estudiante, Profesor, Entregable
from AppSamuel.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario, EntregableFormulario, BuscaCursoForm

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

def estudiante_formulario(request):
    if request.method == "POST":
        mi_formulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()

            return render(request, "AppSamuel/index.html")
    else:
        mi_formulario = EstudianteFormulario()

    return render(request, "AppSamuel/form_con_api.html", {"mi_formulario": mi_formulario})

def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            profesor.save()

            return render(request, "AppSamuel/index.html")
    else:
        mi_formulario = ProfesorFormulario()

    return render(request, "AppSamuel/form_con_api.html", {"mi_formulario": mi_formulario})

def entregable_formulario(request):
    if request.method == "POST":
        mi_formulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            entregable = Entregable(nombre=informacion["nombre"], fecha_de_entrega=informacion["fecha_de_entrega"], entregado=informacion["entregado"])
            entregable.save()

            return render(request, "AppSamuel/index.html")
    else:
        mi_formulario = EntregableFormulario()

    return render(request, "AppSamuel/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppSamuel/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "AppSamuel/buscar_form_con_api.html", {"mi_formulario": mi_formulario})