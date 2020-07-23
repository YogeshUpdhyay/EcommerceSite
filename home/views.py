from django.shortcuts import render
from .models import Slider,Featured,Offers
# Create your views here.
def index(request):
    slidercontent = Slider.objects.all()
    slidernumber = range(2,len(slidercontent)+1)
    offers = Offers.objects.all()
    print(len(offers))
    featured = Featured.objects.all()
    print(len(featured))
    return render(request,'index.html',{'slidercontent' : slidercontent, 'slidernumber' : slidernumber, 'offers' : offers, 'featured' : featured})

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')