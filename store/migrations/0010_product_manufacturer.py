# Generated by Django 4.2.3 on 2023-10-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_in_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(default='Apple', max_length=255),
        ),
    ]