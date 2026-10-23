# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 10:23:14 2025

@author: giuli
"""

def peak_finder(arr):
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return len(arr) - 1
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            return i
    return -1

def variante_picchi(lista): #caso in cui non ci possono essere numeri uguali
    n = len(lista)
    if n == 1:
        return 0
    if lista[0] > lista[1]:
        return 0
    if lista[n - 1] > lista[n - 2]:
        return n - 1
    lo, hi = 1, n - 2
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if lista[mid] > lista[mid - 1] and lista[mid] > lista[mid + 1]:
            return mid
        if lista[mid + 1] > lista[mid]:
            lo = mid + 1
            continue #il picco è nella parte destra
        else: hi = mid - 1 #il picco è nella parte sinistra
    
print(variante_picchi([1, 2, 4, 5, 7, 8, 3]))       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    