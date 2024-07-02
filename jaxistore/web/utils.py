from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from .models import OrdenCompra

def export_order_to_pdf(order_id, filename):
    order = OrdenCompra.objects.get(id_orden_compra=order_id)
    productos = order.productos.all()

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    x_offset = 0.5 * inch
    y_offset = height - 1 * inch

    c.setFont("Helvetica", 12)
    c.drawString(x_offset, y_offset, f"ID: {order.id_orden_compra}")
    y_offset -= 0.5 * inch

    c.setFont("Helvetica-Bold", 24)
    c.drawString(x_offset, y_offset, "Orden de Compra")
    y_offset -= 0.5 * inch
    
    c.setFont("Helvetica", 12)
    c.drawString(x_offset, y_offset, f"Proveedor: {order.nombre_proveedor}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"CUIT: {order.cuit_proveedor}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Dirección: {order.direccion_proveedor}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Teléfono: {order.telefono_proveedor}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Correo: {order.correo_proveedor}")
    y_offset -= 0.5 * inch

    c.drawString(x_offset, y_offset, f"Cliente: {order.nombre_cliente}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"CUIT: {order.cuit_cliente}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Dirección: {order.direccion_cliente}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Teléfono: {order.telefono_cliente}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Correo: {order.correo_cliente}")
    y_offset -= 0.5 * inch

    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_offset, y_offset, "Detalles de la Orden de Compra")
    y_offset -= 0.3 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_offset, y_offset, "Producto")
    c.drawString(x_offset + 3 * inch, y_offset, "Cantidad")
    c.drawString(x_offset + 4 * inch, y_offset, "Precio Unitario")
    c.drawString(x_offset + 6 * inch, y_offset, "Precio Total")
    y_offset -= 0.2 * inch

    c.setFont("Helvetica", 12)
    for producto in productos:
        c.drawString(x_offset, y_offset, producto.nombre)
        c.drawString(x_offset + 3 * inch, y_offset, str(producto.cantidad))
        c.drawString(x_offset + 4 * inch, y_offset, f"${producto.precio:.2f}")
        c.drawString(x_offset + 6 * inch, y_offset, f"${producto.precio_total:.2f}")
        y_offset -= 0.2 * inch

    y_offset -= 0.5 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_offset, y_offset, f"Total Pedido: ${order.total_pedido:.2f}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Total IVA: ${order.total_iva:.2f}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Total a Pagar: ${order.total_pagar:.2f}")
    y_offset -= 0.5 * inch

    c.drawString(x_offset, y_offset, f"Forma de Pago: {order.forma_pago}")
    y_offset -= 0.2 * inch
    c.drawString(x_offset, y_offset, f"Fecha de Entrega: {order.fecha_entrega}")

    c.save()
