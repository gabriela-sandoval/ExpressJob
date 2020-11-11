from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return self.persona_text

class Usuario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=20)
    def __str__(self):
        return self.usuario_text