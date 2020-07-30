from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request,productname):
    product = Product.objects.get(name = productname)
    return render(request,'product.html',{'product' : product})