#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shelve

class oInventaire:

    def __init__(self, pNomSite):
        self.aNomSite = pNomSite
        self.aListe = []
        # Dictionnaire pour évolutivite de l'objet
        self.aDic = {}

    def mAjoutSwitch(self, pAdresseIP, pCommunaute):
        """ajouter un equipement a l'inventaire"""
        lIndex = len(self.aListe)
        lNouveauSwitch = oEquipement(lIndex, pAdresseIP, pCommunaute)
        self.aListe.append(lNouveauSwitch)
        

class oEquipement:

    def __init__(self, pIndex, pAdresseIP, 
               pCommunaute = "public"):
        self.aIndex = pIndex
        self.aAdresseIP = pAdresseIP
        self.aCommunaute = pCommunaute
        self.aEtiquette = "equipement n° {}".format(pIndex)
    
    def __str__(self):
        return """\
index      : {} 
adresse IP : {} 
communauté : {}
étiquette  : {}
""".format(self.aIndex, self.aAdresseIP, self.aCommunaute, self.aEtiquette)


if __name__ == "__main__":
    # générer un fichier d'inventaire et sauvegarder les mesures
    
    vNomSite = "Lab_Courbevoie"
    # verifier l'existence du fichier d'inventaire
    # et le charger dans la variable vInventaire
    if os.path.isfile("inventaire.shlv"):
        ikea = shelve.open("inventaire.shlv")
        vInventaire = ikea["inventaire"]
        ikea.close()
    else:
        vInventaire = oInventaire(vNomSite)
        ikea = shelve.open("inventaire.shlv")
        ikea["inventaire"] = vInventaire
        ikea.close()

    # ajouter un switch
    vIP = "192.168.254.150"
    vCommunaute = "arwlab"
    vInventaire.mAjoutSwitch(vIP, vCommunaute)

    # sauvegarde de l'objet
    ikea = shelve.open("inventaire.shlv")
    ikea["inventaire"] = vInventaire
    ikea.close()


    
