from django.db import models

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.EmailField()

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.nombre
