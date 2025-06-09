from django.db import models
from django.utils import timezone

# Create your models here.

class ONG(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
      return self.nombre

class Donante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
      return self.nombre

class Campaña(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    meta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __str__(self):
      return self.nombre

class Donacion(models.Model):
    donante = models.ForeignKey(Donante, on_delete=models.CASCADE)
    campaña = models.ForeignKey(Campaña, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
      return f"{self.donante.nombre} donó {self.monto} Bs"
