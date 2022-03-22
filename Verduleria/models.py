from django.db import models

class Verduras (models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f"{self.nombre} {self.precio}"
    
class Frutas (models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.CharField(max_length=4)

    def __str__(self) -> str:
        return f"{self.nombre} {self.precio}"
    
class Fruto_Secos (models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=4)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.precio}"
    
    