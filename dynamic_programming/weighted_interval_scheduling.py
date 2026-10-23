# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:16:18 2026

@author: giuli
"""

#calcola il massimo profitto da intervalli compatibili   
def weighted(intervals):
    intervals.sort(key = lambda x: x[1])
    #array che contiene i valori ottenibili fino all'intervallo i
    aus = [intervals[0][2]] #se prendo solo il primo, avrò il suo valore
    for i in range(1, len(intervals)): #itero a partire dal secondo
        prev = prec(intervals, i) #ultimo intervallo compatibile
        if prev == -1:
            #se non c'è un int compatibile, controllo il peso solo dell'intervallo i
            possibile = intervals[i][2]  
        else: 
            #se c'è, sommo il massimo possibile dell'ultimo compatibile al peso corrente
            possibile = aus[prev] +  intervals[i][2]
        #scelgo il massimo tra includere o non includere l'intervallo corrente
        phi_i = max(aus[i - 1], possibile)
        #e lo appendo alla lista ausiliaria
        aus.append(phi_i)
    return aus[-1] #ritorno l'ultimo elemento che è il massimo considerando tutti gli intervalli

#trova l'ultimo intervallo che finisce prima dell'inizio di i
def prec(intervals, i):
    low = 0
    high = len(intervals) - 1
    res = -1
    #ricerca binaria
    while low <= high:
        mid = (low + high) // 2
        if intervals[mid][1] <= intervals[i][0]:
            res = mid    #possibile candidato 
            low = mid + 1
        else:
            high = mid - 1
    return res   #ritorna l'indice dell'ultimo intervallo compatibile