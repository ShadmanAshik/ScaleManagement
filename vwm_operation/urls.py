from django.urls import path
from vwm_operation import views


urlpatterns = [

    #Shipment
    path('viewshipments', views.viewshipments, name = 'viewshipments'),
    path('createshipment', views.createshipment, name = 'createshipment'),
    path('editshipment/<str:varCode>', views.editshipment, name = 'editshipment'),

    ## Checkout
    path('shipment_checkout_list', views.shipment_checkout_list, name = 'shipment_checkout_list'),
    path('shipment_checkout/<str:varCode>', views.shipment_checkout, name = 'shipment_checkout'),

    path('checkinreceipt/<str:varCode>', views.checkinreceipt, name = 'checkinreceipt'),

]