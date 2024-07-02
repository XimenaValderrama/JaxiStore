from django.contrib import admin
from django.urls import path, include
from web.views import inicio_sesion, index, factura, cerrar_sesion, verfactura

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_sesion, name="login"),
    path('index/', index, name="index"),
    path('factura/', factura, name="factura"),
    path('cerrar-sesion', cerrar_sesion, name="cerrar_sesion"),
    path('verfactura/<int:id>/', verfactura, name="verfactura"),
    path('', include('web.urls')),  # Incluye las URLs de la aplicación 'web'
]
