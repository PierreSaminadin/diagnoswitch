#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *

def fCompteur(pIp, pCom, pOid):
    """renvoie la valeur d'un OID"""
    se = SnmpEngine()
    cv2 = CommunityData(pCom, mpModel=1) # SNMPv2c
    t1 = UdpTransportTarget((pIp, 161))
    ot =ObjectType(ObjectIdentity(pOid))
    
    # définit un générator
    g = getCmd(se, cv2, t1, ContextData(), ot)
    # place les résultats dans des variables
    errorIndication, errorStatus, errorIndex, varBinds = next(g)
    
    
    if errorIndication:
        return errorIndication.args
    elif errorStatus:
        print('fCompteur : %s at %s' % (
                            errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
                           )
             )

    # ici varBinds contient une donnée de type : 
    #  'SNMPv2-MIB::sysName.0 = arwlab-sw-150'
    else:
        lBrut = varBinds[0].prettyPrint()
        return lBrut.split()[2]

def fListeCompteurs(pIp, pCom, pOid):
    """renvoie une liste de valeurs - prend une liste d'OID en argument"""
    lResult = {}
    for lElem in pOid:
        lVal = fCompteur(pIp, pCom, lElem)
        # print("Oid #{}# - valeur #{}#".format(lElem, lVal))
        try:
            lVal = int(lVal)
        except ValueError:
            pass
        lResult[lElem] = lVal
    return lResult


