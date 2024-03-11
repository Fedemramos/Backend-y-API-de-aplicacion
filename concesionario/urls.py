from django.urls import path, include
from rest_framework import routers
from .views import CarsList,DataCarsList, inicio
from .api import *


router = routers.DefaultRouter()
router.register(r"cars", CarView, "cars")
router.register(r"data", DataCarView, "data")
router.register(r"ficha", SpecifiCarView, "ficha")


urlpatterns = [
    path("api/", include(router.urls)),
    path('modelos/', CarsList.as_view(), name='car_list'),
    path('fichatecnica/', DataCarsList.as_view(), name='ficha_models'),
    path('inicio', inicio, name='inicio')
]
