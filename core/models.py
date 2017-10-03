from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nombre_cliente = models.CharField('Nombre', max_length=100, blank=True)
    direccion_cliente = models.CharField('Dirección', max_length=100, blank=True)
    telefono_cliente = models.CharField('Telefono', max_length=100, blank=True)

    def __str__(self):
        return self.nombre_cliente

class Vehiculo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    matricula = models.CharField('Matricula del Vehiculo', blank=True, max_length=20)
    modelo_vehiculo = models.CharField('Modelo del Vehiculo', max_length=100, blank=True)
    color_vehiculo = models.CharField('Color del Vehiculo', max_length=100, blank=True)
    fecha_entrada_vehiculo = models.DateTimeField('Fecha de Entrada del Vehiculo', auto_now_add=True, blank=True)
    cliente_vehiculo = models.ForeignKey(Cliente, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.matricula

class Mecanico_Responsable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nombre_mecanico = models.CharField('Nombre del Mecanico Responsable', max_length=100, blank=True)
    direccion_mecanico = models.CharField('Dirección del Mecanico Responsable', max_length=100, blank=True)
    telefono_mecanico = models.CharField('Telefono Mecanico Responsable', max_length=100, blank=True)
    cost_x_hora = models.DecimalField('Costo Por Hora', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre_mecanico


class Responsable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    vehiculo = models.ManyToManyField(Vehiculo, blank=True)
    mecanico = models.ManyToManyField(Mecanico_Responsable, blank=True)

    def __str__(self):
        return self.user.username

class HojaParte(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    concepto = models.CharField('Concepto', max_length=100, blank=True)
    cantidad = models.DecimalField('Cantidad', max_digits=5, decimal_places=2)
    reparacion = models.CharField('Reparación', max_length=100, blank=True)
    mecanico = models.ForeignKey(Mecanico_Responsable, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.concepto

class Repuesto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nombre_repuesto = models.CharField('Nombre del Repuesto', blank=True, max_length=100)
    descripcion = models.CharField('Descripción de la Refacción', blank=True, max_length=100)
    costo_unitario = models.DecimalField('Costo Unitario de la Refacción', max_digits=5, decimal_places=2)
    precio_unitario = models.DecimalField('Costo Unitario de la Refacción', max_digits=5, decimal_places=2)
    importe_parcial = models.DecimalField('Importe', max_digits=5, decimal_places=2)
    hoja_parte = models.ManyToManyField(HojaParte, blank=True)

    def __str__(self):
        return self.nombre_repuesto

class Factura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    RFC = models.CharField('RFC del Cliente', max_length=25, blank=True)
    importe_pesos = models.DecimalField('Importe en Pesos (MXN)', max_digits=5, decimal_places=2)
    importe_dolares = models.DecimalField('Importe en Dolares (USD)', max_digits=5, decimal_places=2)
    hoja_parte = models.ForeignKey(HojaParte, blank=True, on_delete=models.CASCADE)
