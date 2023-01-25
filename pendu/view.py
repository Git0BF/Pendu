# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:37:03 2023

On affiche le jeux ici, 
les lettres trouvés et les lettres manquantes.
on va utilise une liste de (lettre, boolean)
afficher(j)

@author: Utilisateur
"""


def afficher_jeux(jeu):
    for lettre in jeu["mot"]:
        if lettre in jeu["lettres_trouvees"]:
            print(lettre, end="")
        else:
            print("_", end="")
    print()


if __name__ == '__main__':
    j = [('p', True),('j', False)]
    afficher_jeux(j)

    
    