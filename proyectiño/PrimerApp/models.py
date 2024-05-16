from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.grupo}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profesion = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
    

