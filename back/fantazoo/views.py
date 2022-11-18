from django.shortcuts import render
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 

# Create your views here.
class AnimalAPIView(APIView):
    def get(self, *args,**kwargs):
        data = Animal.objects.all()
        serializer = AnimalSerializer(data, many=True)
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