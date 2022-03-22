from django.contrib import admin

# Register your models here.
from .models import Verduras,Frutas,Fruto_Secos

admin.site.register(Verduras)

admin.site.register(Frutas)

admin.site.register(Fruto_Secos)