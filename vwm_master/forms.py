from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from vwm_master.models import *


class DateInput(forms.DateInput):
    input_type = 'date'




class ProductCategoryForm(ModelForm):
    name = forms.CharField(max_length=200, label = _('Product Category Name'))

    class Meta:
        model = ProductCategory
        fields = ['name']




class ProductForm(ModelForm):
    name = forms.CharField(max_length=200, label = _('Product Name'))

    class Meta:
        model = Products
        fields = ['name', 'productcategory', 'measurementUnit']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['productcategory'].label = _('Product Category')
        self.fields['productcategory'].required = True
        self.fields['measurementUnit'].label = _('Measurement Unit')
        self.fields['measurementUnit'].required = True







class ProductChargingForm(ModelForm):
    price = forms.DecimalField(label = _('Price'))
    startDate = forms.DateField(label = _('Start Date'), widget = DateInput)
    endDate = forms.DateField(label = _('End Date'), widget = DateInput)

    class Meta:
        model = ProductCharging
        fields = ['product', 'price', 'startDate', 'endDate']

    def __init__(self, *args, **kwargs):
        super(ProductChargingForm, self).__init__(*args, **kwargs)

        self.fields['product'].label = _('Product Name')
        self.fields['product'].required = True





class SupplierForm(ModelForm):
    name = forms.CharField(max_length=200, label= _('Supplier Name'))
    phone = forms.CharField(max_length=200, label= _('Phone Number'))
    address = forms.CharField(max_length=500, label= _('Address'), widget = forms.Textarea(attrs = {'rows' : 2}))
    contactPerson = forms.CharField(max_length=500, label= _('Contact Person'), widget = forms.Textarea(attrs = {'rows' : 3}))
    
    class Meta:
        model= Supplier
        fields= ['name', 'phone', 'address', 'contactPerson']



WEIGHT_CHOICE=[('gross', 'Gross' ),
                ('tare', 'Tare')]
class ShipmentForm(ModelForm):
    weightype=forms.ChoiceField(choices=WEIGHT_CHOICE, required=True, widget=forms.RadioSelect)
    vehicleNo = forms.CharField(max_length=200, label= _('Vehicle No'))
    driverName = forms.CharField(max_length=200, label= _('Driver name'))
    driverPhone = forms.CharField(max_length=200, label= _('Driver Phone'))
    # grossWeight = forms.DecimalField(max_digits = 10, decimal_places = 2, label = _('Gross Weight'))
    #deliveryEntryTime = forms.DateTimeField(label = _('Entry Time'), widget = forms.DateTimeInput())
    remarks = forms.CharField(max_length=500, label= _('Remarks'), widget = forms.Textarea(attrs = {'rows' : 3}), required = False)
    
    class Meta:
        model=Shipment
        fields=['product', 'supplier', 'vehicleNo', 'driverName', 'driverPhone', 'remarks']
    
    def __init__(self, *args, **kwargs):
        super(ShipmentForm, self).__init__(*args, **kwargs)
        
        self.fields['supplier'].label= 'Sender Name'
        self.fields['supplier'].required = True
        self.fields['product'].label = 'Product Name'
        self.fields['product'].required = True
