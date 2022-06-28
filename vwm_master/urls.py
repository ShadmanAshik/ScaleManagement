from django.urls import path
from vwm_master import views


urlpatterns = [
    path('', views.home, name = 'home'),

    ## Product Category
    path('viewproductcategories', views.viewproductcategories, name = 'viewproductcategories'),
    path('createproductcategory', views.createproductcategory, name = 'createproductcategory'),
    path('editproductcategory/<str:varCode>', views.editproductcategory, name = 'editproductcategory'),
    path('deleteproductcategory/<str:varCode>', views.deleteproductcategory, name = 'deleteproductcategory'),


    ## Product
    path('viewproducts', views.viewproducts, name = 'viewproducts'),
    path('createproduct', views.createproduct, name = 'createproduct'),
    path('editproduct/<str:varCode>', views.editproduct, name = 'editproduct'),
    path('deleteproduct/<str:varCode>', views.deleteproduct, name = 'deleteproduct'),



    ## Product Charging
    path('viewproductcharging', views.viewproductcharging, name = 'viewproductcharging'),
    path('createproductcharging', views.createproductcharging, name = 'createproductcharging'),
    path('editproductcharging/<str:varCode>', views.editproductcharging, name = 'editproductcharging'),
    path('deleteproductcharging/<str:varCode>', views.deleteproductcharging, name = 'deleteproductcharging'),




    #Supplier
    path('viewsuppliers', views.viewsuppliers, name = 'viewsuppliers'),
    path('createsupplier', views.createsupplier, name = 'createsupplier'),
    path('editsupplier/<str:varCode>', views.editsupplier, name = 'editsupplier'),
    path('deletesupplier/<str:varCode>', views.deletesupplier, name = 'deletesupplier'),


]