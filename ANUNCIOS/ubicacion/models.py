from django.db import models

# Create your models here.

class Ubicacion(models.Model):
    """Model definition for Reserva."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    pais =  models.CharField(max_length = 255, unique = True)
    cuidad = models.CharField(max_length = 255, unique = True)
    direccion =  models.CharField(max_length = 255, unique = True)   
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    class Meta:
        """Meta definition for ubicacion."""

        verbose_name = 'Ubicacion'
        verbose_name_plural = 'ubucaciones'