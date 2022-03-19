from django.db import models

# Create your models here.

class Verduras (models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.CharField
    
class Frutas (models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.CharField

class Fruto_Secos (models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.CharField