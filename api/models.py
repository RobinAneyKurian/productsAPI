from django.db import models

# Create your models here.

class Products(models.Model):
    items = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    company = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=1)

