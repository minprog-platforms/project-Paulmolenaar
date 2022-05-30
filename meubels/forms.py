from datetime import datetime
from django.forms import ModelForm
from django import forms
from .models import *
import datetime


class AfmetingenForm(forms.Form):
    lengte = forms.IntegerField(
        required=True,
        label="Lengte (cm)",
        widget=forms.NumberInput(
            attrs={"placeholder": "Wat is de lengte?"}
        ),
    )   
    breedte = forms.IntegerField(
        required=True,
        label="Breedte (cm)",
        widget=forms.NumberInput(
            attrs={"placeholder": "Wat is de breedte?"}
        ),
    )   
    hoogte = forms.IntegerField(
        required=True,
        label="Hoogte (cm)",
        widget=forms.NumberInput(
            attrs={"placeholder": "Wat is de hoogte?"}
        ),
    )
    
class BestellingForm(forms.Form):
    plaats = forms.CharField(
        required=True,
        label="Woonplaats",
        widget=forms.TextInput(
            attrs={"placeholder": "Bijv. Amsterdam"}
        ),
    )   
    straat_nummer = forms.CharField(
        required=True,
        label="Straat + nummer",
        widget=forms.TextInput(
            attrs={"placeholder": "Bijv. plaatsnaam 12b"}
        ),
    )
    postcode = forms.CharField(
        required=True,
        label="Postcode",
        widget=forms.TextInput(
            attrs={"placeholder": "Bijv. 1234AB"}
        ),
    )
    
    datum_tot = forms.DateField(
        required=True,
        label="Einddatum",
        widget=forms.DateInput(            
            attrs={"min": datetime.datetime.now(), "type":"date"}
        ),
    )