from django.db import models

# Create your models here.
class Producto(models.Model):
    # Tipo 1: CharField (Cadenas de texto cortas)
    nombre = models.CharField(max_length=100)
    codigo_barras = models.CharField(max_length=50, unique=True)

    # Tipo 2: TextField (Cadenas de texto largas / descripciones)
    descripcion = models.TextField(blank=True, null=True)

    # Tipo 3: IntegerField (Números enteros)
    precio = models.IntegerField()  # Guardado en centavos o unidades enteras
    stock = models.IntegerField(default=0)

    # Tipo 4: DateTimeField (Fechas y horas)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre