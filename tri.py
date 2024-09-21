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
    l=interact()
    tri(l)
    print(f"{l=}")
