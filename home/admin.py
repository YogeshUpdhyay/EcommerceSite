from django.contrib import admin
from .models import Featured,Offers,Slider,Products
# Register your models here.

admin.site.register(Slider)
admin.site.register(Offers)
admin.site.register(Featured)
admin.site.register(Products)