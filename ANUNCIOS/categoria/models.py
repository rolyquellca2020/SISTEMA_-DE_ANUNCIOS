from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']


class Anuncio(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField('Imagenes', upload_to='imagen/', max_length=255, null=True, blank = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    midificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-id']