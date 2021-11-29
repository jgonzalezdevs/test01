from django.db import models


class Mindicador(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=30)
    fecha = models.DateTimeField()
    valor = models.FloatField(max_length=30)
