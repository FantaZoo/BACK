from rest_framework.serializers import ModelSerializer
from .models import Animal,Admin,Customer,ShoppingCart,Order,OrderItem



class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class ShoppingCartSerializer(ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'
             
class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        
    """ def create(self, validated_data):
        validated_data['Animalstatus'] = 'EN STOCK'
        instance= Animal.objects.create(**validated_data)
        instance.save()
        return instance """

