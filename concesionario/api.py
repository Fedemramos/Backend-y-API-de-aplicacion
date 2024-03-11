from rest_framework import viewsets, permissions, generics
from .models import Car, Datacar, Specifications
from .serializers import CarSerializer, DatacarSerializer, SpecificSerializer

# Create your views/api here.

class CarView(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DataCarView(viewsets.ModelViewSet):
    serializer_class =  DatacarSerializer
    queryset = Datacar.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SpecifiCarView(viewsets.ModelViewSet):
    serializer_class = SpecificSerializer
    queryset = Specifications.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
