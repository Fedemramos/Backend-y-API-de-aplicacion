from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car, Datacar
from .serializers import CarSerializer

# Create your views here.

class CarsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'car_list.html'

    def get(self, request):
        ordering = request.query_params.get('ordering', None)
        queryset = Car.objects.all()

        if ordering == 'price_asc':
            queryset = queryset.order_by('price')
        elif ordering == 'price_desc':
            queryset = queryset.order_by('-price')
        elif ordering == 'year_asc':
            queryset = queryset.order_by('year')
        elif ordering == 'year_desc':
            queryset = queryset.order_by('-year')

        serializer = CarSerializer(queryset, many=True)
        
        return Response({'autos': serializer.data})

class DataCarsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ficha_models.html'
    
    def get(self, request):
        return Response({'informacion': Datacar.objects.all()})


def inicio(request):
   return render(request, "index.html")

