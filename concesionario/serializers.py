from rest_framework import serializers
from .models import Car, Datacar, Specifications

class DatacarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datacar
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class SpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specifications
        fields = '__all__'

