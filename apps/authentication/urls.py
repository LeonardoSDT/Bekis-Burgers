# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, edit_view, delete_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('edit/', edit_view, name="edit"),
    path('delete/', delete_view, name="delete"),
    path("logout/", LogoutView.as_view(), name="logout")
]
