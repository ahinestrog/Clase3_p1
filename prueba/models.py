from django.db import models

# Create your models here.

class Prueba(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=550)
    image = models.ImageField(upload_to='prueba/images/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title