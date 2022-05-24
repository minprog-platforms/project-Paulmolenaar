from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django import forms
from .models import *
from .forms import *

def index(request):    
    return render(request, "pages/index.html")

def product(request,product):
    currentProduct = Producten.objects.get(naam=product)
    return render(request, "pages/product.html",{
        "product" : currentProduct
    })

def kamer_inrichten(request):

    if request.user.is_authenticated:        
        kamer = KamerAfmetingen()

        try:
            kamer = KamerAfmetingen.objects.get(user=request.user)
        except Exception:
            print ("kamer does not exist")
            kamer = KamerAfmetingen.objects.create(user=request.user)

        try:
            bestelling = Bestellingen.objects.get(user=request.user, afgerond = False)
        except Exception:
            bestelling = Bestellingen.objects.create(user=request.user, afgerond = False)

        form = AfmetingenForm()
        form.fields['breedte'].initial = kamer.afmeting_breedte
        form.fields['lengte'].initial  = kamer.afmeting_lengte
        form.fields['hoogte'].initial  = kamer.afmeting_hoogte

        if request.method == "POST":
            producten = request.POST.getlist('producten[]')
            if ('afmetingen' not in request.POST):
                bestelling.producten.clear()
                for productName in producten:
                    product = Producten.objects.get(naam=productName)
                    if product is not None:
                        bestelling.producten.add(product)

                bestelling.save()
            else:
                form = AfmetingenForm(request.POST)
                
                if (form.is_valid):                
                    kamer.afmeting_breedte = int(request.POST['breedte'])
                    kamer.afmeting_lengte  = int(request.POST['lengte'])
                    kamer.afmeting_hoogte  = int(request.POST['hoogte'])
                    kamer.save()

        oppervlakte = kamer.berekenOppervlakte()
        productList = []
        for productItem in Producten.objects.all():
            if (oppervlakte > productItem.afmeting_oppervlakte):
                productList.append(productItem)
                if (bestelling.producten.filter(naam=productItem).exists()):
                    productItem.checked = "checked"
                else:
                    productItem.checked = ""

                oppervlakte = oppervlakte - productItem.afmeting_oppervlakte

        return render(request, "pages/inrichten.html",{
            "form" : form,
            "producten" : productList
        })
    else:
        return render(request, "pages/login.html")

def afgerond(request):
    return render(request, "pages/afgerond.html")

def bestellen(request):
    return render(request, "pages/bestellen.html")    

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
            print(username)
            print(email)
            user = User.objects.create_user(username, email, password)            
            user.save()
            
        except IntegrityError as e: 
            print("error: ")
            print(e)
            return render(request, "pages/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pages/register.html")

