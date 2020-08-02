from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('cart', views.cart),
    path('allproducts', views.allproducts),
    path('checkout', views.checkout),
    path('contact', views.contact),
]