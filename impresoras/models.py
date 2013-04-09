from django.db import models
import datetime
# Create your models here.
# Datos Base de impresora
class Impresora(models.Model):
	serialn = models.CharField(max_length=100, null= True)
	marca= models.ForeignKey(MarcaModelo)
	tipo_conexion= models.ForeignKey(Conexion)
	tipo_impre = models.ForeignKey(Tipo_impresion)
	estado = models.CharField(Estado)
	fecha_ingreso = models.DateField()
# ------------------------------------

# marca de la impresora
class MarcaModelo(models.Model):
	marca = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)	
	
# ------------------------------------

# datos de la conexion usb-wifi-red-otro
class Conexion(models.Model):
	tipo_conexion = models.CharField(max_length=100)
# ------------------------------------

# tipo de impresion laser, inkjet etc
class Tipo_impresion(models.Model):
	tipo_impre = models.CharField(max_length=100)
# ------------------------------------
# Estado de trabajo buena mala inactiva
class Estado(models.Model):
	estado = models.CharField(max_length=100)

