# Generated by Django 5.1.7 on 2025-07-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_obligacion_fecha_pago_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagoproveedor',
            name='obligacion',
        ),
        migrations.RemoveField(
            model_name='pagocliente',
            name='registro',
        ),
        migrations.AddField(
            model_name='registro',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización'),
        ),
        migrations.AddField(
            model_name='registro',
            name='obligaciones_data',
            field=models.JSONField(blank=True, default=list, help_text='Lista de obligaciones con proveedores', verbose_name='Datos de Obligaciones'),
        ),
        migrations.AddField(
            model_name='registro',
            name='pagos_cliente_data',
            field=models.JSONField(blank=True, default=list, help_text='Lista de pagos recibidos del cliente', verbose_name='Datos de Pagos Cliente'),
        ),
        migrations.AddField(
            model_name='registro',
            name='pagos_proveedor_data',
            field=models.JSONField(blank=True, default=list, help_text='Lista de pagos realizados a proveedores', verbose_name='Datos de Pagos Proveedor'),
        ),
        migrations.DeleteModel(
            name='Obligacion',
        ),
        migrations.DeleteModel(
            name='PagoProveedor',
        ),
        migrations.DeleteModel(
            name='PagoCliente',
        ),
    ]
