# Generated by Django 4.2.3 on 2023-10-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_collection_image_url_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image_url',
            field=models.CharField(max_length=255),
        ),
    ]
