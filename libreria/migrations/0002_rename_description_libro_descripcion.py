# Generated by Django 4.2.6 on 2023-10-06 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='description',
            new_name='descripcion',
        ),
    ]
