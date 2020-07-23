from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('product.html', views.product),
    path('cart.html', views.cart),
    path('checkout.html', views.checkout),
    path('contact.html', views.contact),
]