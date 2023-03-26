from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255,blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    img_url = models.CharField(max_length=40,blank=False)
    category = models.CharField(max_length=255,blank=False)
    quantity = models.PositiveIntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.product