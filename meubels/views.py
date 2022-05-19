from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django import forms
from .models import *

def index(request):    
    return render(request, "pages/index.html")

def product(request):
    return render(request, "pages/product.html")

def kamer_inrichten(request):
    return render(request, "pages/inrichten.html")

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
            user = User.objects.create_user(username, email, password)
            UserWatchlist.objects.create(user=user)
            user.save()
        except IntegrityError:
            return render(request, "pages/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pages/register.html")

