from django.contrib import admin
from .models import Car, Datacar, Specifications
# Register your models here.from 

class Caradmin(admin.ModelAdmin):
    list_display = ('model','segment','year','price')
    search_fields = ('model','year','price')

admin.site.register(Car,Caradmin)


class Datadmin(admin.ModelAdmin):
    list_display = ('data_car', 'description')
    

admin.site.register(Datacar,Datadmin)


class Specificdmin(admin.ModelAdmin):
    list_display = ('car_specifications','car')
   

admin.site.register(Specifications,Specificdmin)
