# Generated by Django 4.2 on 2025-01-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cajero_Pichincha', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='identification',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
