from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    return render(request, "index.html")

@login_required(login_url="login")
def factura(request):
    
    return render(request, "factura.html")