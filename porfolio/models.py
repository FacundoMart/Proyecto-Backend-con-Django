from django.db import models

# Create your models here.
# En el class projects creamos los atributos de la base de datos.

class Project(models.Model):
    title = models.CharField(max_length=200)
    descripcion = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField (auto_now_add=True)
    updated = models.DateTimeField (auto_now=True)

