# Generated by Django 5.0.2 on 2024-02-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
