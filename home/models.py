from django.db import models

# Create your models here.
class Slider(models.Model):
    img   = models.ImageField(upload_to='pics')
    desc  = models.TextField()
    name  = models.CharField(max_length = 50)

class Offers(models.Model):
    img  = models.ImageField(upload_to = 'pics')
    percent  = models.IntegerField(default=0)
    title = models.CharField(max_length = 50)

class Featured(models.Model):
    img = models.ImageField(upload_to = 'pics')
    desc  = models.TextField()
    title = models.CharField(max_length = 50)

class AllProducts(models.Model):
    img = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length = 50)
    price = models.IntegerField(default=0)
    description  = models.TextField(default="description")
    disprice = models.IntegerField(default=0)
    batch = models.DateTimeField(default = '2019-12-25 12:30')
    sale = models.BooleanField(default=False)