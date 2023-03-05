# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm, UpdateUserForm, DeleteUserForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Credenciales inválidas'
        else:
            msg = 'Error validando el formulario'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Cuenta creada satisfactoriamente'
            success = True

            # return redirect("/login/")

        else:
            msg = 'El formulario no es válido'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

@login_required
def edit_view(request):
    msg = None
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            msg = 'Su perfil ha sido actualizado correctamente'
        else:
            msg = 'El formulario no es válido'
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'accounts/edit.html', {'user_form': user_form, "msg": msg})

@login_required
def delete_view(request):
    msg = None
    if request.method == 'POST':
        delete_form = DeleteUserForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        msg = 'La cuenta de usuario ha sido eliminada'
        return redirect("/")
    else:
        delete_form = DeleteUserForm(instance=request.user)

    return render(request, 'accounts/delete.html', {'delete_form': delete_form, "msg": msg})

