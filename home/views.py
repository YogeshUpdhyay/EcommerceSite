from django.shortcuts import render,redirect
from products.models import *
# Create your views here.

def index(request):

    # Featuring slider products
    sliders = Product.objects.filter(slider=True).only('name', 'desc', 'img')[:3]
    offer = Product.objects.filter(percent__gte=50).only('name', 'percent', 'img')[0]
    featured = Product.objects.filter(featured=True).only('name', 'desc', 'img')[0]
    products = Product.objects.all()[0:4]

    # Rendering the content
    content = {
        'sliders' : sliders,
        'offer' : offer,
        'featured' : featured,
        'products' : products
    }
    
    return render(request, 'index.html', content)

def allproducts(request):
    products = Product.objects.all()
    content = {
        'products' : products
    }
    return render (request,'allproducts.html',content)

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')