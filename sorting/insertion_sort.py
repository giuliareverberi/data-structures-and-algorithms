# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 18:49:40 2025

@author: giuli
"""
#Insertion sort
def main(array): #L'input è un array
    n = len(array)
    
    #Scorro gli elementi dell'array a partire dal secondo perchè il primo è 
    #già "ordinato con se stesso"
    for i in range(1, n):  
        key = array[i]   #Seleziono l'elemento corrente per poterlo confrontare con gli altri
        j = i - 1    #inizializzo j come l'indice dell'elemento precedente alla chiave
        
        #Sposto gli elementi maggiori di key presenti in array[:i-1] di una posizione
        while j >= 0 and array[j] > key: 
            array[j + 1] = array[j] #Faccio avanzare l'elemento array[j] di una posizione (lo sposto a destra)
            j -= 1 #Passo all'elemento precedente
            
        #Inserisco la chiave nella sua posizione corretta (tutto sarà ordinato fino alla posizione i)
        array[j + 1] = key 
    return array #Restituisco la lista iniziale ordinata in ordine crescente


print(main([5, 4, 3, 2, 4, 1, 6]))




