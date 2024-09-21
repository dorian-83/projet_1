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

    Ce programme est appelÃ© avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.  

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit Ãªtre fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""



def minmax(l):
    """
    Cette fonction rÃ©cursive retourne le minmax de la liste passÃ©e en argument.
    """
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
    if n==0:
        maxi = []
        minmax(l)
        print(min(maxi))
    else:
        for i in l:
            maxi = []
            minmax(i)
            print(min(maxi))
   
