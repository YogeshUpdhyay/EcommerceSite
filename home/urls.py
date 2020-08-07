from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name = 'home'),
    path('cart', views.cart,name = 'cart'),
    path('allproducts', views.allproducts,name = 'allproducts'),
    path('checkout', views.checkout,name = 'checkout'),
    path('contact', views.contact,name = 'contact'),
]