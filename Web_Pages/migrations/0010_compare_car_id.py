# Generated by Django 4.1.7 on 2023-06-20 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Pages', '0009_wishlist_compare'),
    ]

    operations = [
        migrations.AddField(
            model_name='compare',
            name='car_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
