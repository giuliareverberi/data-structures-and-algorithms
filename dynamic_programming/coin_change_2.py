# -*- coding: utf-8 -*-
"""
Created on Sat May 17 12:06:41 2025

@author: giuli
"""

#La funzione ritorna il numero di combinazioni delle monete in coins
#per ottenere come somma il target (usando la programmazione dinamica)

def main(coins, target):
    
    n = len(coins)
    
    #Creo una matrice per memorizzare mano mano il numero di combinazioni, dove
    #combinazioni[i][t] = # modi per ottenere somma t usando "i" tipi di monete     
    combinazioni = [[0] * (target + 1) for _ in range(n + 1)]
    
    #Il caso base è con t = 0:
    #per ogni i, ho solo una possibile combinazione, cioè prendere 0 monete
    for i in range(n + 1):
        combinazioni[i][0] = 1
    
    #Riempio la matrice 
    #i = quanti tipi di monete in coins sto considerando (va da 1 a n)   
    for i in range(1, n + 1):
        coin = coins[i - 1]
        
        #t = somma che voglio ottenere usando in totale "i" tipi di monete
        for t in range(target + 1):
            
            #Se non uso la i-esima moneta,
            #ho tutte le combinazioni con i-1 monete
            combinazioni[i][t] = combinazioni[i - 1][t]
            
            #Se invece la uso,  
            #rimane t - coin da comporre con gli stessi "i" tipi
            if t >= coin:
                combinazioni[i][t] += combinazioni[i][t - coin]
    
    #ritorno l'ultimo elemento della matrice,
    #cioè quello in cui ho considerato tutte le monete in coins 
    #e il target dato in input
    return combinazioni[n][target]  

             