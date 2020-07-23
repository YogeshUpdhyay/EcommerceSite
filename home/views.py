from django.shortcuts import render
from .models import Slider
# Create your views here.
def index(request):
    slidercontent = Slider.objects.all()
    return render(request,'index.html',{'slidercontent' : slidercontent, 'slidernumber' : range(2,len(slidercontent))})

def product(request):
    return render(request,'product.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')