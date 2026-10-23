# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:11:20 2026

@author: giuli
"""

def binary_search(arr, n):
    basso = 0
    alto = len(arr) - 1
    while basso <= alto:
        medio = (alto + basso) // 2
        if arr[medio] == n:
            return medio
        if arr[medio] < n:
            basso = medio + 1
        else:
            alto = medio - 1
    return f"{n} non è nell'array dato"