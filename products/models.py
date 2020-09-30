from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length = 50)
    disprice = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    desc = models.TextField()
    sale = models.BooleanField(default = False)
    percent = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)

    def __str__(self):
        return self.name