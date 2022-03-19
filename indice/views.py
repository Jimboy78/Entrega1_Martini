from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render


def Inicio (request): 

    return render(request, "index.html", {})
    

def plantillaza(request):

    return render(request, "mi-plantilla.html")

    