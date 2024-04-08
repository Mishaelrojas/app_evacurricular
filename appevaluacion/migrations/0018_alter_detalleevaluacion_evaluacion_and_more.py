# Generated by Django 5.0 on 2024-04-03 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appevaluacion', '0017_evaluacion_estado_evaluacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleevaluacion',
            name='evaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appevaluacion.evaluacion', unique=True),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='estado_evaluacion',
            field=models.CharField(default='No Evaluado', max_length=12, null=True),
        ),
    ]