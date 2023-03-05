from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.products_view, name='products'),
    path('add/', views.add_view, name='add'),
]