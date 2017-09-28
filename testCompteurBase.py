#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    
    import os
    import shelve

    """générer une collecte"""
    from inventaire import oInventaire
    from inventaire import oEquipement
    from CompteursErreur import oErrEquipement
    from CompteursErreur import oErrPort
    from CompteursErreur import oErrCollecte
    from compteur import fCompteur
    from compteur import fListeCompteurs

    
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

    # ajouter un port 
    vCompteursErr[vSwitchCourant].aPorts[4] = oErrPort(4)
    
    # rasembler les infos pour la collecte
    vAdresseIP = vInventaire.aListe[vSwitchCourant].aAdresseIP
    vCommunaute = vInventaire.aListe[vSwitchCourant].aCommunaute
    print(vAdresseIP, vCommunaute)
    vListeOID = vCompteursErr[vSwitchCourant].aPorts[4].aListeOIDs
    print(vListeOID)
    vResultats = fListeCompteurs(vAdresseIP, vCommunaute, vListeOID)
    print(vResultats)


    # sauvegarde de l'objet
    ikea = shelve.open("CompteursErreur.shlv")
    ikea["CompteursErreur"] = vCompteursErr
    ikea.close()

