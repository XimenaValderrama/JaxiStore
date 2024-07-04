from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class OrdenCompra(models.Model):

    class EstadosFactura(models.TextChoices):
        CREADA = "CR", _("Creada")
        RECTIFICADA = "RE", _("Rectificada")

    class EstadosEntrega(models.TextChoices):
        POR_ENTREGAR = "PE", _("Por entregar")
        ENTREGADA = "EN", _("Entregada")
        RECHAZADA = "RE", _("Rechazada")

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
    productos = models.ManyToManyField('Producto')

    estado = models.CharField(max_length=20, choices=EstadosFactura, default=EstadosFactura.CREADA)
    estado_entrega = models.CharField(max_length=20, choices=EstadosEntrega, default=EstadosEntrega.POR_ENTREGAR)

    direccion_entrega = models.CharField(max_length=100, blank=True, null=True)
    rut_persona_recibe = models.CharField(max_length=100, blank=True, null=True)
    imagen_entrega = models.ImageField(upload_to='entregas/', blank=True, null=True)
    motivo_rechazo = models.TextField(blank=True, null=True)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    precio_total = models.IntegerField()

    def __str__(self):
        return self.nombre
