# Generated by Django 2.1.3 on 2018-12-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_remision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='Comentario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]