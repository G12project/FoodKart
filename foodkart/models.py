from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	is_customer = models.BooleanField(default=False)
	is_restaurant = models.BooleanField(default=False)
	is_delivery = models.BooleanField(default=False)

class Restaurant(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	reg_num=models.CharField(max_length=200)
	res_name=models.CharField(max_length=200)
	owner=models.CharField(max_length=60)
	mobile=models.IntegerField()
	latitude=models.DecimalField(max_digits=12, decimal_places=9)
	longitude=models.DecimalField(max_digits=12, decimal_places=9)
	Building=models.CharField(blank=True)
	Floor=models.IntegerField(null=True)
	City=models.CharField(max_length=100)
	State=models.CharField(max_length=100)
	Pin=models.IntegerField()

class Customer(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	cus_name=models.CharField(max_length=100)
	mobile=models.IntegerField()

class DeliveryExec(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	exec_name=models.CharField(max_length=100)
	mobile=models.IntegerField()
	avg_rating=models.IntegerField(default=0, null=True)
# Create your models here.
class Menu(models.Model):
    restaurant_id=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    food_name=models.CharField(max_legth=30)
    description=models.CharField(max_length=350)
    rating=models.IntegerField()
    food_image=models.ImageField(upload_to='images/')
    veg=models.BooleanField(default=True)
    price=models.IntegerField()
