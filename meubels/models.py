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

    afmeting_breedte = models.IntegerField(default=0)
    afmeting_lengte  = models.IntegerField(default=0)
    afmeting_hoogte  = models.IntegerField(default=0)

    afmeting_oppervlakte = models.IntegerField(default=0)
    
    prijs    = models.FloatField() # prijs per maand
    voorraad = models.IntegerField()
    
    def berekenOppervlakte(self):
        self.afmeting_oppervlakte = self.afmeting_breedte * self.afmeting_lengte

    def save(self, *args, **kwargs):
        self.berekenOppervlakte()

        return super(Producten, self).save(*args, **kwargs)

    def __str__(self):
       return f"{self.naam}"

class Bestellingen(models.Model):
    user         = models.ForeignKey(User, on_delete = models.PROTECT)
    producten    = models.ManyToManyField(Producten, blank=True)

    adres_plaats        = models.CharField(max_length=80)
    adres_straat_nummer = models.CharField(max_length=80)
    adres_postcode      = models.CharField(max_length=20)
    
    datum        = models.DateTimeField(default='1970-01-01 00:00')
    prijs_totaal = models.FloatField(default=0) # prijs per maand

    afgerond       = models.BooleanField(default=False)
    datum_afgerond = models.DateTimeField(default='1970-01-01 00:00')


class KamerAfmetingen(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='afmetingen_user')  
    afmeting_breedte = models.IntegerField(default=0)
    afmeting_lengte  = models.IntegerField(default=0)
    afmeting_hoogte  = models.IntegerField(default=0)   
    afmeting_oppervlakte  = models.IntegerField(default=0)   

    def berekenOppervlakte(self):
        self.afmeting_oppervlakte = self.afmeting_breedte * self.afmeting_lengte
        return self.afmeting_oppervlakte

    def save(self, *args, **kwargs):
        self.berekenOppervlakte()

        return super(KamerAfmetingen, self).save(*args, **kwargs)

    def __str__(self):
        return 'Afmetingen %s' % (self.user)

# producten
# product categorien
# bestellingen
