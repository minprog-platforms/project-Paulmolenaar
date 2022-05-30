from queue import Empty
from django.contrib.auth import authenticate, login, logout
import datetime
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django import forms
from .models import *
from .forms import *
from .functions import *

COORDS_MAGAZIJN  = [52.0843143, 4.9420627]
VERZENDKOSTEN_KM = 1.5

def index(request):    
    return render(request, "pages/index.html")

def product(request,product):
    currentProduct = Producten.objects.get(naam=product)
    return render(request, "pages/product.html",{
        "product" : currentProduct
    })

def assortiment(request):
    
    producten_lijst = []
    producten = Producten.objects.all()
    for product in producten:
        if (product.voorraad > 0):
            producten_lijst.append(product)

    return render(request, "pages/assortiment.html",{
        "producten_lijst" : producten_lijst
    })

def kamer_inrichten(request):

    if request.user.is_authenticated:        
        kamer = KamerAfmetingen()

        try:
            kamer = KamerAfmetingen.objects.get(user=request.user)
        except Exception:
            kamer = KamerAfmetingen.objects.create(user=request.user)

        bestelling = userKrijgLaatsteBestelling(request.user)

        form = AfmetingenForm()
        form.fields['breedte'].initial = kamer.afmeting_breedte
        form.fields['lengte'].initial  = kamer.afmeting_lengte
        form.fields['hoogte'].initial  = kamer.afmeting_hoogte

        if request.method == "POST":
            producten = request.POST.getlist('producten[]')
            if ('productAdd' in request.POST):
                product = Producten.objects.get(naam=request.POST['productAdd'])
                if product is not None:
                    bestelling.producten.add(product)

                bestelling.save()
            elif('productRemove' in request.POST):
                product = Producten.objects.get(naam=request.POST['productRemove'])
                if product is not None:
                    if (product in bestelling.producten.all()):
                        bestelling.producten.remove(product)

                bestelling.save()
            else: 
                form = AfmetingenForm(request.POST)
                
                if (form.is_valid):                
                    kamer.afmeting_breedte = int(request.POST['breedte'])
                    kamer.afmeting_lengte  = int(request.POST['lengte'])
                    kamer.afmeting_hoogte  = int(request.POST['hoogte'])
                    kamer.save()

        oppervlakte = kamer.berekenOppervlakte()
        gebruikte_oppervlakte = 0
        totaalPrijs = 0

        for productItem in bestelling.producten.all():
            gebruikte_oppervlakte = gebruikte_oppervlakte + productItem.afmeting_oppervlakte
            totaalPrijs = totaalPrijs + productItem.prijs
        
        ongebruikte_oppervlakte = oppervlakte - gebruikte_oppervlakte

        productList = []
        for productItem in Producten.objects.all():
            if (productItem.voorraad <= 0):
                continue
            
            if (ongebruikte_oppervlakte > productItem.afmeting_oppervlakte):
                productList.append(productItem)

        percentage = 0
        if (oppervlakte > 0):
            percentage = round(float(( gebruikte_oppervlakte / oppervlakte ) * 100),1)
        

        bestelling.prijs_maand = totaalPrijs
        bestelling.save()

        return render(request, "pages/inrichten.html",{
            "form" : form,
            "producten" : productList,
            "bestelling_producten" : bestelling.producten.all(),
            "winkelwagen_totaal" : totaalPrijs,
            "percentage" : percentage
        })
    else:
        return render(request, "pages/login.html")

def afgerond(request):

    
    bestelling = userKrijgLaatsteBestelling(request.user)
    if (bestelling == None):
        return HttpResponseRedirect(reverse("kamerinrichten"))

    bestelling.afgerond = True
    bestelling.datum_afgerond = datetime.now()
    bestelling.datum = datetime.now()
    bestelling.save()

    for product in bestelling.producten.all():
        product.voorraad = product.voorraad - 1
        product.save()

    return render(request, "pages/afgerond.html")

def bestellen(request):
    if request.user.is_authenticated:
        bestelling = userKrijgLaatsteBestelling(request.user)

        form = BestellingForm()

        form.fields['plaats'].initial           = bestelling.adres_plaats
        form.fields['straat_nummer'].initial    = bestelling.adres_straat_nummer
        form.fields['postcode'].initial         = bestelling.adres_postcode
        
        if (bestelling.datum_tot != '1970-01-01 00:00'):
            form.fields['datum_tot'].initial         = bestelling.datum_tot

        if request.method == "POST":
            form = BestellingForm(request.POST)
            
            if (form.is_valid):                
                bestelling.adres_plaats = request.POST['plaats']
                bestelling.adres_straat_nummer = request.POST['straat_nummer']
                bestelling.adres_postcode = request.POST['postcode']
                bestelling.datum = datetime.now()
                bestelling.datum_tot = datetime. strptime(form.data['datum_tot'], '%Y-%m-%d')

                coords_klant = getCoords(bestelling.adres_plaats)

                aantal_maanden = berekenMaanden(datetime.now(), bestelling.datum_tot)

                bestelling.afstand = calculateLength(COORDS_MAGAZIJN, coords_klant)
                bestelling.prijs_verzending = float(bestelling.afstand * VERZENDKOSTEN_KM)
                bestelling.prijs_totaal = (bestelling.prijs_maand * aantal_maanden) + bestelling.prijs_verzending 
                bestelling.save()

        aantal_maanden = berekenMaanden(datetime.now(), bestelling.datum_tot)

        return render(request, "pages/bestellen.html",{
            "form": form,
            "bestelling_producten" : bestelling.producten.all(),
            "producten_totaal" : round(bestelling.productenTotaal(),2),
            "totaal_maanden" : aantal_maanden,
            "totaal_reisafstand" : round(bestelling.afstand,1),
            "totaal_verzendkosten" : round(bestelling.prijs_verzending,2),
            "totaal_bestelling" : round(bestelling.prijs_totaal,2),
        })
    else:
        return render(request, "pages/login.html")    

def winkelwagen(request):
    return render(request, "pages/winkelwagen.html")          

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pages/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "pages/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def over_ons(request):
    return render(request, "pages/overons.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "pages/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)            
            user.save()
            
        except IntegrityError as e: 
            return render(request, "pages/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pages/register.html")

