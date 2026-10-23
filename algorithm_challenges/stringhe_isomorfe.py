# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 11:42:59 2025

@author: giuli
"""



def main(s, t):
    
    #non può esserci una corrispondenza tra tutte le lettere se le lunghezze delle parole sono diverse
    if len(s) != len(t):
        return False
    
    #dizionario per memorizzare le associazioni tra le lettere
    associazioni = {} 
    
    #set per memorizzare le lettere di t già usate
    usate = set()
    
    for i in range(len(s)): #itero su tutti i caratteri di s
        
        if s[i] not in associazioni: #se è la prima volta che considero quel carattere di s:
            
            #controllo che il carattere di t che dovrebbe essere il suo corrispondente non sia già associato a un altro di s
            if t[i] in usate: 
                return False
            
            #se non lo è allora aggiorno il dizionario e segno il carattere di t come usato
            else: 
                associazioni[s[i]] = t[i]
                usate.add(t[i])
                
        #se invece l'ho già considerato, 
        #controllo se il carattere di t che dovrebbe essere il suo corrispondente non è diverso da quello a cui era stato associato precedentemente  
        else: 
            if t[i] != associazioni[s[i]]:
                return False
        
    return True

