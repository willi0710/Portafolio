from django.db import models

# Create your models here.
class Proyecto(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length = 100)
    description= models.TextField(verbose_name='Descripcion', max_length = 1000)
    image= models.ImageField(upload_to = 'proyectos/images', verbose_name='Imagenes') 
    link = models.URLField(verbose_name='Direccion web', null=True, blank=True)
    created= models.DateTimeField(auto_now_add = True, verbose_name='Creacion')
    updated = models.DateTimeField(auto_now = True, verbose_name='Actualizacion')