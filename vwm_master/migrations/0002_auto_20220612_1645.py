# Generated by Django 3.2.13 on 2022-06-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vwm_master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='barcode',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
