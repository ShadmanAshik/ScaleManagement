from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from vwm_master.decorators import admin_only
from vwm_master.forms import ShipmentForm
from vwm_master.models import *
from vwm_operation.forms import *

import datetime




@admin_only
def viewshipments(request):
    headerText = 'Shipments'
    createData = 'createshipment'
    shipments = Shipment.objects.all()

    context  = {
        'shipments' : shipments,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'vwm_master/masterview.html', context)


@admin_only
# def createshipment(request):
#     headerText ='Shipment'
#     form= ShipmentCheckInForm()

#     if request.method=='POST':
#         form=ShipmentCheckInForm(request.POST)
#         try:
#             if form.is_valid():
#                 data = form.save(commit = False)
#                 data.deliveryEntryTime = datetime.datetime.now()
#                 data.createdBy = request.user
#                 data.save()
#                 return redirect('checkinreceipt', varCode = data.id)
#         except Exception as e:
#                 messages.error(request, str(e))

#     context  = {
#         'form' : form,
#         'headerText' : headerText,
#     }
#     return render(request, 'vwm_master/masterentry.html', context)
def createshipment(request):
    headerText ='Shipment'
    form= ShipmentForm()

    if request.method=='POST':
        form=ShipmentForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.grossTime = datetime.datetime.now()
                data.createdBy = request.user
                data.save()
                return redirect('home')
        except Exception as e:
                messages.error(request, str(e))

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/home.html', context)
    




@admin_only
def checkinreceipt(request, varCode):
    headerText ='Shipment Check-In Receipt'
    createData = 'No'
    shipment = Shipment.objects.get(id = varCode)
    context  = {
        'shipment' : shipment,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'vwm_master/masterview.html', context)



@admin_only
def shipment_checkout_list(request):
    headerText ='Shipment Check-Out'
    createData = 'No'
    shipments = Shipment.objects.filter(deliveryEntryTime__date = datetime.date.today(), complete = False)

    context  = {
        'shipments' : shipments,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'vwm_master/masterview.html', context)    




@admin_only
def shipment_checkout(request, varCode):
    headerText ='Shipment Check-Out'
    
    shipment = Shipment.objects.get(id = varCode)
    form = ShipmentCheckOutForm(instance = shipment)

    if request.method == 'POST':
        form = ShipmentCheckOutForm(request.POST, instance = shipment)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.deliveryExitTime = datetime.datetime.now()
                data.netWeight = data.grossWeight - data.tareWeight
                data.complete = True
                data.save()
                return redirect('shipment_checkout_list')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)   




@admin_only
def editshipment(request, varCode):
    headerText = 'Shipment'
    shipment = Shipment.objects.get(id = varCode)
    form = ShipmentCheckInForm(instance = shipment)

    if request.method == 'POST':
        form = ShipmentCheckInForm(request.POST, instance = shipment)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.creationDate = datetime.datetime.now()
                data.save()
                return redirect('viewshipments')  
        except Exception as e:
            messages.error(request, str(e))  


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)