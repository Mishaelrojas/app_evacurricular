# Generated by Django 5.0 on 2024-03-29 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appevaluacion', '0010_alter_evaluacion_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2024, 3, 29, 11, 54, 50, 478276)),
        ),
    ]