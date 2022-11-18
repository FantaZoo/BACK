from rest_framework.serializers import ModelSerializer
from .models import Animal

class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['Animalstatus'] = 'EN STOCK'
        instance= Animal.objects.create(**validated_data)
        instance.save()
        return instance
    