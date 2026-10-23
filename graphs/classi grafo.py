#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 12:06:00 2025

@author: valeriodimarco
"""

class Node():
    
    def __init__(self,name):
        
        self.name=name
        
    def getName(self):
        
        return self.name
    
    
    def __str__(self):
        
        return self.name
    
    
    



class Edge():
    
    def __init__(self,source,destination):
        
        self.source= source
        self.destination= destination
        
    def getSource(self):
        
        return self.source
    
    def getDestination(self):
        
        return self.destination
    
    def __str__(self):
        
        return self.source.getName()+'->'+self.destination.getName() 
        # |
        # |
        # |
        # sia source che destinaation sono nodi, quindi hanno metodo getName
        
        
nod1= Node('V')
nod2= Node('W')
arco= Edge (nod1,nod2)










class Digraph():
    
    ''' edges è un dizionario che mappa ogni nodo alla lista dei suoi vicini'''
       
    
    def __init__(self):
        
        self.edges={}  # creiamo un dizionario vuoto e poi lo popoliamo
        
    def addNode(self,node):
        
        if node in self.edges:
            
            raise ValueError
            
        else:
            
            self.edges[node]=[]
            
    def addEdge(self,edge):
        
        source= edge.getSource()
        
        destination= edge.getDestination()
        
        if not (source in self.edges and destination in self.edges):
            
            
            raise ValueError
            
        self.edges[source].append(destination)
        
        
    def children_of(self,node):
        
        return self.edges[node]
    
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
        
        
    def getNodeList(self):
        nodeList = []
        for node in self.edges:
          nodeList.append(node)
        return nodeList
    
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1] #omit final newline
    
    
    
class Graph(Digraph):
    
    def addEdge(self,edge):
        
        Digraph.addEdge(self,edge)
        reverse= Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self, reverse)
        
        
def buildCityGraph(graphType):
    g = graphType()
    cities = ('Milano', 'Bologna', 'Firenze', 'Roma', 'Pescara', 'Bari', 'Taranto', 'Torino', 'Venezia', 'Trieste', 'Napoli', 'Padova', 'Salerno', 'Potenza', 'Catanzaro', 'Reggio Calabria')
    for city in cities: #Create 11 nodes
        g.addNode(Node(city))
    g.addEdge(Edge(g.getNode('Milano'), g.getNode('Bologna')))
    g.addEdge(Edge(g.getNode('Bologna'), g.getNode('Firenze')))
    g.addEdge(Edge(g.getNode('Firenze'), g.getNode('Roma')))
    g.addEdge(Edge(g.getNode('Roma'), g.getNode('Napoli')))
    g.addEdge(Edge(g.getNode('Bologna'), g.getNode('Pescara')))
    g.addEdge(Edge(g.getNode('Pescara'), g.getNode('Bari')))
    g.addEdge(Edge(g.getNode('Bari'), g.getNode('Taranto')))
    g.addEdge(Edge(g.getNode('Torino'), g.getNode('Milano')))
    g.addEdge(Edge(g.getNode('Milano'), g.getNode('Padova')))
    g.addEdge(Edge(g.getNode('Padova'), g.getNode('Venezia')))
    g.addEdge(Edge(g.getNode('Bologna'), g.getNode('Padova')))
    g.addEdge(Edge(g.getNode('Venezia'), g.getNode('Trieste')))
    g.addEdge(Edge(g.getNode('Salerno'), g.getNode('Potenza')))
    g.addEdge(Edge(g.getNode('Potenza'), g.getNode('Catanzaro')))
    g.addEdge(Edge(g.getNode('Catanzaro'), g.getNode('Reggio Calabria')))
    return g


# g = buildCityGraph(Graph)
# print(g)



def printPath(path):
    """Assumes path is a list of nodes"""
    
    # stampa semplicemente il percorso (una lista di nodi)
    
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1: # se non è l'ultima tappa del path, aggiungo freccia
        # di collegamento a prossima tappa
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):  # inserisco il nodo finale, da trovare
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
       
    # algoritmo che implementa sia visita che shortest path  
     
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
        
        
        
    if start == end:  # se ho trovato l'oggetto che stavo cercando, esco
        return path
    
   
    
    for node in graph.childrenOf(start):  # itero sui vicini del nodo 
        if node not in path: # se non è stato esplorato
        
            # per ogni direzione, mantiene
            # una lista path che mi informa su path percorso finora
            # è inutile procedere in direzioni non ottime ---> len(path)<len(shortest)
    
            if shortest == None or len(path) < len(shortest):  
                
                # chiamo ricorsivamente la funzione. non su start, end. ma su node, end
                # la sto quindi chiamando non sul nodo stesso, ma sul vicino
                
                #  ATTENZIONE: è qui che, per come lavora Python, utilzziamo il concetto di pila
                # anche se non c'è una pila esplicita
                
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest

def shortestPath_DFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
       
       
    # racchiude, per sempicità e concisione, la funzione DFS in un unico algoritmo
       
       
    return DFS(graph, start, end, [], None, toPrint)
        

# ATTENZIONE: qui la distanza non è pesata, ma è semplicemente data dal numero
# di archi tra un nodo e un altro

def testSP_DFS(source, destination):
    g = buildCityGraph(Graph)
    sp = shortestPath_DFS(g, g.getNode(source), g.getNode(destination),
                      toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

testSP_DFS('Napoli', 'Torino')


##########################################################################################



# ALGORITMO PER BFS

printQueue = True

def BFS(graph, start, end, toPrint = False):  # non è funzione che usa ricorsione
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
       
    # il path chiaramente inizia da start
      
    initPath = [start]
    
    
    pathQueue = [initPath] # cosa aggiungo nella lista pathQueue
    
    # non aggiungiamo solo il node, ma tutto il percorso che ha portato da start a quel node
    
    # aggiungo tutti i path che stiamo seguendo
    
    
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        if printQueue:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p))
                
                
        # prendo il primo path in lista   
                
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
            print()
            
        # l'ultimo nodo è l'ultimo elemento di path  
            
        lastNode = tmpPath[-1]
        
        # se l'ultimo nodo è proprio la mia destinazione finale, 
        # ritorno il percorso che mi ha portato fino a lì.
        # la prima volta che tocco end, ritorno immediatamente il path che mi 
        # ha portato lì, che sarà sicuramente il più breve
        
        
        
        if lastNode == end:
            return tmpPath
        
        # altrimenti, esploro i vicini dell'ultimo nodo (il livello successivo)
        
        
        for nextNode in graph.childrenOf(lastNode):
            
            # se il prossimo nodo non è nel percorso, lo aggiungo a path, e aggiungo
            # path a pathQueue
            
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def shortestPath_BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end, toPrint)






# La DFS deve visitare tutto quanto, la BFS no. Quando ho raggiunto l'obiettivo, posso
# terminare, perchè se ci fosse stato un percorso più breve l'avrei trovato 
# a un livello precedente

##################################################################


def reachableFrom(graph, start):
    
    # molto semplice, capire quali nodi sono connessi ad un dato nodo
    
    
    # visito in profondità
    
    
    """Assumes graph is a Digraph; start is a node;
      returns the list of nodes reachable from start."""
      
    # inizialmente i nodi raggiungibili sono solo start
      
    reachableNodes = {start}
    
    
    # to visita sarà una pila
    
    
    to_visit = []
    
    
    # visito i vicini
    
    for node in graph.childrenOf(start):
        
        # li aggiungo alla lista dei nodi da visitare
        
      to_visit.append(node)
      
      
    # se la lista non è vuota...
      
    while len(to_visit) > 0:
        
      # faccio il pop dell'ultimo elemento
        
      node = to_visit.pop()
      
      # lo aggiungo a set nodi raggiungibili
      
      reachableNodes.add(node)
      
     # esploro i figli del nodo appena aggiunto
      
      for child in graph.childrenOf(node):
          
          # se il figlio su cui sto iterando non è stato già aggiunto,
          # lo aggiungo a quelli da visitare
          
        if child not in reachableNodes:
            to_visit.append(child)
            
    # ritorno i nodi raggiungibili
            
            
            
    return reachableNodes

def printConnectedComponent(component):
    """print nodes in component"""
    component = list(component)
    result = ''
    for i in range(len(component)):
        result = result + str(component[i])
        if i != len(component) - 1:
            result = result + ', '
    return result






        
        
    
    
        
        

        
        
        
        
        
        
        