# Generated by Django 4.1.7 on 2023-06-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0006_car_db_car_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_db',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]