# Generated by Django 4.1.1 on 2022-10-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
