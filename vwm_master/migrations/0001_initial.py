# Generated by Django 3.2.13 on 2022-06-08 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('measurementUnit', models.CharField(blank=True, choices=[('Ton', 'Ton'), ('Kg', 'Kg')], max_length=100, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('productcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vwm_master.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('contactPerson', models.CharField(blank=True, max_length=500, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleNo', models.CharField(blank=True, max_length=100, null=True)),
                ('driverName', models.CharField(blank=True, max_length=100, null=True)),
                ('driverPhone', models.CharField(blank=True, max_length=100, null=True)),
                ('grossWeight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('tareWeight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('netWeight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('deliveryEntryTime', models.DateTimeField(blank=True, null=True)),
                ('deliveryExitTime', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=1000, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vwm_master.products')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vwm_master.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCharging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vwm_master.products')),
            ],
        ),
    ]