#!/usr/bin/env python
# -*- coding: utf-8 -*-

# script de validation des fonctions et de la structure de données
# pour tester, supprimer les fichiers "inventaire.shlv"
# et "CompteursErreur.shlv"


if __name__ == "__main__":
    
    import os
    import shelve

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

    # verifier l'existence du fichier de compteur d'erreurs
    # et le charger dans la variable vCompteursErr
    if os.path.isfile("CompteursErreur.shlv"):
        ikea = shelve.open("CompteursErreur.shlv")
        vCompteursErr = ikea["CompteursErreur"]
        ikea.close()
    else:
        vCompteursErr = {}
        ikea = shelve.open("CompteursErreur.shlv")
        ikea["CompteursErreur"] = vCompteursErr
        ikea.close()

    # ajouter un enregistrement dans vCompteursErr
    # sous la forme d'un objet "oErrEquipement"
    vCompteursErr[vSwitchCourant] = oErrEquipement(vSwitchCourant)

    # ajouter un port 
    # c'est un attribut de l'équipement
    # sous la forme d'un objet "oErrPort"
    vCompteursErr[vSwitchCourant].aPorts[4] = oErrPort(4)
    
    # rasembler les infos pour la collecte
    vAdresseIP = vInventaire.aListe[vSwitchCourant].aAdresseIP
    vCommunaute = vInventaire.aListe[vSwitchCourant].aCommunaute
    print(vAdresseIP, vCommunaute)
    ## en particulier la liste des OID de ce ports
    ## cette liste est un attribut du port
    vListeOID = vCompteursErr[vSwitchCourant].aPorts[4].aListeOIDs
    print(vListeOID)

    # effectuer la collecte
    # on appelle la fonction fListeCompteurs
    vResultats = fListeCompteurs(vAdresseIP, vCommunaute, vListeOID)
    print(vResultats)

    # nommer la collecte "C1", clé du dictionnaire
    # et générer un objet oErrCollecte
    vCompteursErr[vSwitchCourant].aPorts[4].aCollectes["C1"] = oErrCollecte("C1")
    # simplifier la référence à l'objet 
    # et à l'attribut "aDonnees"
    aCollecteEnCours = vCompteursErr[vSwitchCourant].aPorts[4].aCollectes["C1"].aDonnees
    
    # parcourir "vResultats" et sauvegarder dans aCollecteEnCours
    for cle, valeur in vResultats.items():
        aCollecteEnCours[cle] = valeur
    print(aCollecteEnCours)

    


    # sauvegarde de l'objet
    ikea = shelve.open("CompteursErreur.shlv")
    ikea["CompteursErreur"] = vCompteursErr
    ikea.close()

