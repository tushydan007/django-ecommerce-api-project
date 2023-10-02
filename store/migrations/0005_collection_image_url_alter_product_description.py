# Generated by Django 4.2.3 on 2023-10-02 06:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='image_url',
            field=models.CharField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
