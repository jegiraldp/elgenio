# Generated by Django 2.1.3 on 2018-12-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_servicio_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='Comentario',
            field=models.CharField(default='--', max_length=100),
        ),
    ]
