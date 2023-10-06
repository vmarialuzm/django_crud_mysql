from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    description = models.TextField(verbose_name='Descripción', null=True)

