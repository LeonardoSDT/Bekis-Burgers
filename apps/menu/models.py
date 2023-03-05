from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40, default='', blank=False)
    description = models.CharField(max_length=200, default='', blank=False)
    img_url = models.CharField(max_length=40, default='', blank=False)