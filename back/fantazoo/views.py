from django.shortcuts import render
from .models import Animal,Admin,Customer,ShoppingCart,Order,OrderItem
from .serializers import AnimalSerializer,AdminSerializer,CustomerSerializer,ShoppingCartSerializer,OrderSerializer,OrderItemSerializer
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

class AdminAPIView(APIView):
    def get(self, *args,**kwargs):
        data = Admin.objects.all()
        serializer = AdminSerializer(data, many=True)
        return Response(serializer.data)
class AdminViewSet(ModelViewSet):
    serializer_class = AdminSerializer
    def get_queryset(self):
        return Admin.objects.all()
    
class CustomerAPIView(APIView):
    def get(self, *args,**kwargs):
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response(serializer.data)
class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    def get_queryset(self):
        return Customer.objects.all()
class OrderAPIView(APIView):
    def get(self, *args,**kwargs):
        data = Order.objects.all()
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)
    
class OrderItemAPIView(APIView):
    def get(self, *args,**kwargs):
        data = OrderItem.objects.all()
        serializer = OrderItemSerializer(data, many=True)
        return Response(serializer.data)



""" 
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
 """