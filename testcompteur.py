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


class TestCompteur(unittest.TestCase):
    def test_oid1(self):
        warnings.simplefilter("ignore")
        lResult = fCompteur(ip,com,OID)
        self.assertEqual(lResult, "arwlab-sw-150", "le nom de ce switch devrait être arwlab-sw-150")

class TestMauvaiseCommunaute(unittest.TestCase):
    def test_oid1(self):
        warnings.simplefilter("ignore")
        lResult = fCompteur(ip,"nimportequoi",OID)
        lReponse = ('No SNMP response received before timeout',)
        self.assertEqual(lResult, lReponse, "attendu : timeout SNMP")

if __name__ == "__main__":
    unittest.main()



