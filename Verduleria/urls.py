from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.verduleria, name="verduleria"),
    path('form_verduras/', views.agregar_modelo_verduras, name="agregar_modelo_verdus"),
    path('form_frutas/', views.agregar_modelo_frutas, name="agregar_modelo_frutas"),
    path('form_frutos_secos/', views.agregar_modelo_frutos_secos, name="agregar_modelo_frutos_secos"),
]
 