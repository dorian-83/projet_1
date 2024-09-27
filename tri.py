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


    Ce programme triera les listes contenues contenues a l'intérieur des listes traitées

"""

def tri(l):
    """
    Cette fonction rÃ©cursive tri la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

"""
PROGRAMME PRINCIPAL
"""

if __name__=="__main__":
    l,n=interact()
    if n==-1:
        print("le document est vide")
    elif n==0:
        tri(l)
        print(f"{l=}")
    else:
        for i in l:
            L=i
            tri(L)
            print(f"{L=}")
