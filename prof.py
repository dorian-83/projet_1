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
    Ce programme est appelÃ© avec le nom d'un fichier sur la ligne de commande,
    ce fichier contenant des listes de type L.
    Il sort la profondeur de chaque liste.
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
    if n==0:
        print(f"{l=}")
        print(f"{profondeur(l)=}")
    else:
        for i in l:
            L=i
            print(f"{L=}")
            print(f"{profondeur(L)=}")
