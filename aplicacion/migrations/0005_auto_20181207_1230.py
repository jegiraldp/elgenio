# Generated by Django 2.1.3 on 2018-12-07 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_auto_20181207_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]