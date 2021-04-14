from django.urls import path
from .views import detail,addcart,delecart,updatecart
app_name = 'Product'
urlpatterns = [

    path('<int:id>', detail, name = 'detail'),
    path('addtocart', addcart, name = 'addtocart'),
    path('deletecart', delecart, name = 'deletecart'),
    path('updatecart', updatecart, name = 'updatecart'),

]