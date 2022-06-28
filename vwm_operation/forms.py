from dataclasses import fields
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from vwm_master.models import *


class DateInput(forms.DateInput):
    input_type = 'date'



class ShipmentCheckInForm(ModelForm):
    vehicleNo = forms.CharField(max_length=200, label= _('Vehicle No'))
    driverName = forms.CharField(max_length=200, label= _('Driver name'))
    driverPhone = forms.CharField(max_length=200, label= _('Driver Phone'))
    grossWeight = forms.DecimalField(max_digits = 10, decimal_places = 2, label = _('Gross Weight'))
    #deliveryEntryTime = forms.DateTimeField(label = _('Entry Time'), widget = forms.DateTimeInput())
    remarks = forms.CharField(max_length=500, label= _('Remarks'), widget = forms.Textarea(attrs = {'rows' : 3}), required = False)
    
    class Meta:
        model=Shipment
        fields=['product', 'supplier', 'vehicleNo', 'driverName', 'driverPhone', 'grossWeight', 'remarks']
    
    def __init__(self, *args, **kwargs):
        super(ShipmentCheckInForm, self).__init__(*args, **kwargs)
        
        self.fields['supplier'].label= 'Supplier Name'
        self.fields['supplier'].required = True
        self.fields['product'].label = 'Product Name'
        self.fields['product'].required = True




class ShipmentCheckOutForm(ModelForm):
    vehicleNo = forms.CharField(max_length=200, label= _('Vehicle No'))
    tareWeight = forms.DecimalField(max_digits = 10, decimal_places = 2, label = _('Tare Weight'))
    remarks = forms.CharField(max_length=500, label= _('Remarks'), widget = forms.Textarea(attrs = {'rows' : 3}), required = False)

    class Meta:
        model = Shipment
        fields = ['vehicleNo', 'tareWeight', 'remarks']