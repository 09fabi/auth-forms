from django.db import models

# Create your models here.


class Activo(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    proyecto = models.CharField(max_length=50)
    estado_activo = models.CharField(max_length=50)
    ordenar_por = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class Report(models.Model):
    nombre_responsable = models.CharField(max_length=255)
    email = models.EmailField()
    estado_activo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    activo_titulo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_responsable
