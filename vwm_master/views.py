from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from vwm_master.decorators import admin_only
from vwm_master.models import *
from vwm_master.forms import *
from vwm_operation.models import *
from vwm_operation.forms import *

import datetime



def home(request):
    shipments = Shipment.objects.all()
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
        'shipments' : shipments,
        
    }


    return render(request, 'vwm_master/home.html', context)








#####################################################################################################
#####################################################################################################

## Products Category
@admin_only
def viewproductcategories(request):
    headerText = _('Product Category')
    createData = 'createproductcategory'
    products = ProductCategory.objects.all()

    context  = {
        'products' : products,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'vwm_master/masterview.html', context)


@admin_only
def createproductcategory(request):
    headerText = _('Product Category')
    form = ProductCategoryForm()

    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.save()
                return redirect('viewproductcategories') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)



@admin_only
def editproductcategory(request, varCode):
    headerText = _('Product Category')
    product = ProductCategory.objects.get(id = varCode)
    form = ProductCategoryForm(instance = product)

    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, instance = product)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.creationDate = datetime.datetime.now()
                data.save()
                return redirect('viewproductcategories')  
        except Exception as e:
            messages.error(request, str(e))  


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)


@admin_only
def deleteproductcategory(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Product Category'

    deletedVal = ProductCategory.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewproductcategories')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
    }
    return render(request, 'vwm_master/masterentry.html', context)








## Products
@admin_only
def viewproducts(request):
    headerText = _('Products')
    createData = 'createproduct'
    products = Products.objects.all()

    context  = {
        'products' : products,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'vwm_master/masterview.html', context)


@admin_only
def createproduct(request):
    headerText = _('Products')
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.save()
                return redirect('viewproducts') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)



@admin_only
def editproduct(request, varCode):
    headerText = _('Products')
    product = Products.objects.get(id = varCode)
    form = ProductForm(instance = product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.creationDate = datetime.datetime.now()
                data.save()
                return redirect('viewproducts')  
        except Exception as e:
            messages.error(request, str(e))  


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)


@admin_only
def deleteproduct(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Product'

    deletedVal = Products.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewproducts')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
    }
    return render(request, 'vwm_master/masterentry.html', context)










## Product Charging
@admin_only
def viewproductcharging(request):
    headerText = _('Product Charging')
    createData = 'createproductcharging'
    products = ProductCharging.objects.all()

    context  = {
        'products' : products,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'vwm_master/masterview.html', context)


@admin_only
def createproductcharging(request):
    headerText = _('Product Charging')
    form = ProductChargingForm()

    if request.method == 'POST':
        form = ProductChargingForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.save()
                return redirect('viewproductcharging') 
        except Exception as e:
            messages.error(request, str(e))
         

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)



@admin_only
def editproductcharging(request, varCode):
    headerText = _('Product Charging')
    product = ProductCharging.objects.get(id = varCode)
    form = ProductChargingForm(instance = product)

    if request.method == 'POST':
        form = ProductChargingForm(request.POST, instance = product)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.creationDate = datetime.datetime.now()
                data.save()
                return redirect('viewproductcharging')  
        except Exception as e:
            messages.error(request, str(e))  


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)


@admin_only
def deleteproductcharging(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Product Charging'

    deletedVal = ProductCharging.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewproductcharging')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.product.name,
    }
    return render(request, 'vwm_master/masterentry.html', context)






################################################################################################

#Supplier
@admin_only
def createsupplier(request):
    headerText = _('Supplier')
    form= SupplierForm()

    if request.method=='POST':
        form=SupplierForm(request.POST)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.save()
                return redirect('viewsuppliers')  
        except Exception as e:
                messages.error(request, str(e))

    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)




@admin_only
def viewsuppliers(request):
    headerText = _('Supplier')
    createData = 'createsupplier'
    suppliers = Supplier.objects.all()

    context  = {
        'suppliers' : suppliers,
        'headerText' : headerText,
        'createData' : createData,
    }
    return render(request, 'vwm_master/masterview.html', context)





@admin_only
def editsupplier(request, varCode):
    headerText = _('Supplier')
    supplier = Supplier.objects.get(id = varCode)
    form = SupplierForm(instance = supplier)

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance = supplier)
        try:
            if form.is_valid():
                data = form.save(commit = False)
                data.createdBy = request.user
                data.creationDate = datetime.datetime.now()
                data.save()
                return redirect('viewsuppliers')  
        except Exception as e:
            messages.error(request, str(e))  


    context  = {
        'form' : form,
        'headerText' : headerText,
    }
    return render(request, 'vwm_master/masterentry.html', context)


@admin_only
def deletesupplier(request, varCode):
    headerText = 'Delete'
    deletedItem = 'Supplier'

    deletedVal = Supplier.objects.get(id = varCode)

    if request.method == 'POST':
        try:
            deletedVal.delete()
            return redirect('viewsuppliers')  
        except Exception as e:
            messages.error(request, str(e))  

    context  = {
        'headerText' : headerText,
        'deletedItem' : deletedItem,
        'deletedVal' : deletedVal.name,
    }
    return render(request, 'vwm_master/masterentry.html', context)
