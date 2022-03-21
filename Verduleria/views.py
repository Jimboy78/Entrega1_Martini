from django.shortcuts import render

# Create your views here.

def verduleria(request):
    form = None
    return render(request, "verduleria.html", {"form": form}) 


def agregar_modelo_verduras(request):
    form = None
    return render(request, "formulario_verdu.html", {"form": form}) 


def agregar_modelo_frutas(request):
    form = None
    return render(request, "formulario_fruta.html", {"form": form}) 
    

def agregar_modelo_frutos_secos(request):
    form = None
    return render(request, "formulario_fruto_seco.html", {"form": form}) 