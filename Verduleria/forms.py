from django import forms

class Verduras_formulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    precio = forms.CharField(max_length=4)
    
class Frutas_formulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    precio = forms.CharField(max_length=4)

class Fruto_Secos_formulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.CharField(max_length=4)