# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 11:57:43 2023

@author: Utilisateur
"""
import view
import controller
import model

if __name__ == "__main__":
    mots = model.charger_lexique()
    mot_a_trouver = model.choisir_mot(mots)
    jeu = controller.init_jeux(mot_a_trouver)

    while not controller.jeux_complet(jeu) and jeu["erreurs_restantes"] > 0:
        view.afficher_jeux(jeu)
        lettre = input("Saisir une lettre: ")
        trouvee = controller.jouer_car(jeu, lettre)
        if not trouvee:
            print("La lettre", lettre, "n'est pas dans le mot.")
            print("Il vous reste", jeu["erreurs_restantes"], "erreurs.")

    if controller.jeux_complet(jeu):
        print("Félicitations, vous avez gagné!Le mot était bien", jeu["mot"])
    else:
        print("Désolé, vous avez perdu. Le mot était", jeu["mot"])

