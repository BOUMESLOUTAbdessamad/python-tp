# coding=utf-8
"""
 Application de l'algorithme MINIMAX sur le TIC-TAC-TOE
 L'IA joue contre un joueur phisique et utilise l'algorithme
 pour définir quelle est le meilleur coup à jouer

 L'IA commence toujour le jeu suivant ce code mais il est
 possible de le modifier afin de demander au joueur s'il souhaite
 commencer ou laisser l'IA commencer.

 La table de jeu est représenté suivant un tableau de 9 case.
 Elle est représenté suivant ce schéma :
                      1  2  3
                      4  5  6
                      7  8  9
"""

#################################################################
# Affichage de l'état de la table de jeu
#################################################################
def affiche_table(table):
    print(table[1] + '|' + table[2] + '|' + table[3] + '     1, 2, 3 ')
    print('-+-+-')
    print(table[4] + '|' + table[5] + '|' + table[6] + '     4, 5, 6 ')
    print('-+-+-')
    print(table[7] + '|' + table[8] + '|' + table[9] + '     7, 8, 9 ')
    print("\n")

#################################################################
# Vérifier si oui ou non une position dans la table est libre
#################################################################
def position_libre(table, position):
    if table[position] == ' ':
        return True
    else:
        return False

#################################################################
# insérer le marqueur X ou O dans la table
#################################################################
def inserer_marqueur(table, marqueur, position):
    if position_libre(table, position):  # si la position est libre
        table[position] = marqueur  # insertion du marqueur donné
        affiche_table(table)  # afficher l'état de la table
        if (table_rempli(table)):  # si la table est rempli
            print("Table Remplis! ")
            exit()
        if verifier_si_jeu_gagnant(table):  # si c'est un coup gangant
            if marqueur == 'X':
                print("l'IA a gangé!")
                exit()
            else:
                print("Le joueur à gagner!")
                exit()

        return
    else:
        print("position déjà utilisée !")  # position non libre
        position = int(input("Donnez une autre position :  "))
        inserer_marqueur(table, marqueur, position)  # rappel de la fonction
        return

#################################################################
# Vérifier si un coup est gangant (quelque soit le joueur)
#################################################################
def verifier_si_jeu_gagnant(table):
    if (table[1] == table[2] and table[1] == table[3] and table[1] != ' '):
        return True
    elif (table[4] == table[5] and table[4] == table[6] and table[4] != ' '):
        return True
    elif (table[7] == table[8] and table[7] == table[9] and table[7] != ' '):
        return True
    elif (table[1] == table[4] and table[1] == table[7] and table[1] != ' '):
        return True
    elif (table[2] == table[5] and table[2] == table[8] and table[2] != ' '):
        return True
    elif (table[3] == table[6] and table[3] == table[9] and table[3] != ' '):
        return True
    elif (table[1] == table[5] and table[1] == table[9] and table[1] != ' '):
        return True
    elif (table[7] == table[5] and table[7] == table[3] and table[7] != ' '):
        return True
    else:
        return False

#################################################################
# Vérifier quel joeur à gangé lors de la recherche minimax (suivant le marqueur X ou O)
#################################################################
def verifier_quel_joueur_gagne(table, marqueur):
    if table[1] == table[2] and table[1] == table[3] and table[1] == marqueur:
        return True
    elif (table[4] == table[5] and table[4] == table[6] and table[4] == marqueur):
        return True
    elif (table[7] == table[8] and table[7] == table[9] and table[7] == marqueur):
        return True
    elif (table[1] == table[4] and table[1] == table[7] and table[1] == marqueur):
        return True
    elif (table[2] == table[5] and table[2] == table[8] and table[2] == marqueur):
        return True
    elif (table[3] == table[6] and table[3] == table[9] and table[3] == marqueur):
        return True
    elif (table[1] == table[5] and table[1] == table[9] and table[1] == marqueur):
        return True
    elif (table[7] == table[5] and table[7] == table[3] and table[7] == marqueur):
        return True
    else:
        return False

#################################################################
# Vérifier si la table de jeu est remplie
#################################################################
def table_rempli(table):
    for position in table.keys():  # pour toutes les positions
        if (table[position] == ' '):  # si une seul est libre
            return False
    return True

#################################################################
# tour du joueur physique
#################################################################
def jeu_joueur(table):
    position = int(input("Donnez une position:  "))
    inserer_marqueur(table, 'O', position)
    return

#################################################################
# tour de l'IA
#################################################################
def jeu_IA(table):
    meilleur_score = -800  #
    meilleur_position = 0
    for position in table.keys():  # parcours de la table entière
        if (table[position] == ' '):  # si une position est libre
            table[position] = 'X'  # On pose un X dans cette position libre
            # L'algorithme par de ce coup et cherche à savoir si c'est le meilleur
            # coup à jouer en parcourant toutes les possiblités par la suite
            score = minimax(table, False)  # Le prochain coup sera pour le joueur
            # d'où le False  (voir la fct minimax)
            table[position] = ' '  # On remet la position à son état libre
            if (score > meilleur_score):  # si le score est meilleur que l'initial
                meilleur_score = score  # on le prend comme score final
                meilleur_position = position  # on décide que c'est le meilleur coup à jouer

    inserer_marqueur(table, 'X', meilleur_position)  # insertion dans la meilleur position trouvée
    return

#################################################################
# Fonction à développer ...
# L'IA cherche à maximiser son score
# et à minimiser le score du joueur physique
#################################################################
def minimax(table, si_maximisation):
    return 1
    """ 
    Pour le coup joué lors du choix d'une place libre dans la fct "jeu_IA" on va parcourir la suite
    des coups à jouer et voir si cela est favorable à l'IA ou au joueur  
    En résumé, on parcours toute l'arborésence du jeu 
    """
    # Si le coup ne fait gagner ni l'IA ni le Joueur ni fini dans un état nul alors on continue à jouer

    ########################################
    ########################################
    ########################################
    ########################################
    ########################################
    ########################################
    #### DEVELOPPEZ VOTRE CODE ICI #########
    ########################################
    ########################################
    ########################################
    ########################################
    ########################################
    ########################################

#################################################################
# Main ##########################################################
#################################################################
if __name__ == '__main__':

    # définition d'une table avec ses clés de 1 à 9 suivant le schéma prédéfini

    table = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    affiche_table(table)  # Affichage de la table à l'état initiale avec les clé de chaque position
    print("\n")
    print('Vous jouez contre une IA, elle utilise le  "X" et vous le "O" :')
    print('L"IA commence ----- ')

    while not verifier_si_jeu_gagnant(table):  # répéter tant qu'il n'y a pas de gagnant
        jeu_IA(table)  # l'IA commence
        jeu_joueur(table)

