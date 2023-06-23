from django.db import models
from datetime import datetime

# Create your models here.
class Category_Db(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category')


class Car_Db(models.Model):

    car_name = models.CharField(max_length=100, null=True)
    car_category = models.CharField(max_length=100, null=True)
    car_brand = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)
    condition = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    car_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    body_style = models.CharField(max_length=100, null=True)
    engine = models.CharField(max_length=100, null=True)
    transmission = models.CharField(max_length=100, null=True)
    kilometers = models.IntegerField()
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50, null=True)
    no_of_owners = models.CharField(max_length=100, null=True)
    is_featured = models.BooleanField(default=False, null=True)
    is_approved = models.BooleanField(default=False, null=True)
    created_date = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.car_name
    