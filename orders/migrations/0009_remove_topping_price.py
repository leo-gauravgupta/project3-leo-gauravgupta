# Generated by Django 2.0.4 on 2018-04-23 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_topping_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='price',
        ),
    ]