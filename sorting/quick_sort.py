# -*- coding: utf-8 -*-
"""
Created on Mon May  5 16:54:00 2025

@author: giuli
"""

import random

def main(arr):    
    #ordina una lista di interi positivi usando Randomized QUick Sort
    
    r_quicksort(arr, 0, len(arr) - 1)
    return arr
    
def r_quicksort(A, p, r):   
    #Ordina l'array A dalla posizione p fino alla r
    
    #Se p>r, non devo ordinare
    if p < r:
        
        #Partiziona l'array e restituisce la posizione del pivot (che chiamo q)
        q = partition(A, p, r)
        
        #ordina ricorsivamente le due parti dell'array divise dal pivot
        r_quicksort(A, p, q - 1) #ordina parte sinistra
        r_quicksort(A, q + 1, r) #ordina parte destra

def partition(A, p, r):
    #Esegue la partizione dell'array scegliendo un pivot qualsiasi
    
    #Sceglie casualmente un pivot tra gli elementi dell'array
    indice_pivot = random.randint(p, r)
    pivot = A[indice_pivot]
    
    #Porta il pivot alla fine per semplificare il procedimento
    A[r], A[indice_pivot] = A[indice_pivot] , A[r]
    
    #i tiene traccia della fine della "zona" di numeri <= pivot 
    i = p - 1
    for j in range(p, r):
        
        #Gli elementi <= del pivot vanno a sinistra, gli altri a destra
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    #sposta il pivot nella posizione corretta        
    A[i + 1], A[r] = A[r], A[i + 1]
    
    return i + 1 #ritorna l'indice del pivot
    

    
    
    
    