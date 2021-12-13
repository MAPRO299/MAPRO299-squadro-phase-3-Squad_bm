import squadro
import api

def main():
    commands = squadro.traiter_la_ligne_de_commande().__dict__

    if commands['parties'] == True:
        parties = api.lister_les_parties(commands['IDUL'])
        print(squadro.formatter_les_parties(parties))
    else:
        api.créer_une_partie(commands['IDUL'])

        id, prochain_joueur, état = api.créer_une_partie(commands['IDUL'])
        squadro.afficher_le_plateau_de_jeu(état)

        while True:
            pion = input("Quel pion voulez-vous bouger?")
            état = api.jouer_un_coup(id, prochain_joueur, pion)['état']
            squadro.afficher_le_plateau_de_jeu(état)
            
main()