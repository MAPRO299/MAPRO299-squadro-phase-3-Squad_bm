import json
import httpx


URL = 'https://pax.ulaval.ca/squadro/api2/'


#Liste des parties
def lister_les_parties(iduls):
    rep = httpx.get(URL+'parties', params={'iduls' : iduls})

    if  rep.status_code == 200:
        return rep.json()
    if  rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    
#Récupération d'une partie.
def récupérer_une_partie(id_partie):
    rep = httpx.get(URL+'partie', params={'id' : id_partie})

    if  rep.status_code == 200:
        return rep.json()
    if  rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
    
#Création d'une partie.
def créer_une_partie(iduls): 
    rep = httpx.post(URL+'partie', json={'iduls' : iduls})

    if  rep.status_code == 200:
        return (rep.json()['id'], rep.json()['prochain_joueur'], rep.json()['état'])
    if  rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])

#Jouer un coup
def jouer_un_coup(id_partie, idul, pion):
    rep = httpx.put(URL+'jouer', json={'id' : id_partie, 'idul' : idul, 'pion' : pion})

    if  rep.status_code == 200:
        if rep.json()['gagnant'] != None:
            raise StopIteration('Gagnant :' + rep.json()['gagnant'])
        return rep.json()
    if rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])



        