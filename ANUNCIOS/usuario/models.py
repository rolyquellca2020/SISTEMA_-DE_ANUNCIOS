from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 255, unique = True)
    apelliidos = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    imagen = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
   
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'