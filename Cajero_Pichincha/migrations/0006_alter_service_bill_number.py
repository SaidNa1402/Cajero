# Generated by Django 4.2 on 2025-01-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cajero_Pichincha', '0005_transaction_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='bill_number',
            field=models.CharField(max_length=10, verbose_name='Número de factura'),
        ),
    ]
