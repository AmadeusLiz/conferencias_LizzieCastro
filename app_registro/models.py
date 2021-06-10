from django.db import models
from django.db.models.enums import Choices

class Conferencista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    experiencia = models.TextField()
    
    def __str__(self):
        return self.nombre


class Conferencia(models.Model):
    ESTADOS = (
        ('1', 'Pendiente'), #BD, INTERFAZ GRAFICA
        ('2', 'En Proceso'), 
        ('3', 'Finalizada'), 
        ('4', 'Cancelada'), 
    )

    nombre = models.CharField( max_length=35 )
    fecha_registro = models.DateTimeField(auto_now_add=True) #agregar fechas de ese momento automaticamente
    fecha = models.DateField()
    hora = models.TimeField()
    conferencista = models.ManyToManyField(Conferencista, blank=True) #MtM no llevan on delete y el nulo no aplica
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')
    cupos = models.SmallIntegerField(default=10)

    def __str__(self):
        return 'Conferencia: {self.nombre}'

class Participante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    twitter = models.CharField(max_length=35, null=True, blank=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Asistencia(models.Model):
    conferencia = models.ForeignKey(Conferencia, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    confirmacion = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.conferencia} | {self.participante}'

    class Meta:
        unique_together = ('conferencia', 'participante')    