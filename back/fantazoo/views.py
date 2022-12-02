from django.shortcuts import render
from .models import Animal,User,ShoppingCart,Order,OrderItem
from .serializers import AnimalSerializer,UserSerializer,ShoppingCartSerializer,OrderSerializer,OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 

# Create your views here.

class AnimalAPIView(APIView):
    def get(self, *args,**kwargs):
        data = Animal.objects.all()
        serializer = AnimalSerializer(data, many=True)
        return Response(serializer.data)
    
class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    def get_queryset(self):
        return Animal.objects.all()
######## SHOPPING CART ########

    ###AJOUTER UN PRODUIT AU PANIER#####

class AddToCartAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ShoppingCartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    ###AFFICHER LE PANIER#####
    
    
class ShoppingCartAPIView(APIView):
    def get(self, *args,**kwargs):
        data = ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(data, many=True)
        return Response(serializer.data)
class ShoppingCartViewSet(ModelViewSet):
    serializer_class = ShoppingCartSerializer
    def get_queryset(self):
        return ShoppingCart.objects.all()
class UserAPIView(APIView):
    def get(self, *args,**kwargs):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
    
class OrderAPIView(APIView):
    def get(self, *args,**kwargs):
        data = Order.objects.all()
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.all()
    
class OrderItemAPIView(APIView):
    def get(self, *args,**kwargs):
        data = OrderItem.objects.all()
        serializer = OrderItemSerializer(data, many=True)
        return Response(serializer.data)

class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        return OrderItem.objects.all()
