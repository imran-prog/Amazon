# Generated by Django 3.1.3 on 2020-11-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0017_product_delievery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warrenty_support',
            field=models.TextField(default=''),
        ),
    ]