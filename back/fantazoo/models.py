import djongo
from djongo import models
import enum

# Create your models here.

    
class Animal(models.Model):
    SEXE =[('M','Mâle'),('F','Femelle'),('ND','Non défini')]
    SPECIES=[('Phoenix','Phoenix'),('Dragon','Dragon'),('Unicorn','Unicorn'),('Griffin','Griffin'),('Hippogriff','Hippogriff'),('Pegasus','Pegasus'),('Chimera','Chimera'),('Basilisk','Basilisk'),('Gorgon','Gorgon'),('ND','Non défini')]
    STATUT=[('A VENDRE','A VENDRE'),('VENDU','VENDU'),('EN STOCK','EN STOCK')]
    description = models.CharField(max_length=200)
    price=models.FloatField()
    status=models.CharField(max_length=20,default='EN STOCK',choices=STATUT)
    species=models.CharField(max_length=20,choices=SPECIES,default='ND')
    sexe=models.CharField(max_length=20,choices=SEXE,default='ND')
    age = models.IntegerField()
    type = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    diet = models.CharField(max_length=200)