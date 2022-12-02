from django.shortcuts import render
from .models import Animal,User,ShoppingCart,Order
from .serializers import AnimalSerializer,UserSerializer,ShoppingCartSerializer,OrderSerializer
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
        queryset = User.objects.all()
        email = self.request.GET.get('email', None)
        if email and email is not None:
            queryset = queryset.filter(email=email)
        return queryset
    
class OrderAPIView(APIView):
    def get(self, *args,**kwargs):
        data = Order.objects.all()
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.all()
    
