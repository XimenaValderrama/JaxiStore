from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from .models import *
from django.http import HttpResponse
from .utils import export_order_to_pdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pdfkit
from django.db.models import Count
from jinja2 import Environment, FileSystemLoader
# Create your views here.

def inicio_sesion(request):
    
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        contrasena = request.POST.get("password")
        user = authenticate(request, username=usuario, password=contrasena)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirigir a la página principal u otra página después de iniciar sesión
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')

@login_required(login_url="login")
def cerrar_sesion(request):
    logout(request)
    return redirect('login') 

@login_required(login_url="login")
def index(request):

    facturas = OrdenCompra.objects.all()

    facturas_creadas = OrdenCompra.objects.filter(estado="CR").count()
    facturas_rectificadas = OrdenCompra.objects.filter(estado="RE").count()
    facturas_anuladas = OrdenCompra.objects.filter(estado="AN").count()
    facturas_por_entregar = OrdenCompra.objects.filter(estado_entrega="PE").count()
    facturas_entregadas = OrdenCompra.objects.filter(estado_entrega="EN").count()
    facturas_rechazadas = OrdenCompra.objects.filter(estado_entrega="RE").count()

    contexto = {
        "facturas": facturas,
        "facturas_creadas" : facturas_creadas,
        "facturas_rectificadas" : facturas_rectificadas,
        "facturas_anuladas" : facturas_anuladas,
        "facturas_por_entregar" : facturas_por_entregar,
        "facturas_entregadas" : facturas_entregadas,
        "facturas_rechazadas" : facturas_rechazadas,
        }

    return render(request, "index.html", contexto)

