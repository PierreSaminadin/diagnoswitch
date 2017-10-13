#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysnmp.hlapi import *


def fGetNext(pIp, pCom, pOid):
    """renvoie une liste de valeurs a la façon snmpwalk"""
    lResult = []
    se = SnmpEngine()
    cv2 = CommunityData(pCom, mpModel=1) # SNMPv2c
    t1 = UdpTransportTarget((pIp, 161))
    ot =ObjectType(ObjectIdentity(pOid))
    
    # définit un générator
    g = nextCmd(se, cv2, t1, ContextData(), ot, lexicographicMode=False)
    # place les résultats dans des variables
    for errorIndication, errorStatus, errorIndex, varBinds in g:

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
            # print(varBinds)
            for varBind in varBinds:
                oid = str(varBind[0])
                value = str(varBind[1])
                # print(value)
                lResult.append((oid,value))
    return lResult


if __name__ == "__main__":
    gIP = "192.168.254.150"
    gCom = "arwlab"
    gOid = "1.3.6.1.2.1.2.2.1.1"
    gTable = fGetNext(gIP, gCom, gOid)
    print(gTable)
    for bElem in gTable:
        print(bElem)
