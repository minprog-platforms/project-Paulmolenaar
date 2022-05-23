from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Categorie(models.Model):
    naam = models.CharField(max_length=40)

    def __str__(self):
       return f"{self.naam}"

class Producten(models.Model):
    naam         = models.CharField(max_length=40)    
    beschrijving = models.CharField(max_length=1000)    
    categorie    = models.ForeignKey(Categorie, on_delete = models.PROTECT, related_name = "cat_product")
    afbeelding   = models.CharField(max_length=200)

    afmeting_breedte = models.IntegerField()
    afmeting_lengte  = models.IntegerField()
    afmeting_hoogte  = models.IntegerField()

    prijs    = models.FloatField() # prijs per maand
    voorraad = models.IntegerField()
    
    def __str__(self):
       return f"{self.naam}"

class Bestellingen(models.Model):
    user         = models.ForeignKey(User, on_delete = models.PROTECT)
    producten    = models.ManyToManyField(Producten, blank=True)

    adres_plaats        = models.CharField(max_length=80)
    adres_straat_nummer = models.CharField(max_length=80)
    adres_postcode      = models.CharField(max_length=20)

    datum        = models.DateTimeField()
    prijs_totaal = models.FloatField() # prijs per maand

    afgerond       = models.BooleanField()
    datum_afgerond = models.DateTimeField()


# producten
# product categorien
# bestellingen
