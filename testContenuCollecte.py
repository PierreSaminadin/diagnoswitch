#!/usr/bin/env python
# -*- coding: utf-8 -*-

# visualisation de l'objet "Compteur erreurs"

import shelve

from inventaire import oInventaire
from inventaire import oEquipement
from CompteursErreur import oErrEquipement
from CompteursErreur import oErrPort
from CompteursErreur import oErrCollecte

# récupération de l'objet dans le fichier
ikea = shelve.open("CompteursErreur.shlv")
vCompteursErr = ikea["CompteursErreur"]
ikea.close()

# nombre d'équipements
print("\nNombre d'équipements : ", len(vCompteursErr), "\n")

# parcourir chauque équipement et afficher un résumé
for vNum in vCompteursErr:
    # simplification du nom de l'instance : 
    vPort = vCompteursErr[vNum].aPorts
    print("Equipement n° : ", vNum)
    print("Nombre de ports : ", len(vPort))
    print("")
    # parcourir chaque port
    for vNumPort in vPort:
        print("Nombre de collectes pour le port {} : {}"
              .format(vNumPort, len(vPort[vNumPort].aCollectes)))

# parcourir les équipements et afficher seulement les compteurs non nuls

vTableau = []
for vNum in vCompteursErr:
    # simplification du nom de l'instance : 
    vPort = vCompteursErr[vNum].aPorts
    # parcourir chaque port
    for vNumPort in vPort:
        # parcourir chaque collecte
        for vCollecte in vPort[vNumPort].aCollectes:
            # simplifier le nom du jeu de données
            vDonnes = vPort[vNumPort].aCollectes[vCollecte].aDonnees
            #parcourir chauque OID et retenir si non nul
            for vOID in vDonnes:
                if vDonnes[vOID] != 0:
                    vLigne = (vCollecte, vNumPort, vOID, vDonnes[vOID])
                    vTableau.append(vLigne)

print(vTableau)

