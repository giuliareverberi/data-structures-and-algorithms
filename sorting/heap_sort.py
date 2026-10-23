# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:24:25 2025

@author: giuli
"""

def parent(i): 
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(A, i, heapsize):
    l = left(i)
    r = right(i)
    
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heapsize)

def build_max_heap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, i, n)

def heap_sort(A):
    n = len(A)
    build_max_heap(A)
    # riduci heapsize a ogni iterazione
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # max va in fondo
        max_heapify(A, 0, i)     # ricostruisci heap con size ridotta

        
        
A = [16, 5, 4, 3, 2, 7, 22, 11]
heap_sort(A)        