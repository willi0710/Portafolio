# Generated by Django 4.2.10 on 2024-02-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_alter_proyecto_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion web'),
        ),
    ]
