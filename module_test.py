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

def mklist():
    i=0
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

#def arguments():                     
	#if len(sys.argv)==0
		
	#elif nom de fichier donné:
		
	#else la liste qu'on voudra traiter







