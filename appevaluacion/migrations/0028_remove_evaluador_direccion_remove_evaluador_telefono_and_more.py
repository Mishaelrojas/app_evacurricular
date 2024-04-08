# Generated by Django 5.0 on 2024-04-07 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appevaluacion', '0027_postulante_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluador',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='evaluador',
            name='telefono',
        ),
        migrations.AddField(
            model_name='evaluador',
            name='cargo',
            field=models.CharField(choices=[('Presidente', 'Presidente'), ('Secretario', 'Secretario'), ('Vocal', 'Vocal')], default='Presidente', max_length=20),
        ),
        migrations.AddField(
            model_name='evaluador',
            name='unidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appevaluacion.unidad'),
        ),
        migrations.AlterField(
            model_name='evaluador',
            name='dni',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluador',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
    ]
