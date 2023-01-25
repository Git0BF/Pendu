# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:37:23 2023
comparer la lettre saisie :
    jouer un caractère jouer_car()
    jeux complet ? jeux_complet()
    Il ya zero erreur au départ init_jeux() 
@author: Utilisateur
"""


def init_jeux(mot):
    jeu = {"mot": mot, "lettres_trouvees": [], "erreurs_restantes": 6}
    return jeu


def jouer_car(jeu, lettre):
    lettre = lettre.upper()
    for l in jeu["mot"]:
        if l == lettre:
            jeu["lettres_trouvees"].append(l)
            return True
    jeu["erreurs_restantes"] -= 1
    return False


def jeux_complet(jeu):
    return set(jeu["mot"]) == set(jeu["lettres_trouvees"])


#if __name__ == "__main__":
 # T  mot = "python"
  #  jeu = init_jeux(mot)
  #  print(jeu)
if __name__ == "__main__":
    mot = "python"
    jeu = init_jeux(mot)
    lettre = input("Saisir une lettre: ")
    trouvee = jouer_car(jeu, lettre)
    if trouvee:
        print("La lettre", lettre, "a été trouvée.")
    else:
        print("La lettre", lettre, "n'a pas été trouvée.")