@login_required(login_url="login")
def factura(request):
    if request.method == "POST":
        nombre_proveedor = request.POST.get('nombre_proveedor')
        cuit_proveedor = request.POST.get('cuit_proveedor')
        direccion_proveedor = request.POST.get('direccion_proveedor')
        telefono_proveedor = request.POST.get('telefono_proveedor')
        correo_proveedor = request.POST.get('correo_proveedor')
        nombre_cliente = request.POST.get('nombre_cliente')
        cuit_cliente = request.POST.get('cuit_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        correo_cliente = request.POST.get('correo_cliente')
        rut_transporte = request.POST.get('rut_transporte')
        patente = request.POST.get('patente')
        rut_chofer = request.POST.get('rut_chofer')
        nombre_chofer = request.POST.get('nombre_chofer')
        total_pedido = float(request.POST.get('total_pedido').replace('$', '').replace(',', ''))
        total_iva = float(request.POST.get('iva').replace('$', '').replace(',', ''))
        total_pagar = float(request.POST.get('total_pagar').replace('$', '').replace(',', ''))
        forma_pago = request.POST.get('forma_pago')
        fecha_entrega = request.POST.get('fecha_entrega')

        nueva_orden = OrdenCompra(
            nombre_proveedor=nombre_proveedor,
            cuit_proveedor=cuit_proveedor,
            direccion_proveedor=direccion_proveedor,
            telefono_proveedor=telefono_proveedor,
            correo_proveedor=correo_proveedor,
            nombre_cliente=nombre_cliente,
            cuit_cliente=cuit_cliente,
            direccion_cliente=direccion_cliente,
            telefono_cliente=telefono_cliente,
            correo_cliente=correo_cliente,
            rut_transporte=rut_transporte,
            patente=patente,
            rut_chofer=rut_chofer,
            nombre_chofer=nombre_chofer,
            total_pedido=total_pedido,
            total_iva=total_iva,
            total_pagar=total_pagar,
            forma_pago=forma_pago,
            fecha_entrega=fecha_entrega
        )
        nueva_orden.save()

        # Procesar los productos
        productos = request.POST.getlist('producto[]')
        cantidades = request.POST.getlist('cantidad[]')
        precios = request.POST.getlist('precio[]')
        totales = request.POST.getlist('total[]')

        for producto_nombre, cantidad, precio, total in zip(productos, cantidades, precios, totales):
            nuevo_producto = Producto(
                nombre=producto_nombre,
                cantidad=cantidad,
                precio=precio,
                precio_total=total.replace('$', '').replace(',', '')
            )
            nuevo_producto.save()
            nueva_orden.productos.add(nuevo_producto)


        return render(request, "factura.html", {"mensaje_factura_creada": True})
    
    else:
        return render(request, "factura.html")

@login_required(login_url="login")
def verfactura(request, id):
    try:
        factura = OrdenCompra.objects.get(id_orden_compra=id)
        productos = factura.productos.all()

        print(factura.estado_entrega)

    except OrdenCompra.DoesNotExist:
        raise Http404("Factura no encontrada")
    return render(request, "verfactura.html", {'factura': factura, 'productos': productos})

@login_required(login_url="login")
def export_order(request, order_id):
    filename = f"web/facturas/orden_compra_{order_id}.pdf"
    export_order_to_pdf(order_id, filename)

    with open(filename, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response

@login_required(login_url="login")
def rectificar_factura(request, order_id):

    factura = OrdenCompra.objects.filter(id_orden_compra=order_id)
    if factura.count() > 0:
        factura =  OrdenCompra.objects.get(id_orden_compra=order_id)

    #Modificar factura
    if request.method == "POST":    
        nombre_proveedor = request.POST.get('nombre_proveedor')
        cuit_proveedor = request.POST.get('cuit_proveedor')
        direccion_proveedor = request.POST.get('direccion_proveedor')
        telefono_proveedor = request.POST.get('telefono_proveedor')
        correo_proveedor = request.POST.get('correo_proveedor')
        nombre_cliente = request.POST.get('nombre_cliente')
        cuit_cliente = request.POST.get('cuit_cliente')
        direccion_cliente = request.POST.get('direccion_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        correo_cliente = request.POST.get('correo_cliente')
        rut_transporte = request.POST.get('rut_transporte')
        patente = request.POST.get('patente')
        rut_chofer = request.POST.get('rut_chofer')
        nombre_chofer = request.POST.get('nombre_chofer')
        total_pedido = float(request.POST.get('total_pedido').replace('$', '').replace(',', ''))
        total_iva = float(request.POST.get('iva').replace('$', '').replace(',', ''))
        total_pagar = float(request.POST.get('total_pagar').replace('$', '').replace(',', ''))
        forma_pago = request.POST.get('forma_pago')
        fecha_entrega = request.POST.get('fecha_entrega')

        factura.nombre_proveedor = nombre_proveedor
        factura.cuit_proveedor=cuit_proveedor
        factura.direccion_proveedor=direccion_proveedor
        factura.telefono_proveedor=telefono_proveedor
        factura.correo_proveedor=correo_proveedor
        factura.nombre_cliente=nombre_cliente
        factura.cuit_cliente=cuit_cliente
        factura.direccion_cliente=direccion_cliente
        factura.telefono_cliente=telefono_cliente
        factura.correo_cliente=correo_cliente
        factura.rut_transporte=rut_transporte
        factura.patente=patente
        factura.rut_chofer=rut_chofer
        factura.nombre_chofer=nombre_chofer
        factura.total_pedido=total_pedido
        factura.total_iva=total_iva
        factura.total_pagar=total_pagar
        factura.forma_pago=forma_pago
        factura.fecha_entrega=fecha_entrega
        factura.estado = "Rectificada"
        
        factura.save()



        # Procesar los productos
        factura.productos.all().delete()

        productos = request.POST.getlist('producto[]')
        cantidades = request.POST.getlist('cantidad[]')
        precios = request.POST.getlist('precio[]')
        totales = request.POST.getlist('total[]')

        for producto_nombre, cantidad, precio, total in zip(productos, cantidades, precios, totales):
            nuevo_producto = Producto(
                nombre=producto_nombre,
                cantidad=cantidad,
                precio=precio,
                precio_total=total.replace('$', '').replace(',', '')
            )
            nuevo_producto.save()
            factura.productos.add(nuevo_producto)

        return redirect("index")

    contexto = {
        'factura': factura
    }

    return render(request, "rectificar_factura.html", contexto)

@login_required(login_url="login")
def entrega_factura(request, order_id):
    
    factura = OrdenCompra.objects.filter(id_orden_compra=order_id)
    if factura.count() > 0:
        factura =  OrdenCompra.objects.get(id_orden_compra=order_id)

        if factura.estado_entrega != factura.EstadosEntrega.ENTREGADA:

            contexto = {
                'factura': factura
            }
            return render(request, "entrega_factura.html", contexto)

        return redirect("index")

    else:
        return redirect("index")
    
@login_required(login_url="login")
def rechazar_entrega(request, order_id):

    if request.method == "POST":
        motivo_rechazo = request.POST.get('motivo_rechazo')

        factura = OrdenCompra.objects.filter(id_orden_compra=order_id)
        

        if factura.count() > 0:
            factura =  OrdenCompra.objects.get(id_orden_compra=order_id)
            factura.estado_entrega = factura.EstadosEntrega.RECHAZADA
            factura.motivo_rechazo = motivo_rechazo
            factura.save()
            return render(request, "rechazar_entrega.html", {"mensaje_factura_rechazada": True})

    else:
        factura = OrdenCompra.objects.filter(id_orden_compra=order_id)
        if factura.count() > 0:
            factura =  OrdenCompra.objects.get(id_orden_compra=order_id)

            if factura.estado_entrega == factura.EstadosEntrega.ENTREGADA:
                return redirect("index")
        
            return render(request, "rechazar_entrega.html")
        
        else:
            return redirect("index")

@login_required(login_url="login")
def aceptar_entrega(request, order_id):
    
    if request.method == "POST":

        direccion_entrega = request.POST.get('direccion_entrega')
        rut_persona_recibe = request.POST.get('rut_recibe')
        imagen_entrega = request.FILES.get('imagen_entrega')

        factura = OrdenCompra.objects.filter(id_orden_compra=order_id)
        if factura.count() > 0:

            factura =  OrdenCompra.objects.get(id_orden_compra=order_id)
            if factura.estado_entrega == factura.EstadosEntrega.ENTREGADA:
                return redirect("index")


            factura.estado_entrega = factura.EstadosEntrega.ENTREGADA
            factura.direccion_entrega = direccion_entrega
            factura.rut_persona_recibe = rut_persona_recibe
            factura.imagen_entrega = imagen_entrega
            factura.save()
            return render(request, "aceptar_entrega.html", {"mensaje_factura_entregada": True})

    else:
        factura = OrdenCompra.objects.filter(id_orden_compra=order_id)
        if factura.count() > 0:
            factura =  OrdenCompra.objects.get(id_orden_compra=order_id)
            if factura.estado_entrega == factura.EstadosEntrega.ENTREGADA:
                return redirect("index")
            
            return render(request, "aceptar_entrega.html")
        
        else:
            return redirect("index")

@login_required(login_url="login")           
def anular_factura(request, factura_id):
    factura = get_object_or_404(OrdenCompra, id_orden_compra=factura_id)
    if factura.estado != OrdenCompra.EstadosFactura.ANULADA:
        factura.estado = OrdenCompra.EstadosFactura.ANULADA
        factura.save()
        return redirect("index")
    return redirect("index")

