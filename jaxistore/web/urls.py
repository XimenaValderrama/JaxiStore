from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('export_order/<int:order_id>/', export_order, name='export_order'),
    path('entrega_factura/<int:order_id>/', entrega_factura, name='entrega_factura'),
    path('rechazar_entrega/<int:order_id>/', rechazar_entrega, name='rechazar_entrega'),
    path('aceptar_entrega/<int:order_id>/', aceptar_entrega, name='aceptar_entrega'),   
    path('anular_factura/<int:factura_id>/', anular_factura, name='anular_factura'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
