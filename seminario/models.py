from django.db import models
# Create your models here.


class Institucion(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre


class Inscritos(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    hora = models.DateTimeField(auto_now_add=True)
    institucion = models.ForeignKey(
        Institucion, blank=True, on_delete=models.CASCADE)
