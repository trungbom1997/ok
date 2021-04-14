from django.urls import path
from .views import homepage,login,register,categoryView
app_name = 'homepage'
urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('category/<str:key>/', categoryView, name = 'category'),
]