from django.shortcuts import render
from .models import Slider,Featured,Offers
# Create your views here.

def index(request):
    slidercontent = Slider.objects.all()
    slidernumber = range(2,len(slidercontent)+1)
    offers = Offers.objects.get()
    featured = Featured.objects.get()
    content = {
        'slidercontent' : slidercontent, 
        'slidernumber' : slidernumber, 
        'offers' : offers, 
        'featured' : featured
        #'products' : products
    }
    return render(request,'index.html',content)

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')