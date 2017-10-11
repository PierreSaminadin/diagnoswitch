#!/usr/bin/env python
# -*- coding: utf-8 -*-

class oErrEquipement:
    """un équipement pour la fonctionnalité de décompte des erreurs"""
    def __init__(self, pIndex):
        self.aIndex = pIndex
        self.aPorts = {}
        # liste des collectes
        self.aListeCollectes = []

class oErrPort:
    """un port, ses OID et ses collectes"""
    def __init__(self, pPortNum):
        self.aPortNum = pPortNum
        self.aListeOIDs = ["1.3.6.1.2.1.10.7.2.1.2.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.3.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.4.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.5.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.6.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.7.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.8.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.9.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.10.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.11.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.13.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.16.{}".format(self.aPortNum),
                           "1.3.6.1.2.1.10.7.2.1.18.{}".format(self.aPortNum)]
        self.aCollectes = {}

class oErrCollecte:
    """un enregistrement d'une collecte pour un port"""
    def __init__(self, pNom):
        self.aNom = pNom
        self.aDonnees = {}

if __name__ == "__main__":
    
    import os
    import shelve

    """générer une collecte"""
    from inventaire import oInventaire
    from inventaire import oEquipement
    
    #############################################################
    # générer un fichier d'inventaire
    ###########################################################

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
    vSwitchCourant = len(vInventaire.aListe) - 1

    # sauvegarde de l'objet
    ikea = shelve.open("inventaire.shlv")
    ikea["inventaire"] = vInventaire
    ikea.close()

    ###########################################
    # ajouter le switch dans CompteurErreurs et sauvegarder
    ############################################

    if os.path.isfile("CompteursErreur.shlv"):
        ikea = shelve.open("CompteursErreur.shlv")
        vCompteursErr = ikea["CompteursErreur"]
        ikea.close()
    else:
        vCompteursErr = {}
        ikea = shelve.open("CompteursErreur.shlv")
        ikea["CompteursErreur"] = vCompteursErr
        ikea.close()

    vCompteursErr[vSwitchCourant] = oErrEquipement(vSwitchCourant)
    
    # sauvegarde de l'objet
    ikea = shelve.open("CompteursErreur.shlv")
    ikea["CompteursErreur"] = vCompteursErr
    ikea.close()


