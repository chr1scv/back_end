from django.db import models


class Tratamientos(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre 

class Mascotas(models.Model):
    nombre = models.CharField(max_length=30)
    microchip = models.IntegerField()
    fecha_de_atencion = models.DateField()
    motivo = models.CharField(max_length=30)
    diagnostico = models.CharField(max_length=30)
    tratamiento = models.ForeignKey(Tratamientos, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=30)
    valor = models.IntegerField()
