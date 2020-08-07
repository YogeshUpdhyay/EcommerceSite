from django.shortcuts import render,redirect
from .models import Product
# Create your views here.

def product(request,productname):
    product = Product.objects.get(name = productname)
    relproducts = Product.objects.all()[:4]
    content = {
        'product' : product,
        'relproducts' : relproducts
    }
    return render(request,'product.html',content)
