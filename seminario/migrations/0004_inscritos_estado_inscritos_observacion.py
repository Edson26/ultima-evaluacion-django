# Generated by Django 4.0.1 on 2022-12-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario', '0003_alter_inscritos_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscritos',
            name='estado',
            field=models.CharField(choices=[('Reservado', 'Reservado'), ('Completada', 'Completada'), ('Anulada', 'Anulada'), ('No Asiste', 'No asiste')], default='Reservado', max_length=30),
        ),
        migrations.AddField(
            model_name='inscritos',
            name='observacion',
            field=models.TextField(null=True),
        ),
    ]
