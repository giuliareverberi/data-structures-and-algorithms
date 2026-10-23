# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:20:36 2026

@author: giuli
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_at_end(self, data):
        nuovo = Node(data)
        if self.head is None:
            self.head = nuovo
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next    
        current_node.next = nuovo
        
    def insert_at_beginning(self, data):
        nuovo = Node(data)
        if self.head is None:
            self.head = nuovo
            return
        else:
            nuovo.next = self.head
            self.head = nuovo
            
    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            
    def search(self, data):
        corrente = self.head
        while corrente is not None:
            if corrente.data == data:
                return True
            corrente = corrente.next
        return False
    
    def display(self):
        corrente = self.head
        result = ""
        while corrente is not None:
            result += (str(corrente.data))
            if corrente.next is not None:
                result += "->"
            corrente = corrente.next
        print(result)
            
        