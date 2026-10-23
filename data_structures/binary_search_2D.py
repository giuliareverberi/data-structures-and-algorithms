# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:20:06 2026

@author: giuli
"""

def search_matrice(mat, x):
    lo = 0
    n = len(mat)
    m = len(mat[0])
    hi = n - 1    
    while lo <= hi:
        mid = (lo + hi) // 2
        if x < mat[mid][0]:
            hi = mid - 1
            continue
        if x > mat[mid][m - 1]:
            lo = mid + 1
            continue
        else:
            basso = 0
            alto = m - 1
            while basso <= alto:
                medio = (alto + basso) // 2
                if mat[mid][medio] == x:
                    return (mid, medio)
                if x < mat[mid][medio]:
                    alto = medio - 1
                    continue
                else: basso = medio + 1
    return "Elemento non trovato"
