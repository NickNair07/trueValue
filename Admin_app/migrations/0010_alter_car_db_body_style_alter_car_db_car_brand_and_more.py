# Generated by Django 4.1.7 on 2023-06-16 04:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0009_alter_car_db_body_style_alter_car_db_car_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_db',
            name='body_style',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='car_brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='car_category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='car_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='condition',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='engine',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='fuel_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='is_featured',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='no_of_owners',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='price',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='transmission',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='year',
            field=models.CharField(max_length=100, null=True),
        ),
    ]