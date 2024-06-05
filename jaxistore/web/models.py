from django.db import models

# Create your models here.

class orden_compra(models.Model):
    id_orden_compra = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    nombre_proveedor = models.CharField(max_length=100)
    cuit_proveedor = models.CharField(max_length=100)
    direccion_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.CharField(max_length=100)
    correo_proveedor = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=100)
    cuit_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=100)
    correo_cliente = models.CharField(max_length=100)
    rut_transporte = models.CharField(max_length=100)
    patente = models.CharField(max_length=100)
    rut_chofer = models.CharField(max_length=100)
    nombre_chofer = models.CharField(max_length=100)
    total_pedido = models.IntegerField()
    total_iva = models.IntegerField()
    total_pagar = models.IntegerField()
    forma_pago = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    productos = models.ManyToManyField('producto')

class producto (models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    precio_total = models.IntegerField()
