from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profesion = models.CharField(max_length=100)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    

