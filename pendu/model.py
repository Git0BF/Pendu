# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:34:22 2023
On recupere le mot à trouver ici
a partir d'un dictionaire de mot on choisis un random
mais on doit utiliser tt la liste.
@author: Utilisateur
"""
import random

def charger_lexique():
    with open("dictionaire.txt", "r") as f:
        mots = f.read().splitlines()
    return [mot.upper() for mot in mots]

def choisir_mot(mots):
    return random.choice(mots)

#mots = charger_lexique()
#mot_a_trouver = choisir_mot(mots)
#print(mot_a_trouver)
