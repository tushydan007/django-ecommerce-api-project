# Generated by Django 4.2.3 on 2023-10-02 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_productreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='reviewer_name',
            new_name='customer_name',
        ),
    ]
