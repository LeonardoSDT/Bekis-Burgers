from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem, Product
from .forms import CartAddProductForm

# Create your views here.

def check_staff(user):
   return user.is_staff

def products_view(request):
    products = Product.objects.all()
    
    return render(request, "menu/products.html", {'products': products})

def product_details_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CartAddProductForm(request.POST)
    context = {'product': product, 'form': form}
    return render(request, 'menu/product_detail.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cart_item.quantity = form.cleaned_data['quantity']
            cart_item.subtotal = cart_item.quantity * product.price
            cart_item.save()
            return redirect('cart')
    else:
        form = CartAddProductForm()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart = cart_qs.get()
        context = {
            'cart': cart,
        }
        return render(request, 'menu/cart.html', context)
    else:
        # handle the case when the cart doesn't exist
        return render(request, 'menu/cart.html')