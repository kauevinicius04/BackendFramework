from django.db import models

# Create your models here.
class Modelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
