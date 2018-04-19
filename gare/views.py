from django.shortcuts import render
from .models import GarePubblicate

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'gare/index.html', {})

def gare_list(request):
    #from firebase import firebase
    GarePubblicate.objects.all().delete()

    import pyrebase
    import datetime

    config = {
      "apiKey": "AIzaSyAecCiVjizFOWgZM4KuSpdzDcyyEw1MBl0",
      "authDomain": "bandigare-8096d.firebaseapp.com",
      "databaseURL": "https://bandigare-8096d.firebaseio.com",
      "storageBucket": "bandigare-8096d.appspot.com",
      "serviceAccount": ""
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    results = db.child("gare").get()
    #print(results.val())
    result = results.val()

    list_gare = []



    for uno in result:
        
        dataPubblicazione = '1900-01-01'
        if result[uno]['DATA_PUBBLICAZIONE']> 0:
          dataPubblicazione = datetime.datetime.fromtimestamp(int(result[uno]['DATA_PUBBLICAZIONE'])).strftime('%Y-%m-%d')

        dataInserimento = '1900-01-01'
        if result[uno]['DATA_INSERIMENTO']>0:
          dataInserimento = datetime.datetime.fromtimestamp(int(result[uno]['DATA_INSERIMENTO'])).strftime('%Y-%m-%d')


        dataScadenza = '1900-01-01'
        if result[uno]['DATA_SCADENZA']>0:
          dataScadenza = datetime.datetime.fromtimestamp(int(result[uno]['DATA_SCADENZA'])).strftime('%Y-%m-%d')

        #print >>sys.stderr, 'Goodbye, cruel world!'

        #print (result[uno])
        singol_gare =  GarePubblicate(IDEN = result[uno]['ID'],
                                      IDFIREBASE = uno,
                                      IDENTIFICATIVO_GARA = result[uno]['IDENTIFICATIVO_GARA'],
                                      OGGETTO =   result[uno]['OGGETTO'],
                                      CIG = result[uno]['CIG'],
                                      TIPOLOGIA = result[uno]['TIPOLOGIA'],
                                      PROCEDURA = result[uno]['PROCEDURA'],
                                      ENTE = result[uno]['ENTE'],
                                      CITTA = result[uno]['CITTA'],
                                      PROVINCIA = result[uno]['PROVINCIA'],
                                      REGIONE = result[uno]['REGIONE'],
                                      IMPORTO = result[uno]['IMPORTO'],
                                      DATA_PUBBLICAZIONE = dataPubblicazione,
                                      DATA_INSERIMENTO = dataInserimento,
                                      DATA_SCADENZA = dataScadenza,
                                      CATEGORIA_PREVALENTE = result[uno]['CATEGORIA_PREVALENTE'],
                                      CATEGORIE_SCORPORABILI = result[uno]['CATEGORIE_SCORPORABILI'],
                                      CPV = result[uno]['CPV'],
                                      PROVENIENZA = result[uno]['PROVENIENZA'],
                                      DOWNLOAD = result[uno]['DOWNLOAD'],
                                      INFO_AGGIUNTIVE = result[uno]['INFO_AGGIUNTIVE'],
                                      )
        list_gare.append(singol_gare)

    GarePubblicate.objects.bulk_create(list_gare)
    return render(request, 'gare/gare_list.html', {})


def simple_search(request):
  return render(request, 'gare/simple_search.html', {})