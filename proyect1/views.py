from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render


def Inicio (request, nombre): 

    Nombres = f"Holii {nombre}"
    
    return HttpResponse(Nombres)

def plantillaza(request):

    return render(request, "mi-plantilla.html")