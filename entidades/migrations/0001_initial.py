# Generated by Django 5.0.6 on 2024-06-30 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca del auto')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo del auto')),
                ('año', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Precio')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_usuario', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.CharField(choices=[('uno', '1'), ('dos', '2'), ('tres', '3'), ('cuatro', '4'), ('cinco', '5')], max_length=6)),
                ('contenido', models.TextField()),
                ('automovil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.automovil')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(max_length=50)),
                ('automovil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.automovil')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='automovil',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.vendedor'),
        ),
    ]