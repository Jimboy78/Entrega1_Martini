from django.urls import path
from .views import Inicio, plantillaza

urlpatterns = [
    
    path('', Inicio, name="index"),
    path('plantillaza/', plantillaza),
    
]
 