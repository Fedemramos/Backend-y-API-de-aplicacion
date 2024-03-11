from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=100)
    segment = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.model} {self.segment} {self.year} - ${self.price}"

# informacion del auto - caracteristicas unicas
class Datacar(models.Model):
    data_car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key = True)
    description = models.TextField()

    def __str__(self):
        return f"info car {self.data_car}"
    

#ficha tecnica - motor, transmicion - piezas en comun
class Specifications(models.Model):
    car_specifications = models.TextField()
    car = models.ForeignKey(Car,on_delete=models.CASCADE, related_name ='specs')

    def __str__(self):
        return self.car_specifications
    

class Cliente(models.Model):
    name= models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    direction = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone}"