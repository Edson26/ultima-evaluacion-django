# Generated by Django 4.0.1 on 2022-12-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario', '0004_inscritos_estado_inscritos_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscritos',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
