# Generated by Django 5.0.6 on 2024-07-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_ordencompra_motivo_rechazo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='direccion_entrega',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
