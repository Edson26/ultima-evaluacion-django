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
    hora = models.TimeField(auto_now_add=True)
    institucion = models.ForeignKey(
        Institucion, blank=True, on_delete=models.CASCADE)
    RESERVADO = 'Reservado'
    COMPLETADA = 'Completada'
    ANULADA = 'Anulada'
    NO_ASISTE = 'No Asiste'

    ESTADO_CHOICES = [
        (RESERVADO, 'Reservado'),
        (COMPLETADA, 'Completada'),
        (ANULADA, 'Anulada'),
        (NO_ASISTE, 'No asiste')
    ]
    estado = models.CharField(
        max_length=30, choices=ESTADO_CHOICES, default=RESERVADO)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.institucion
