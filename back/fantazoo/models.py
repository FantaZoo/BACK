import djongo
from djongo import models
import enum

# Create your models here.

class User(models.Model):
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    
    

  
class Animal(models.Model):
    
    SEXE =[('M','Mâle'),('F','Femelle'),('ND','Non défini')]
    STATUT=[('A VENDRE','A VENDRE'),('VENDU','VENDU')]
    TYPE=[('REPTILE','REPTILE'),('MAMMIFERE','MAMMIFERE'),('POISSON','POISSON'),('INSECTE','INSECTE'),('ARACHNIDE','ARACHNIDE'),('OISEAU','OISEAU'),('ND','Non défini')]
    DIET=[('OMNIVORE','OMNIVORE'),('HERBIVORE','HERBIVORE'),('CARNIVORE','CARNIVORE'),('ND','Non défini')]
    animal_name = models.CharField(max_length=50,default='ND')
    description = models.CharField(max_length=200)
    price=models.FloatField(null=False, default=0)
    animal_status=models.CharField(max_length=20,default='EN STOCK',choices=STATUT)
    species=models.CharField(max_length=200,default='ND')
    sexe=models.CharField(max_length=20,choices=SEXE,default='ND')
    age = models.IntegerField()
    animal_type = models.CharField(max_length=50,choices=TYPE,default='ND')
    image = models.CharField(max_length=200)
    diet = models.CharField(max_length=200,choices=DIET,default='ND')

class ShoppingCart(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    productID = models.ForeignKey(Animal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
   

class Order(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price =models.FloatField(null=False, default=0)
    total_quantity=models.IntegerField(null=False, default=0)
    
   
    
