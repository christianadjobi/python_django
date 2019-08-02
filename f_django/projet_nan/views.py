from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse
import json

from requests import get
from bs4 import BeautifulSoup

def match(request):
    return render(request, 'projet_nan/match.html')

def home(request):

    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """

    return HttpResponse("""

        <h1>Bienvenue sur mon blog !</h1>

        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>

    """)

def articles(request):

    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """

    return HttpResponse("""

        <h1>Première article </h1>

        <p>Soyez attentifs !!!</p>

    """)

 #def date_actuelle(request):
     #return render(request, 'projet_nan/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'projet_nan/addition.html', locals())

def date_actuelle(request):

    url = 'https://www.matchendirect.fr/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs = {'id':'livescore'}) 
    compt = 1

    mydata = []


    for row in table.findAll('div', attrs = {'class':'panel panel-info'}): 


        a_desc = row.find('h3', attrs = {'class':'panel-title'}).get_text() 

        for el in row.findAll('tr'):

            resultat = {}
            heure = el.find('td', attrs = {'class':'lm1'}).get_text() 
            eqA = el.find('span', attrs = {'class':'lm3_eq1'}).get_text()
            eqB =  el.find('span', attrs = {'class':'lm3_eq2'}).get_text()

            scors =  el.find('span', attrs = {'class':'lm3_score'}).get_text()

            resultat['heure'] = heure
            resultat['eqa'] = eqA
            resultat['eqb'] = eqB
            resultat['scors'] = scors

            mydata.append(resultat)

    data = mydata
    
    return render(request, 'projet_nan/resultat.html', {'result': data}) # retourn du json
# Create your views here.
