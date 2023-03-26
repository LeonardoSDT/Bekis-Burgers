from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.products_view, name='products'),
    path('products/<int:product_id>/', views.product_details_view, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='cart_add'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='cart_remove'),
]