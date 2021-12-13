import re
import argparse

# traiter la ligne de commande
def traiter_la_ligne_de_commande():
    parser = argparse.ArgumentParser(description='Traiter la ligne de commande')
    parser.add_argument('IDUL', help='IDUL du ou des joueurs', nargs='+')
    parser.add_argument('-p', '--parties', help='Lister les 20 dernieres parties', action='store_true')

    return parser.parse_args()

#Formatage des parties
def formatter_les_parties(liste_parties): 
    liste_formattée = ""
    for i, partie in enumerate(liste_parties['parties']):
        liste_formattée += f"{i+1} : {partie['date']}"
        liste_formattée += f", {partie['joueurs'][0]} vs {partie['joueurs'][1]}"
        if partie['gagnant'] != None:
            liste_formattée += f", gagnant: {partie['gagnant']}"
        liste_formattée += '\n'

    return liste_formattée

#Afficher le plateau de jeu
def afficher_le_plateau_de_jeu(argliste):
    print('Légende:')
    print('  □ = ' + argliste[0]['nom'])
    print('  ■ = ' + argliste[1]['nom'] + '\n')
    Lignste =  ['       . | . : | : : | : : | : . | .',
                '         |   . | .   |   . | .   |',
                '  ...    |     |     |     |     |      .',
                '1 ───────┼─────┼─────┼─────┼─────┼───────',
                '  ...    |     |     |     |     |      .',
                '  .      |     |     |     |     |    ...',
                '2 ───────┼─────┼─────┼─────┼─────┼───────',
                '  .      |     |     |     |     |    ...',
                '   ..    |     |     |     |     |     ..',
                '3 ───────┼─────┼─────┼─────┼─────┼───────',
                '   ..    |     |     |     |     |     ..',
                '  .      |     |     |     |     |    ...',
                '4 ───────┼─────┼─────┼─────┼─────┼───────',
                '  .      |     |     |     |     |    ...',
                '  ...    |     |     |     |     |      .',
                '5 ───────┼─────┼─────┼─────┼─────┼───────',
                '  ...    |     |     |     |     |      .',
                '       . | .   |     |     |   . | .',
                '       : | : . | . : | : . | . : | :'
    ]
        
    # Ajout des pions:
    for i, position in enumerate(argliste[0]['pions']):
        if i == 0:
            y = 3
        if i == 1:
            y = 6
        if i == 2:
            y = 9
        if i == 3:
            y = 12
        if i == 4:
            y = 15
        if position == 0 or position == 12:
            x = 5
        if position == 1 or position == 11:
            x = 9
        if position == 2 or position == 10:
            x = 15
        if position == 3 or position == 9:
            x = 21
        if position == 4 or position == 8:
            x = 27
        if position == 5 or position == 7:
            x = 33
        if position == 6:
            x = 37
        if position < 6:
            Lignste[y] = re.split('', Lignste[y])
            Lignste[y][x] = '□□'
            Lignste[y][x+1] = ' '
            Lignste[y][x+2] = '○'
            Lignste[y][x+3] = ''
            Lignste[y] = ''.join(Lignste[y])
        if position >= 6 and position < 12:
            Lignste[y] = re.split('', Lignste[y])
            Lignste[y][x+2] = '□□'
            Lignste[y][x+1] = ' '
            Lignste[y][x] = '○'
            Lignste[y][x-1] = ''
            Lignste[y] = ''.join(Lignste[y])
        if position == 12:
            Lignste[y] = re.split('', Lignste[y])
            Lignste[y][x+3] = '□□'
            Lignste[y][x+2] = ' '
            Lignste[y][x+1] = '○'
            Lignste[y][x] = ''
            Lignste[y] = ''.join(Lignste[y])
        
    for i, position in enumerate(argliste[1]['pions']):
        if i == 0:
            x = 10
        if i == 1:
            x = 16
        if i == 2:
            x = 22
        if i == 3:
            x = 28
        if i == 4:
            x = 34
        if position == 0 or position == 12:
            y = 1
        if position == 1 or position == 11:
            y = 3
        if position == 2 or position == 10:
            y = 6
        if position == 3 or position == 9:
            y = 9
        if position == 4 or position == 8:
            y = 12
        if position == 5 or position == 7:
            y = 15
        if position == 6:
            y = 18
        
        if position < 6:
            Lignste[y] = re.split('', Lignste[y])
            Lignste[y+1] = re.split('', Lignste[y+1])
            Lignste[y][x] = '█'
            Lignste[y+1][x] = '●'
            Lignste[y] = ''.join(Lignste[y])
            Lignste[y+1] = ''.join(Lignste[y+1])
        if position == 6:
            Lignste[y-1] = re.split('', Lignste[y-1])
            Lignste[y-2] = re.split('', Lignste[y-2])
            Lignste[y-1][x] = '█'
            Lignste[y-2][x] = '●'
            Lignste[y-1] = ''.join(Lignste[y-1])
            Lignste[y-2] = ''.join(Lignste[y-2])
        if position == 12:
            Lignste[y+1] = re.split('', Lignste[y+1])
            Lignste[y] = re.split('', Lignste[y])
            Lignste[y+1][x] = '█'
            Lignste[y][x] = '●'
            Lignste[y+1] = ''.join(Lignste[y+1])
            Lignste[y] = ''.join(Lignste[y])
        if position > 6 and position < 12:
            Lignste[y] = re.split('', Lignste[y])
            Lignste[y-1] = re.split('', Lignste[y-1])
            Lignste[y][x] = '█'
            Lignste[y-1][x] = '●'
            Lignste[y] = ''.join(Lignste[y])
            Lignste[y-1] = ''.join(Lignste[y-1])
            
    for i in range(len(Lignste)):
        print(Lignste[i])