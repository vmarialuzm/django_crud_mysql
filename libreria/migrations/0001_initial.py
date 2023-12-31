# Generated by Django 4.2.6 on 2023-10-06 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
    ]
