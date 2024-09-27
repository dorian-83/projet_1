#!/bin/env python3

import re
import sys

def construire():
    def _construire():
        """
        Cette fonction rÃ©cursive construit la liste 
        Ã  partir des arguments fournis sur la ligne de commande.
        Elle retourne la liste construite.
        """

        nonlocal i  
        l = []          
        while True:
            if sys.argv[i]=="[":   
                i+=1               
                if i!=2:                  # pour la premiÃ¨re liste, on ne fait rien
                    l.append(_construire()) 
            elif sys.argv[i]=="]":        # c'est la fin de la liste,
                i+=1
                return l                  # on renvoie la liste constuite
            else:                         # c'est une liste d'entiers
                l.append(int(sys.argv[i]))   
                i+=1
    i = 1                              # indice pour parcourir les arguments
    return _construire()

def build(l0):
    def _build():
        nonlocal i
        l = []          # sous-liste courant
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1
                if i!=1:             # pour la premiÃ¨re sous-liste, on ne>
                    l.append(_build())    # sinon on construit cette sous->
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))
                i+=1
    i = 0
    res = _build()
    return res

"""
liste demandée interactivement
"""

def mklist(L,i):
        l = []       # liste courante
        while True:
            if L[i]=="[":   # c'est une liste de listes
                i+=1                 # argument suivant
                if i!=1:             # pour la premiÃ¨re liste, on ne fait rien
                    l.append(mklist(L,i)[0])    # sinon on construit cette sous-liste et on la met dans la liste courante
                    i=i+mklist(L,i)[1]+1
            elif L[i]=="]": # c'est la fin de la liste,
                i+=1
                return l,len(l)
            else:                  # c'est une liste d'entiers
                l.append(int(L[i]))
                i+=1
                
def llist(obj):
    # Vérifie que l'objet est une liste
    if isinstance(obj, list):
        # Vérifie que chaque élément de la liste est aussi une liste
        return all(isinstance(elem, list) for elem in obj)
    return False  





def interact():
    n=0
    if len(sys.argv)==1:         #aucun argument: liste demandée interactivement
        while True:
            line = input("? ").rstrip("\n").strip()
            if line=="":
                break
            lline = re.split(r' +',line.rstrip("\n"))
            i = 0
            l=mklist(lline,0)
            if llist(l):
                return l,n
            else:
                l=l[0]
                return l,n
    elif len(sys.argv)==2:
        f = open(sys.argv[1], "r")
        L=list()
        for line in f:
            n+=1
            lline = re.split(r' +',line.rstrip("\n"))
            l = build(lline)
            L.append(l)
        if L==[]:
            return L,-1
        else:
            return L,n
    else:
        l=construire()
        return l,n

