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

    si aucun argument n'est fourni sur la ligne de commande, alors les listes sont demandées interactivement à l’utilisateurs,

    sinon, si 1 argument unique est fourni sur la ligne de commande, alors c’est le nom du fichier dans lequel seront lues les listes (1 par ligne),

    sinon les arguments fournissent la liste à traiter.


    Ce programme donnera le minimum des maximum des listes traitées


    

"""


def minmax(l):
    print(l)
    """
    Cette fonction rÃ©cursive retourne le minmax de la liste passÃ©e en argument.
    """
    if type(l)==list:
        if type(l[0])==int:
            maxi.append(max(l))
        else:
            for i in l:
                minmax(i)

"""
PROGRAMME PRINCIPAL
"""


if __name__=="__main__":
    l,n=interact()
    if n==-1:
        print("le document est vide")
    elif n==0:
        maxi = []
        minmax(l)
        print(min(maxi))

    else:
        for i in l:
            maxi = []
            minmax(i)
            print(min(maxi))
   



