from django.shortcuts import render
from .models import Slider,Featured,Offers
# Create your views here.

def index(request):
    slidercontent = Slider.objects.all()
    slidernumber = range(2,len(slidercontent)+1)
    offers = Offers.objects.all()
    featured = Featured.objects.all()
    return render(request,'index.html',{'slidercontent' : slidercontent, 'slidernumber' : slidernumber, 'offers' : offers[0], 'featured' : featured[0]})

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')