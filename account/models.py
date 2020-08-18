from django.db import models

# Create your models here.

class Account(models.Model):
    firstname  = models.CharField(max_length = 50)
    lastname   = models.CharField(max_length = 50)
    country    = models.CharField(max_length = 50)
    address    = models.TextField()
    zipcode    = models.IntegerField(default=0)
    city       = models.CharField(max_length = 50)
    province   = models.CharField(max_length = 50)
    email_id   = models.EmailField(max_length=254)
    terms_condition = models.BooleanField(default = True)
    create = models.BooleanField(default = True)
    cart_value = models.IntegerField(default=0)
