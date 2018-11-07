# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 14:43:41 2018

@author: daniel chavez
"""
    
def bubble_sort(alist):                     #sorts list in descending order
    for x in range(len(alist)-1, 0, -1):
        for i in range(x):
            if alist[i].get_num() < alist[i].get_num():
                temp = alist[i]
                alist[i].next_node = alist[i]
                alist[i].next_node.next_node = temp

def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def solution_a():
    password_list = []
    f = open("10-million-combos.txt","r")   #reads .txt file line by line
    f1 = f.readline()
    #line by line begins adding passwords to the list, checking to see
    # if it has been added before. If it finds the password in the list
    #it updates the number of times it has been seen
    for line in f1:
        if password_list.isEmpty():
            password_list.insert(f1, 0)
        if password_list.search(line):
            password_list.num = password_list.num + 1
        else:
            password_list.insert(f1, 0)
            
    bubble_sort(password_list)
    for i in 20:
        temp_password = password_list[i].get_password()
        print (temp_password)
    
def solution_b():
    password_list = LinkedList()
    f = open("10-million-combos.txt","r")
    f1 = f.readline()
    for line in f1:
        if line in password_list:
            password_list[line] = password_list[line] + 1
        else:
            password_list[line] = 1
    merge_sort(password_list)
    for i in 20:
        temp_password = password_list[i].get_password()
        print (temp_password)

class Node(object):
    password = ""
    num = -1
    next_node = None    
    
    def __init__(self, password, num,  next_node):
        self.password = password
        self.num = num
        self.next_node = next_node
        
    def get_password(self):
        return self.password
    
    def get_num(self):
        return self.num
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
    

class LinkedList(object):
    
    def init(self, head = None):
        self.head = head
    
    def insert(self, password, num):
        new_node = Node(password, num)
        new_node.set_next(self.head)
        self.head = new_node
        
    def search(self, password):
        current = self.head
        found = False
        while current and found is False:
            if current.get_password() == password:
                found = True
            else:
                current = current.get_next()
        if current is None:
            self.insert(current, current.get_password(), 0)    #don't know if this should insert a node or just return a value...
        return current