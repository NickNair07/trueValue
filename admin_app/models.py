from django.db import models
from datetime import datetime

# Create your models here.
class Category_Db(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category')


class Car_Db(models.Model):

    car_name = models.CharField(max_length=100)
    car_category = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    car_photo = models.ImageField(upload_to='photos')
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    kilometers = models.IntegerField()
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.car_name
    

    