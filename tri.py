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

    Ce programme lit des liste de type L sur l'entrÃ©e standard, au format
    [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
    et sort cette liste dans laquelle les sous-listes d'entiers sont triÃ©es.  
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
    if len(sys.argv)==1:         #aucun argument: liste demandée interactivement
        while True:
            line = input("? ").rstrip("\n").strip()
            if line=="":
                break
            lline = re.split(r' +',line.rstrip("\n"))
            i = 0
            l=mklist(lline,0)
            if llist(l):
                tri(l)
                print(f"{l=}")
            else:
                l=l[0]
                tri(l)
                print(f"{l=}")
    elif len(sys.argv)==2:
        f = open(sys.argv[1], "r")
        for line in f:
            lline = re.split(r' +',line.rstrip("\n"))
            l = build(lline)
            tri(l)
            print(f"{l=}")
    else:
        l=construire()
        tri(l)
        print(f"{l=}")
