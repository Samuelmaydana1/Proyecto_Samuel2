from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField(
        label="Fecha de entrega",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    entregado = forms.BooleanField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField(max_length=20)