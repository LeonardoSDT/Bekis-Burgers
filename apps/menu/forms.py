# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre",
                "class": "form-control"
            }
        ))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Descripción",
                "class": "form-control"
            }
        ))
    # img_url = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "",
    #             "class": "form-control"
    #         }
    #     ))

