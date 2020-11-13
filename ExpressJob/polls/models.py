from django.db import models
from enum import Enum


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
   # fotografia = models.ImageField(max_length=100)
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre_usuario

class Trabajador(Persona):
        descripcion_trabajador = models.CharField(max_length=150)
        telefono_fijo = models.CharField(max_length=10)
        def __str__(self):
           return self.descripcion

class Consumidor(Persona):
    FechaRegistro = models.DateTimeField()


class Solicitud(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    descripcion_solicitud = models.CharField(max_length=150)
    imagen_solicitud = models.ImageField(max_length=100)
    #tipo_servicio_solicitado = models.CharField(max_length=10,
                                    # choices=[(tag, tag.value) for tag in TipoServicio])
    def __str__(self):
        return self.descripcion_solicitud

class Direccion(models.Model):
    calle = models.CharField(max_length=150)
    calle_colindancia = models.CharField(max_length=150)
    colinia = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=50)
    numero_interior = models.CharField(max_length=50)

class horario(models.Model):
    dia = models.CharField(max_length=50)
    hora_inicio = models.CharField(max_length=50)
    hora_final = models.CharField(max_length=50)

class Servicio(models.Model):
    descripcion_servicio = models.CharField(max_length=150)
    precio_promedio = models.CharField(max_length=50)
    trabajadores = models.ManyToManyField(Trabajador)
   # tipo_servicio_contratado = models.CharField(max_length=10,
                                     #choices=[(tag, tag.value) for tag in TipoServicio])

#class Detalles(models.Model):

class Trato(models.Model):
    fecha_inicio = models.CharField(max_length=10)
    fecha_termino = models.CharField(max_length=10)
    precio = models.FloatField

class Opinion(models.Model):
    trato = models.OneToOneField(Trato, on_delete=models.CASCADE, primary_key=True)
    comentario = models.CharField(max_length=150)
    puntaje = models.IntegerField()



class TipoServicio(Enum): #A subclass of Enum
    AL = "Albañileria"
    FT = "Fontaneria"
    EL = "Electricista"
    MEC = "Mecanico"
    PT = "Pintura"
    CP = "Carpinteria"
    HR = "Herrería"
    VD = "Vidrería"
    IF = "Informatica"
    HJ = "Hojalateria"
    ED = "Educación"





