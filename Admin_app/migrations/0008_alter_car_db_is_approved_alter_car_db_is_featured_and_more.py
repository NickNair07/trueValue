# Generated by Django 4.1.7 on 2023-06-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0007_car_db_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_db',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='is_featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='car_db',
            name='no_of_owners',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
