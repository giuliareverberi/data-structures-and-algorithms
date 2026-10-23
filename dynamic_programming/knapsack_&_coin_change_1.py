# -*- coding: utf-8 -*-
"""
Created on Wed May  7 08:42:16 2025

@author: giuli
"""


def knapsack(items, B): #input lista items in cui items[i] = (vi, ci) e budget B
    n = len(items)
    result = [] #lista per memorizzare
    
    #costruisco la matrice
    mat = [[0 for _ in range(B + 1)] for _ in range(n + 1)]   
    
    #aggiorno la matrice elemento per elemento dalla prima colonna in basso
    for i in range(1, n+1): #colonne
        for b in range(0, B+1): #righe
            
            if items[i-1][1] > b:   #se l'elemento supera il budget
                mat[i][b] = mat[i-1][b] 
                
            else:  #se non lo supera prendo il massimo tra aggiungerlo o non aggiungerlo
                mat[i][b] = max(items[i-1][0] + mat[i-1][b-items[i-1][1]], 
                                mat[i-1][b])
                
    #backtracking per capire quali ho usato
    i, b = n, B
    while i > 0 and b >= 0:
        if mat[i][b] != mat[i-1][b]:  # l'oggetto i-1 è stato incluso
            result.append(items[i-1])
            b -= items[i-1][1]  # scala il budget
        i -= 1
    result.reverse()
                  
    return (mat[n][B], result)




items = [(1,3), (10,2),(9,1),(3,4)]
B = 5
print(knapsack(items, B))

#------------------------------------------------------------------------------------------------------

#COINCHANGEPROBLEM
#input: target (n naturale) e coins (lista di interi)
#output: numero minimo di monete che sommano a target
#assunzione: 1 appartiene a coins

#cioè target è il numero da raggiungere sommando solo valori da coins (i tagli della moneta)

#phi(i, t) = numero min monete per arrivare a t usando i tagli fino a i
#phi(1, t) = t (la prima moneta è sempre quella che vale 1)
#phi(i, t) = min(for j= 0 to t//coins[i]: j + phi(i-1, t-j*coins[i]))
#per casa!!!!


#e in più aggiungere a knapsack quale è la soluzione che ti porta a quei valori
#FATTO 
    

def coin_change(target, coins):
    n = len(coins)
    
    #float inf significa infinito, così poi trovo sempre un min
    mat = [[float("inf") for _ in range(target + 1)] for _ in range(n + 1)] 
    
    for i in range(n + 1):
        mat[i][0] = 0 
        
    for i in range(1, n + 1):
        coin = coins[i - 1]
        for t in range(target + 1):
            mat[i][t] = min(j + mat[i - 1][t - j * coin] 
                for j in range(t // coin + 1))
    return mat[n][target]   

     
def coinchange(target, coins):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # base: 0 monete per somma 0

    for coin in coins:
        for t in range(coin, target + 1):
            dp[t] = min(dp[t], dp[t - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1


target = 77
coins = [1, 60, 11, 10, 5]    
print(coin_change(target, coins))   
print(coinchange(target, coins))






