from django.shortcuts import render

from django.contrib.auth.decorators import user_passes_test
from .models import Product

# Create your views here.

def check_staff(user):
   return user.is_staff

def products_view(request):
    products = Product.objects.all()
    
    return render(request, "menu/products.html", {'products': products})

@user_passes_test(check_staff)
def add_view(request):

    return render(request, "menu/add.html", {})