# Generated by Django 4.1.7 on 2023-05-24 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_brand', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('DL', 'Delhi'), ('MH', 'Maharashtra'), ('LA', 'Ladakh'), ('TS', 'Telangana')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('car_photo', models.ImageField(upload_to='photos')),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('kilometers', models.IntegerField()),
                ('milage', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]