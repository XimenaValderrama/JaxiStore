from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")

def factura(request):
    return render(request, "factura.html")