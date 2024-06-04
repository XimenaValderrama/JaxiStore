# Generated by Django 5.0.6 on 2024-06-04 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orden_compra',
            fields=[
                ('id_orden_compra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('cuit_proveedor', models.CharField(max_length=100)),
                ('direccion_proveedor', models.CharField(max_length=100)),
                ('telefono_proveedor', models.CharField(max_length=100)),
                ('correo_proveedor', models.CharField(max_length=100)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('cuit_cliente', models.CharField(max_length=100)),
                ('direccion_cliente', models.CharField(max_length=100)),
                ('telefono_cliente', models.CharField(max_length=100)),
                ('correo_cliente', models.CharField(max_length=100)),
                ('rut_transporte', models.CharField(max_length=100)),
                ('patente', models.CharField(max_length=100)),
                ('rut_chofer', models.CharField(max_length=100)),
                ('nombre_chofer', models.CharField(max_length=100)),
                ('total_pedido', models.IntegerField()),
                ('total_iva', models.IntegerField()),
                ('total_pagar', models.IntegerField()),
                ('forma_pago', models.CharField(max_length=100)),
                ('fecha_entrega', models.DateField()),
            ],
        ),
    ]
