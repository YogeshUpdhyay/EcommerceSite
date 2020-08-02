from django.shortcuts import render,redirect
from .models import Slider,Featured,Offers
from products.models import Product
# Create your views here.

def index(request):
    slidercontent = Slider.objects.all()
    slidernumber = range(2,len(slidercontent)+1)
    offers = Offers.objects.get()
    featured = Featured.objects.get()
    products = Product.objects.all()
    content = {
        'slidercontent' : slidercontent, 
        'slidernumber' : slidernumber, 
        'offers' : offers, 
        'featured' : featured,
        'products' : products
    }
    return render(request,'index.html',content)

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