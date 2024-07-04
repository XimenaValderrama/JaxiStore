from django.urls import path
from .views import *

urlpatterns = [
    path('export_order/<int:order_id>/', export_order, name='export_order'),
    path('entrega_factura/<int:order_id>/', entrega_factura, name='entrega_factura'),
    path('rechazar_entrega/<int:order_id>/', rechazar_entrega, name='rechazar_entrega'),
    path('aceptar_entrega/<int:order_id>/', aceptar_entrega, name='aceptar_entrega'),
]
