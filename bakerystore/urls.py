from django.urls import path
from . import views

app_name = 'bakerystore'

urlpatterns = [
    path('', views.index, name='index'),
    path('find-customer/', views.find_customer, name='find-customer'),
    path('add-customer/<int:customer_id>/', views.add_customer, name='add-customer'),
    path('take-order/<int:order_id>/', views.take_order, name='take-order'),
    path('take-order/<int:order_id>/confirm/', views.confirm_order, name='confirm_order'),
    path('printbill/<int:bill_id>/', views.printbill, name='printbill'),
    path('add-product/', views.add_product, name='add-product'),
    path('update-product/', views.update_product, name='update-product'),
    path('view-order/', views.view_order, name='view-order'),
    path('view-order/<int:orderid>/', views.view_order_specific, name='view-order-specific'),
    path('done-orders/', views.done_orders, name='done-orders'),
    path('canceled-orders/', views.canceled_orders, name='canceled-orders'),
    path('mark-done/<int:order_id>/', views.mark_order_done, name='mark-done'),
    path('mark-canceled/<int:order_id>/', views.mark_order_canceled, name='mark-canceled'),
    path('add-supplier/', views.add_supplier, name='add-supplier'),
    path('add-supply-order/', views.add_supply_order, name='add-supply-order'),
    path('view-supply-order/', views.view_supply_order, name='view-supply-order'),
    path('view-supply-order/update-invoice/<int:invoice_id>/', views.update_status, name='update-invoice'),
    path('view-home-delivery/', views.view_home_delivery, name='view-home-delivery'),
]