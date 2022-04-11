from django.db import models

# Create your models here.
class Familiar1(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.IntegerField()

class Familiar2(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.IntegerField()

class Familiar3(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.IntegerField()

class FechaConsulta(models.Model):
    fecha = models.DateField()