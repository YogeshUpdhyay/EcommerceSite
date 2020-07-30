from django.db import models

# Create your models here.
class Product(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length = 50)
    disprice = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    desc = models.TextField()
    sale = models.BooleanField(default = False)