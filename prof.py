#!/bin/env python3
import sys
import re
from module import construire
from module import build
from module import mklist
from module import llist
from module import interact

"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  

    si aucun argument n'est fourni sur la ligne de commande, alors les listes sont demandées interactivement à l’ut>

    sinon, si 1 argument unique est fourni sur la ligne de commande, alors c’est le nom du fichier dans lequel sero>

    sinon les arguments fournissent la liste à traiter.


    Ce programme donnera la profondeur des listes traitées

"""

def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passÃ©e en argument.
    """

    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

"""
PROGRAMME PRINCIPAL
"""


if __name__=="__main__":
    l,n=interact()
    if n==-1:
        print("le document est vide")
    elif n==0:
        print(f"{l=}")
        print(f"{profondeur(l)=}")
        assert profondeur(l)>0,"la profondeur est négative"
    else:
        for i in l:
            L=i
            print(f"{L=}")
            print(f"{profondeur(L)=}")
            assert profondeur(l)>0,"la profondeur est négative"
