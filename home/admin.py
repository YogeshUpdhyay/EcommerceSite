from django.contrib import admin
from .models import Featured,Offers,Slider
# Register your models here.

admin.site.register(Slider)
admin.site.register(Offers)
admin.site.register(Featured)