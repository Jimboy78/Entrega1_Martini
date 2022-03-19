from django.db import models

# Create your models here.

class Verduras (models.Model):
    nombre = models.CharField(max_length=20)
     #= models.CharField(max_length=20)

class Frutas (models.Model):
    nombre = models.CharField(max_length=20)
    ... 

class Fruto_Secos (models.Model):
    nombre = models.CharField(max_length=20)
    ... 