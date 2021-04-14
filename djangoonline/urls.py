
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Order import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('product/',include('Product.urls')),
    path('cart/',include('Order.urls')),
    path('myaccount/', views.myaccount,name= 'myaccount'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
