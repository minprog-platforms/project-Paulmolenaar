from django.forms import ModelForm
from django import forms
from .models import *


class AfmetingenForm(ModelForm):
    lengte = forms.IntegerField(
        required=True,
        label="lengte",
        widget=forms.NumberInput(
            attrs={"placeholder": "Wat is de lengte?"}
        ),
    )   
    breedte = forms.IntegerField(
        required=True,
        label="breedte",
        widget=forms.NumberInput(
            attrs={"placeholder": "Wat is de breedte?"}
        ),
    )   
    hoogte = forms.IntegerField(
        required=True,
        label="hoogte",
        widget=forms.NumberInput(
            attrs={"placeholder": "Wat is de hoogte?"}
        ),
    )   
