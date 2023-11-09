from django.db import models

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    carnet = models.CharField(max_length=10)


