#!/bin/env python3
import sys
import re
from module import construire
from module import build
from module import mklist
from module import llist
#from module import interact

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
    if len(sys.argv)==1:         #aucun argument: liste demandée interactivement
        while True:
            line = input("? ").rstrip("\n").strip()
            if line=="":
                break
            lline = re.split(r' +',line.rstrip("\n"))
            i = 0
            l=mklist(lline,0)
            if llist(l):
                print(f"{l=}")
                print(f"{profondeur(l)=}")
            else:
                l=l[0]
                print(f"{l=}")
                print(f"{profondeur(l)=}")
    elif len(sys.argv)==2:
        f = open(sys.argv[1], "r")
        for line in f:
            lline = re.split(r' +',line.rstrip("\n"))
            l = build(lline)
            print(f"{l=}")
            print(f"{profondeur(l)=}")
    else:
        l=construire()
        print(f"{l=}")
        print(f"{profondeur(l)=}")

