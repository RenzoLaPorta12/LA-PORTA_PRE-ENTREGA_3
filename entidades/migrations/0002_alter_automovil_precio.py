# Generated by Django 5.0.6 on 2024-07-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovil',
            name='precio',
            field=models.CharField(max_length=50),
        ),
    ]
