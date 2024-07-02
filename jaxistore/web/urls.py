from django.urls import path
from .views import export_order

urlpatterns = [
    path('export_order/<int:order_id>/', export_order, name='export_order'),
]
