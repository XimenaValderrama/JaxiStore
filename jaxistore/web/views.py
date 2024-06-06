from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


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
    return render(request, "index.html", {"facturas": facturas})

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

        return redirect('factura')  # Redirige a la misma página o a otra página después de guardar
    else:
        return render(request, "factura.html")
