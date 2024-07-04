# Generated by Django 5.0.6 on 2024-07-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_ordencompra_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='estado',
            field=models.CharField(choices=[('Creada', 'Creada'), ('Rectificada', 'Rectificada')], default='Creada', max_length=20),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='estado_entrega',
            field=models.CharField(choices=[('Por entregar', 'Por Entregar'), ('Entregada', 'Entregada'), ('Rechazada', 'Rechazada')], default='Por entregar', max_length=20),
        ),
    ]