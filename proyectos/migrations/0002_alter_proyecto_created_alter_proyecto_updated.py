# Generated by Django 4.2.10 on 2024-02-22 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creacion'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualizacion'),
        ),
    ]
