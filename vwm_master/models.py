from django.db import models
from django.contrib.auth.models import User
#Barcode
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File



class ProductCategory(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True)
    createdBy = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.name



MEASUREMENTUNIT_CHOICES = (
    ('Ton', 'Ton'),
    ('Kg', 'Kg')
)

class Products(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True)
    productcategory = models.ForeignKey(ProductCategory, on_delete = models.SET_NULL, null = True, blank = True)
    measurementUnit = models.CharField(max_length=100, null = True, blank = True, choices = MEASUREMENTUNIT_CHOICES)
    createdBy = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.name




class ProductCharging(models.Model):
    product = models.ForeignKey(Products, on_delete = models.SET_NULL, null = True, blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, null = True, blank = True)
    startDate = models.DateField(auto_now_add = False, null = True, blank = True)
    endDate = models.DateField(auto_now_add = False, null = True, blank = True)
    createdBy = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.product.name



class Supplier(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 15, null = True, blank = True)
    address=models.CharField(max_length = 500, null = True, blank = True)
    contactPerson = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.name

class Reciever(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    phone = models.CharField(max_length = 15, null = True, blank = True)
    address=models.CharField(max_length = 500, null = True, blank = True)
    contactPerson = models.CharField(max_length = 500, null = True, blank = True)
    createdBy = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.name


class Shipment1(models.Model):
    product = models.ForeignKey(Products, on_delete = models.SET_NULL, null = True, blank = True)
    supplier = models.ForeignKey(Supplier, on_delete = models.SET_NULL, null = True, blank = True)
    reciever = models.ForeignKey(Reciever, on_delete = models.SET_NULL, null = True, blank = True)   
    vehicleNo = models.CharField(max_length = 100, null = True, blank = True)
    driverName = models.CharField(max_length = 100, null = True, blank = True)
    driverPhone = models.CharField(max_length = 100, null = True, blank = True)
    grossWeight = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    tareWeight = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    netWeight = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    deduct = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    deductRate = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    realNet = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)    
    grossTime = models.DateTimeField(auto_now_add = False, null = True, blank = True)
    tareTime = models.DateTimeField(auto_now_add = False, null = True, blank = True)
    remarks = models.CharField(max_length = 1000, null = True, blank = True)
    barcode = models.ImageField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    createdBy = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.supplier.name + '-' + self.vehicleNo
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.id}.{self.vehicleNo}', writer = ImageWriter()).write(rv)
        self.barcode.save(f'{self.id}.png', File(rv), save = False)

        return super().save(*args, **kwargs)

    @property
    def barcodeURL(self):
        try:
            url = self.barcode.url 
        except:
            url = ''
        return url

class Shipment(models.Model):
    product = models.ForeignKey(Products, on_delete = models.SET_NULL, null = True, blank = True)
    supplier = models.ForeignKey(Supplier, on_delete = models.SET_NULL, null = True, blank = True)
    vehicleNo = models.CharField(max_length = 100, null = True, blank = True)
    driverName = models.CharField(max_length = 100, null = True, blank = True)
    driverPhone = models.CharField(max_length = 100, null = True, blank = True)
    grossWeight = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    tareWeight = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    netWeight = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True, null = True)
    deliveryEntryTime = models.DateTimeField(auto_now_add = False, null = True, blank = True)
    deliveryExitTime = models.DateTimeField(auto_now_add = False, null = True, blank = True)
    remarks = models.CharField(max_length = 1000, null = True, blank = True)
    barcode = models.ImageField(null = True, blank = True)
    complete = models.BooleanField(default = False)
    createdBy = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    creationDate = models.DateTimeField(auto_now_add = True, null = True, blank = True)

    def __str__(self):
        return self.supplier.name + '-' + self.vehicleNo


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.id}.{self.vehicleNo}', writer = ImageWriter()).write(rv)
        self.barcode.save(f'{self.id}.png', File(rv), save = False)

        return super().save(*args, **kwargs)


    @property
    def barcodeURL(self):
        try:
            url = self.barcode.url 
        except:
            url = ''
        return url