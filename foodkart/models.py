from django.db import models

# Create your models here.
class Menu(models.Model):
    restaurant_id=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    food_name=models.CharField(max_legth=30)
    description=models.CharField(max_length=350)
    rating=models.IntegerField()
    food_image=models.ImageField(upload_to='images/')
    veg=models.BooleanField(default=True)
    price=models.IntegerField()