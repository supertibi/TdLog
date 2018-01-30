# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:32:23 2017

@author: sacha
"""
import os
print(os.getcwd())
os.chdir('/Users/sachabozou/Desktop/PONTS 2A/TDLOG/Projet/TdLog-master')
import numpy as np
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import psycopg2
import matplotlib.pyplot as plt

import bdd
from bdd import Film 

import networkx as nx

db=bdd.Base_de_films()


# class Graph:
# 
#     def __init__(self):
#         self.G=nx.Graph()
#         
#     def ajoute_noeud(self,list):
#         self.G.add_nodes_from(list)
#         
#     def ajoute_arrete_rapide(self,M,n):
#         a=0
#         for i in range (0,n):
#             film1=M[i]
#             cast1=eval(M[i][0])
#             id1=film1[2]
#             a=a+1
#             #print(a)
#             for j in range (0,n):
#                 if (i>j):
#                     film2=M[j]
#                     cast2=eval(M[i][0])
#                     id2=film2[2]
#                 
#                     for k in range (0,len(cast1)):
#                         for l in range (0,len(cast2)):
#                             if cast1[k]['name']==cast2[l]['name']:
#                                 self.G.add_edge(id1,id2)
# 
#     def number_of_nodes(self):
#         return (self.G.number_of_nodes())
#         
#     def clear(self):
#         self.G.clear()



def ajoute_arrete_rapide(G,M,n):
    a=0
    for i in range (0,n):
        film1=M[i]
        cast1=eval(M[i][0])
        id1=film1[2]
        a=a+1
        print(a)
        for j in range (i,n):
            film2=M[j]
            cast2=eval(M[j][0])
            id2=film2[2]
                
            for k in range (0,len(cast1)):
                for l in range (0,len(cast2)):
                    if cast1[k]['name']==cast2[l]['name']:
                        G.add_edge(id1,id2)  
                            
    return(G)
    
def list_id(n):
    list=[]
    db.cur.execute("SELECT id FROM metadata;")
    list_id_prov=db.cur.fetchall()
    for i in range (0,len(list_id_prov)):
        list.append(list_id_prov[i][0])
    return list[0:n]
    
def list_id():
    list=[]
    db.cur.execute("SELECT id FROM metadata;")
    list_prov=db.cur.fetchall()
    for i in range (0,len(list_prov)):
        list.append(list_prov[i][0])
    return list
    
    
                
def save_graph(G):
    import pickle
    with open('graph.pkl', 'wb') as output:
        pickle.dump(G, output, pickle.HIGHEST_PROTOCOL)
    pass

def retrieve_graph(file='graph.pkl'):
    import pickle
    with open(file, 'rb') as input:
        return(pickle.load(input))
        
def affiche_graph(G):
    pos=nx.spring_layout(G)         
    nx.draw(G, pos, with_labels=True)
    plt.show()
    
    
# def construit_graph(l):
#     G=nx.Graph()
#     G.add_nodes_from(l)
#     a=0
#     b=0
#     for i in range (0,len(l)):
#         db.cur.execute("SELECT * FROM public.credits WHERE id=%s", (l[i],))
#         film1=db.cur.fetchone()
#         cast1=eval(film1[0])
#         id1=film1[2]
#         a=a+1
#         print(a)
#         for j in range (0,len(l)):
#             print(b)
#             b=b+1
#             db.cur.execute("SELECT * FROM public.credits WHERE id=%s", (l[j],))
#             film2=db.cur.fetchone()
#             cast2=eval(film2[0])
#             id2=film2[2]
#             
#                 
#             for k in range (0,len(cast1)):
#                 for l in range (0,len(cast2)):
#                     if cast1[k]['name']==cast2[l]['name']:
#                         G.add_edge(id1,id2)  
#                             
#     return(G)
#     

                 
def construit_graph(M,n):
    G=nx.Graph()
    l=[]
    a=0
    for i in range (0,n):
        l.append(M[i][2])
    G.add_nodes_from(l)
    for i in range (0,n):
        film1=M[i]
        cast1=eval(M[i][0])
        id1=film1[2]
        a=a+1
        print(a)
        for j in range (i,n):
            film2=M[j]
            cast2=eval(M[j][0])
            id2=film2[2]
            for k in range (0,len(cast1)):
                for l in range (0,len(cast2)):
                    if cast1[k]['name']==cast2[l]['name']:
                        G.add_edge(id1,id2)  
                            
    return(G)
    
def plus_court_chemin(G,id1,id2):
    if nx.has_path(G,id1,id2):
        return (nx.shortest_path(G,id1,id2))
    else:
        print('Les deux films ne sont pas reliés')
    
def max_longeur(G,id1):
    dict=nx.shortest_path_length(G,id1)
    m=0
    for elem in dict:
        if (dict[elem]>m):
            m=dict[elem]
    return m
    

def main():

    db.cur.execute('SELECT * FROM public.credits')
    M=db.cur.fetchall()

    # A=retrieve_graph()
    # print(M[1])

    
    #l=list_id()[0:10]
    #G=construit_graph(M,2000)
    #save_graph(G)
    
    
    A=retrieve_graph()
    #print(nx.single_source_shortest_path(A,862))
    print(plus_court_chemin(A,862,11))
    #print (max(nx.shortest_path_length(A,862)))
    #print (max_longeur(A,8851))
    
if __name__=='__main__':
    main()
    
    



