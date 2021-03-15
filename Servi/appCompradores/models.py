from django.db import models
from django.db.models.fields import CharField, FloatField

class Compradores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)
    longitud = models.FloatField(max_length=50,default=0)
    latitud = models.FloatField(max_length=50,default=0)
    estado_geo = models.BooleanField(default=False)
