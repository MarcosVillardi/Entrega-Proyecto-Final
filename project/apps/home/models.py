from django.db import models

class Cliente(models.Model):
    usuario_cliente = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField()
    email = models.EmailField()
    numero_telefono = models.PositiveIntegerField()
    def __str__(self):
        return self.usuario_cliente   
class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()
    fecha_llegada = models.DateField()
    fecha_salida = models.DateField()
    numero_habitacion = models.PositiveSmallIntegerField()
    comentarios = models.TextField(null=True)
    def __str__(self):
        return self.apellido
class Garaje(models.Model):
    nombre = models.CharField(max_length=50)
    titular = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    capacidad = models.PositiveSmallIntegerField()
    patente = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    comentarios = models.TextField(null=True)
    def __str__(self):
        return self.patente