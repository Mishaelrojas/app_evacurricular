# Generated by Django 5.0 on 2024-04-05 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appevaluacion', '0023_unidad_postulante_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulante',
            name='doctorado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postulantes_doctorado', to='appevaluacion.doctorado'),
        ),
        migrations.AlterField(
            model_name='postulante',
            name='maestria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postulantes_maestria', to='appevaluacion.maestria'),
        ),
    ]