from datetime import datetime
import http.client, urllib.parse
from django.contrib.gis.measure import Distance, D
from geopy.distance import geodesic
import json
from .models import *

# Positionstack.om API settings
POS_STACK_KEY   = '0a49c3bb9f792478c704cf51c39340b4'

def calculateLength(coords_one, coords_two):
    # middels de geodesic library wordt het verschil in kilometers uitgerekend tussen de twee coördinaten

    return geodesic(coords_one, coords_two).km

def getCoords(location):

    # middels de API van api.positionstack.com kan een GPS-locatie opgehaald worden middels de plaatsnaam.
    
    # Doe een HTTP request naar de API om middels de (geheime) sleutel en plaatsnaam de GPS-locatie op te vragen.
    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': POS_STACK_KEY,
        'query': location,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    text = data.decode('utf-8')

    # de verkegen gegevens zijn beschreven in een JSON formaat. Deze wordt middels json.loads()
    # omgezet naar een object
    jsonObject = json.loads(text)

    # in dit object wordt de latitude en de longitude verkregen en doorgegeven.
    return [jsonObject['data'][0]['latitude'],jsonObject['data'][0]['longitude']]

def berekenMaanden(start_date: datetime , end_date: datetime) -> int:
    # in deze functie worden 2 parameters van het type datetime ontvangen
    # en wordt het verschil tussen deze (in maanden) uitgerekend.
 
    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    # voorkomen wordt dat het aantal negatief kan worden, dit omdat hierdoor een negatieve prijs zou ontstaan.
    if (num_months < 0):
        num_months = 0

    return num_months

def userKrijgLaatsteBestelling(user):
    geenBestellingGevonden = True

    bestelling = None

    try:
        # probeer bestelling op te halen van de gebruiker welke nog NIET is afgerond.
        bestelling = Bestellingen.objects.filter(user=user).filter(afgerond = False).first()
        
        if (bestelling != None):
            geenBestellingGevonden = False
    except Bestellingen.DoesNotExist:
        geenBestellingGevonden = True
    except Exception:
        geenBestellingGevonden = True

    # wanneer dit mislukt (geenBestellingGevonden == True), dan wordt een nieuwe bestelling aangemaakt 
    # voor de gebruiker.
    if (geenBestellingGevonden):
        bestelling = Bestellingen.objects.create(user=user, afgerond = False)

    return bestelling