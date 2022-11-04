import djongo
from djongo import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    age = models.IntegerField()
    type = models.CharField(max_length=50)
    image = models.CharField(max_length=200)