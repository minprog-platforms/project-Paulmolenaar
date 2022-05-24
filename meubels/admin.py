from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Producten)
admin.site.register(Categorie)
admin.site.register(Bestellingen)
admin.site.register(KamerAfmetingen)
admin.site.register(User)