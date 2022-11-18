import djongo
from djongo import models
import enum

# Create your models here.

class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    class Meta:
        abstract = True
################################################################################

class Customer(User):
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

################################################################################

class Admin(User):
   """  def """

################################################################################
  
class Animal(models.Model):
    SEXE =[('M','Mâle'),('F','Femelle'),('ND','Non défini')]
    SPECIES=[('Phoenix','Phoenix'),('Dragon','Dragon'),('Unicorn','Unicorn'),('Griffin','Griffin'),('Hippogriff','Hippogriff'),('Pegasus','Pegasus'),('Chimera','Chimera'),('Basilisk','Basilisk'),('Gorgon','Gorgon'),('ND','Non défini')]
    STATUT=[('A VENDRE','A VENDRE'),('VENDU','VENDU'),('EN STOCK','EN STOCK')]
    TYPE=[('REPTILE','REPTILE'),('MAMMIFERE','MAMMIFERE'),('POISSON','POISSON'),('INSECTE','INSECTE'),('ARACHNIDE','ARACHNIDE'),('ND','Non défini')]
    DIET=[('OMNIVORE','OMNIVORE'),('HERBIVORE','HERBIVORE'),('CARNIVORE','CARNIVORE'),('AUTRE','AUTRE'),('ND','Non défini')]
    description = models.CharField(max_length=200)
    price=models.FloatField(null=False, default=0)
    animal_status=models.CharField(max_length=20,default='EN STOCK',choices=STATUT)
    species=models.CharField(max_length=20,choices=SPECIES,default='ND')
    sexe=models.CharField(max_length=20,choices=SEXE,default='ND')
    age = models.IntegerField()
    animal_type = models.CharField(max_length=50,choices=TYPE,default='ND')
    image = models.CharField(max_length=200)
    diet = models.CharField(max_length=200,choices=DIET,default='ND')

class ShoppingCart(models.Model):
    userID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Animal, on_delete=models.CASCADE)
    product_quantity = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(Animal.price)
    total = models.FloatField()
    def __str__(self):
        return self.Animal.description


class Order(models.Model):
    userID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address=models.CharField(Customer.address,max_length=50)
    product = models.ForeignKey(Animal, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    total_price = models.FloatField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Animal.description
    
""" class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Animal,on_delete=models.CASCADE)
    price = models.FloatField(null=False,default=0.0)
    quantity = models.IntegerField(null=False,default=0)
    
    def __str__(self):
        return '{}{}'.format(self.order.id) """