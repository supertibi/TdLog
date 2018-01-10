# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:50:21 2018

@author: thibaut
"""

import numpy as np
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import psycopg2





def idValue(dict_element):
    return dict_element['id']

def occurencesValue(dict_element):
    return dict_element['occurences']

def genre_dict_in_liste_occurences_on_id(genre_dict,liste_occurences):
    '''complexité atroce'''
    for element in liste_occurences:
        if idValue(genre_dict)==idValue(element):
            return(True)
    return(False)
def index_genre_dict_in_liste_occurences(genre_dict,liste_occurences):
    '''complexité atroce'''
    index=0
    for element in liste_occurences:
        if idValue(genre_dict)==idValue(element):
            return(index)
        index+=1
    return('il y a une erreur')

def save_most_common_genres_list(liste_mots_clefs):
    import pickle
    with open('most_common_genres_list.pkl', 'wb') as output:
        pickle.dump(liste_mots_clefs, output, pickle.HIGHEST_PROTOCOL)
    pass

def retrieve_most_common_genres_list(file='most_common_genres_list.pkl'):
    import pickle
    with open(file, 'rb') as input:
        return(pickle.load(input))


def most_common_genres():
    liste_occurences=[]
    conn = psycopg2.connect(dbname="dbmovies", user="postgres")
    cur = conn.cursor()
    cur.execute("SELECT genre FROM metadata ")
    data=list(cur.fetchall())
    
    
    tour=0

    for item in data[:]:
        tour+=1
        if(tour%500==0):print('tour=',tour,'/',len(data))
        
        
        genres_film=item[0]
        #print(type(genres_film))
        #print(genres_film)
        try:
            genres_film=eval(genres_film)
            

    
            
            for genre_dict in genres_film:
                #print(genre_dict)
                
                
                genre_dict['occurences']=1
                if genre_dict_in_liste_occurences_on_id(genre_dict,liste_occurences):
                    liste_occurences[index_genre_dict_in_liste_occurences(genre_dict,liste_occurences)]['occurences']+=1
                else:
                    #genre_dict['occurences']=1
                    liste_occurences.append(genre_dict)
        except:
            pass
                
    
 
    #print(liste_occurences)
    #print('sort')
    liste_occurences.sort(key=occurencesValue,reverse=True)
    #print(liste_occurences)
    #print('return')
    save_most_common_genres_list(liste_occurences)
    return(liste_occurences)

#print(most_common_genres()[:10])