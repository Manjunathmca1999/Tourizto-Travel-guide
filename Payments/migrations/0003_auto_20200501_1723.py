# Generated by Django 3.0.5 on 2020-05-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0002_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.IntegerField(),
        ),
    ]