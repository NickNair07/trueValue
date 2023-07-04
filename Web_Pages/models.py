from django.db import models
from Admin_app.models import Car_Db
from datetime import datetime


# Create your models here.
class UserDB(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    

class ContactDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    

class EnquiryDB(models.Model):
    car_id = models.CharField(max_length=10, null=True, blank=True)
    car_name = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=500, null=True, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)


class TestDriveDB(models.Model):
    car_id = models.CharField(max_length=10, null=True, blank=True)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    preferred_day =models.DateField(null=True, blank=True)
    preferred_time = models.CharField(max_length=20, null=True, blank=True)




