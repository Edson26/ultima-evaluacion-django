from django.db import models
# Create your models here.

class Intituto(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    nombre = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.nombre

class Inscritos(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    nombre = models.CharField(max_length=30)
    telefono = models.DecimalField(max_digits=10)
    fecha = models.DateField(add_auto_now=True)
    institucion = models.ForeignKey()