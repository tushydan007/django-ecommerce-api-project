# Generated by Django 4.2.2 on 2023-07-08 13:20

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='store/media', validators=[store.validators.validate_file_size]),
        ),
    ]