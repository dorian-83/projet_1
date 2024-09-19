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



#def arguments():                      #programme qui décide ce qui se passera en fonction du nombre d'arguments que l'on met
	#if len(sys.argv)==0
		
	#elif nom de fichier donné:
		
	#else la liste qu'on voudra traiter




if __name__=="__main__":
    # programme principal
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))


