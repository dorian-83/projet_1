#!/bin/env python3
import sys
import re
from module_test import construire

"""
    Soit L le type liste dont les Ã©lÃ©ments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  

    Ce programme est appelÃ© avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.  

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit Ãªtre fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""
def mklist():
    global i
    l = []          # liste courante
    while True:
        if lline[i]=="[":   # c'est une liste de listes
            i+=1                 # argument suivant
            if i!=1:             # pour la premiÃ¨re liste, on ne fait rien
                l.append(mklist())    # sinon on construit cette sous-liste et on la met dans la liste courante
        elif lline[i]=="]": # c'est la fin de la liste,
            i+=1
            return l             # on renvoie la liste courante
        else:                  # c'est une liste d'entiers
            l.append(int(lline[i]))   
            i+=1


def minmax(l):
    """
    Cette fonction rÃ©cursive retourne le minmax de la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    if len(sys.argv)==1:         #aucun argument: liste demandée interactivement
            while True:
                line = input("? ").rstrip("\n").strip()
                if line=="":
                    break
                lline = re.split(r' +',line.rstrip("\n"))
                i = 0
                l = mklist()                      # rÃ©cupÃ©ration de la liste
                maxi = []
                minmax(l)
                print(f"{l=}")
                print(min(maxi))
    else:
        l=construire()
        maxi = []
        minmax(l)
        print(min(maxi))

   
