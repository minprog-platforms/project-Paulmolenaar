from datetime import datetime
import http.client, urllib.parse
from django.contrib.gis.measure import Distance, D
from geopy.distance import geodesic
import json
from .models import *

# Positionstack.om API settings
POS_STACK_KEY   = '0a49c3bb9f792478c704cf51c39340b4'

def calculateLength(coords_one, coords_two):
    return geodesic(coords_one, coords_two).km

def getCoords(location):

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

    jsonObject = json.loads(text)
    return [jsonObject['data'][0]['latitude'],jsonObject['data'][0]['longitude']]

def berekenMaanden(start_date: datetime , end_date: datetime) -> int:
    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    if (num_months < 0):
        num_months = 0
    return num_months

def userKrijgLaatsteBestelling(user):
    geenBestellingGevonden = True

    bestelling = None

    try:
        bestelling = Bestellingen.objects.filter(user=user).filter(afgerond = False).first()
        
        if (bestelling != None):
            geenBestellingGevonden = False
    except Bestellingen.DoesNotExist:
        geenBestellingGevonden = True
    except Exception:
        geenBestellingGevonden = True

    if (geenBestellingGevonden):
        bestelling = Bestellingen.objects.create(user=user, afgerond = False)

    return bestelling