#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
teste la fonction "compteur"
"compteur" va chercher la valeur d'un OID sur un switch
"""

from compteur import fCompteur
from compteur import fListeCompteurs


import unittest
import warnings

## variables de connexion
# communauté
com = "arwlab"
ip = "192.168.254.150"
# OID 1.3.6.1.2.1.1.1 - sysDescr 
OID = "1.3.6.1.2.1.1.5.0"



## tableau d'OID pour une interface
vListe = [
    "1.3.6.1.2.1.10.7.2.1.2.4",
    "1.3.6.1.2.1.10.7.2.1.3.4",
    "1.3.6.1.2.1.10.7.2.1.4.4",
    "1.3.6.1.2.1.10.7.2.1.5.4",
    "1.3.6.1.2.1.10.7.2.1.6.4",
    "1.3.6.1.2.1.10.7.2.1.7.4",
    "1.3.6.1.2.1.10.7.2.1.8.4",
    "1.3.6.1.2.1.10.7.2.1.9.4",
    "1.3.6.1.2.1.10.7.2.1.10.4",
    "1.3.6.1.2.1.10.7.2.1.11.4",
    "1.3.6.1.2.1.10.7.2.1.13.4",
    "1.3.6.1.2.1.10.7.2.1.16.4",
    "1.3.6.1.2.1.10.7.2.1.18.4"]

vListe2 = [
    "1.3.6.1.2.1.10.7.2.1.2.4",
    "1.3.6.1.2.1.10.7.2.1.3.4",
    "1.3.6.1.2.1.10.7.2.1.4.4",
    "1.3.6.1.2.1.10.7.2.1.5.4",
    "1.3.6.1.2.1.10.7.2.1.6.4",
    "1.3.6.1.2.1.10.7.2.1.7.4",
    "1.3.6.1.2.1.10.7.2.1.8.4",
    "1.3.6.1.2.1.10.7.2.1.9.4",
    "1.3.6.1.2.1.10.7.2.1.11.4",
    "1.3.6.1.2.1.10.7.2.1.14.4",
    "1.3.6.1.2.1.10.7.2.1.13.4",
    "1.3.6.1.2.1.10.7.2.1.16.4",
    "1.3.6.1.2.1.10.7.2.1.18.4"]


class TestListeCompteurs(unittest.TestCase):
    def testliste(self):
        """verifie que la fonction retourne une liste d'entiers"""
        warnings.simplefilter("ignore")
        lResult = fListeCompteurs(ip,com,vListe)
        lTest = True
        if not isinstance(lResult, dict):
            lTest = False
        else:
            for elem in lResult.values():
                if not isinstance(elem, int):
                    lTest = False
        self.assertTrue(lTest, "la fonction ne retourne pas une liste d'entiers")

    def testlisteCh(self):
        """cas ou il y a des OID injoignables"""
        warnings.simplefilter("ignore")
        lResult = fListeCompteurs(ip,com,vListe2)
        lTest = False
        if not isinstance(lResult, dict):
            lTest = False
        else:
            for elem in lResult.values():
                if elem == "No":
                    lTest = True
        self.assertTrue(lTest, "en cas dOID injoignable, certaines valeurs doivent être 'No'")

if __name__ == "__main__":
    unittest.main()



