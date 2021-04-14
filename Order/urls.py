
from django.contrib import admin
from django.urls import path,include
from .views import viewcart,checkout,updateaddress,addship,payment
app_name = 'Order'

urlpatterns = [
    path('',viewcart, name = 'view'),
    path('checkout',checkout, name = 'checkout'),
    path('updateadd',updateaddress, name = 'updateadd'),
    path('addship',addship, name = 'addship'),
    path('payment',payment, name = 'payment'),
]