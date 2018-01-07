# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:32:23 2017

@author: thibaut
"""

import numpy as np
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import psycopg2
from common_keywords_build import retrieve_most_common_keywords_list
from common_metadata_build import retrieve_most_common_genres_list



def pickle_retrieve_bdd(self,file='save_bdd.pkl'):
    import pickle
    with open(file, 'rb') as input:
        return(pickle.load(input))
               


def fetch_image(argument_bdd,affiche=True,format=2):
    basic_image='http://image.tmdb.org/t/p/'
    #format doit etre entre 0 et 6
    tailles=['w92','w154', 'w185', 'w342', 'w500', 'w780','original']
    url=basic_image+tailles[format]+argument_bdd
    import requests
    response = requests.get(url)
        
    from PIL import Image
    from io import BytesIO
    i = Image.open(BytesIO(response.content))
    
    if(affiche==True):
        import matplotlib.pyplot
        matplotlib.pyplot.imshow(i)
        matplotlib.pyplot.show()
    return(i)


def idValue(dict_element):
    return dict_element['id']

def word_dict_in_liste_dict_on_id(word_dict,liste_dict):
    '''complexité atroce'''
    for element in liste_dict:
        if idValue(word_dict)==idValue(element):
            return(True)
    return(False)


class Base_de_films():
    
    def __init__(self):
        self.conn = psycopg2.connect(dbname="dbmovies", user="postgres")
        self.cur = self.conn.cursor()
        self.number_features_keywords=10#ou100
        self.number_features_genres=10 # must be <20 (ou 19)
        self.nbre_recomandations=5
        self.usual_keymords=retrieve_most_common_keywords_list()[:self.number_features_keywords]
        self.usual_genres=retrieve_most_common_genres_list()[:self.number_features_genres]
    
    
    def conversion_type_database(self,tempo):
        try:
            tempo[1]=eval(tempo[1])#character varying
        except:
            pass
        try:
            tempo[3]=eval(tempo[3])#character varying
        except:
            pass
        try:
            tempo[12]=eval(tempo[12])#character varying
        except:
            pass   
        try:
            tempo[13]=eval(tempo[13])#character varying
        except:
            pass
        try:
            tempo[17]=eval(tempo[17])#character varying
        except:
            pass   
        return(tempo)
    
    def pickle_dump_bdd(self):
        import pickle
        with open('save_bdd.pkl', 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        pass
    
    def create_all_database(self):
        self.cur.execute("SELECT * FROM metadata")
        self.data=list(self.cur.fetchall())
        self.data_matrix=[list(iter) for iter in self.data]
        pass
    
    
    def Matrix_DB_fast(self,full_database=True):
        self.M=[]
        #self.cur.execute("SELECT * FROM public.metadata JOIN public.keywords on public.metadata.id=public.keywords.id;")
        
        if(full_database==True):
            self.cur.execute("SELECT * FROM public.metadata JOIN public.keywords on public.metadata.id=public.keywords.id;")
        if(full_database==False):
            self.cur.execute("SELECT * FROM public.metadata JOIN public.keywords on public.metadata.id=public.keywords.id LIMIT 1000;")
            
        self.data_and_keywords=list(self.cur.fetchall())
        self.data_matrix_fast=[list(iter) for iter in self.data_and_keywords]
        self.all_id_fast=[enum_film[5] for enum_film in self.data_matrix_fast]
        
        #add_keywords
        for k in self.data_matrix_fast:
            try:
                k[-1]=eval(k[-1])
                k[3]=eval(k[3])
            except:
                pass
        for film in self.data_matrix_fast:
            
            
            film_answer_keywords=[]
            for common in self.usual_keymords:
                if word_dict_in_liste_dict_on_id(common,film[-1]):
                    film_answer_keywords.append(1)
                else:
                    film_answer_keywords.append(0)
            #ici le film_answer_keywords est complet pour le film en question
            
            film_answer_genres=[]
            for common in self.usual_genres:
                if word_dict_in_liste_dict_on_id(common,film[3]):
                    film_answer_genres.append(1)
                else:
                    film_answer_genres.append(0)
            #ici le film_answer_genres est complet pour le film en question
            
            self.M.append(film_answer_keywords+film_answer_genres)
        #for f in self.data_matrix_fast:
            #self.M.append(f.caracteristiques_vector())
            
        pass
        #return(self.data_matrix_fast)
    
    
#  
#    
#    def Matrix_DB(self,full_database=True):
#        self.M=[]
#        if(full_database==True):
#            self.cur.execute("SELECT id FROM metadata")
#        if(full_database==False):
#            self.cur.execute("SELECT id FROM metadata LIMIT 100")
#        self.all_id=list(self.cur.fetchall())
#        self.all_id=[self.all_id[k][0] for k in range(len(self.all_id))]
#        tour=0
#        nbre_tourstotal=len(self.all_id)
#        for id in self.all_id:
#            print('id=',id,'tour',tour,'/',nbre_tourstotal)
#            tour+=1
#            f=Film(id)
#            self.M.append(f.caracteristiques_vector())
#            '''il manque un max d'infos'''
#            '''il est inutile de retourner M'''
#        pass
#        #return(self.M)
    
    def id_to_matrix_column(self,id):
#        if hasattr(self, 'all_id')==False:
#            self.cur.execute("SELECT id FROM metadata")
#            self.all_id=list(self.cur.fetchall())
#            self.all_id=[self.all_id[k][0] for k in range(len(self.all_id))]
#            print('on a fait la table all_id')
        return(self.all_id_fast.index(id))
        
        
        
    def matrix_column_to_id(self,column):
#        if hasattr(self, 'all_id')==False:
#            self.cur.execute("SELECT id FROM metadata")
#            self.all_id=list(self.cur.fetchall())
#            self.all_id=[self.all_id[k][0] for k in range(len(self.all_id))]
#            print('on a fait la table all_id')
        return(self.all_id_fast[column])
        
    def features_distance1(self,id1,id2):
        if hasattr(self, 'M')==False:
            print('il faut charger une matrice')
            
        resultat=0
        for k in range(len(self.M[0])):
            if(self.M[self.id_to_matrix_column(id1)][k]!=self.M[self.id_to_matrix_column(id2)][k]):
                resultat+=1
        
        return(resultat)
    def recomandation(self,id):
        meilleurs_distances=[]
        #premier elt est la distance, le deuxième l'id de l'autre
        #toujours classée par distance décroissante (pire en premier)
        #toujours plus petite le nbre max de recommandations
        colonne0=self.id_to_matrix_column(id)
        print('colonne0',colonne0)
        autres_colonnes=list(range(len(self.M)))
        autres_colonnes.pop(colonne0)
        dist_initialisation=self.features_distance1(self.matrix_column_to_id(colonne0),self.matrix_column_to_id(autres_colonnes[0]))
        meilleurs_distances.append([dist_initialisation,self.matrix_column_to_id(autres_colonnes[0])])
        
        tour=0;tours_total=len(autres_colonnes)
        
        for colonne in autres_colonnes[:10000]:
            tour+=1
            if(tour%1000==0):print('tour',tour,'/',tours_total)
            dist=self.features_distance1(self.matrix_column_to_id(colonne0),self.matrix_column_to_id(colonne))
            if(dist<meilleurs_distances[0][0]):
                meilleurs_distances.append([dist,self.matrix_column_to_id(colonne)])
                if(len(meilleurs_distances)>self.nbre_recomandations):
                    meilleurs_distances.pop(0)
                meilleurs_distances.sort(reverse=True,key=lambda paire:paire[0])
        
        
        films_recommandes=[]
        for k in range(len(meilleurs_distances)):
            films_recommandes.append(Film(meilleurs_distances[k][1]))
        return(films_recommandes)
   

    

class Film(Base_de_films):
    
    def __init__(self,id):
        Base_de_films.__init__(self)
        

        self.cur.execute("SELECT * FROM metadata WHERE id = %s", (id,))
        
        list_fetchone=list(self.cur.fetchone())
        tempo=self.conversion_type_database(list_fetchone)

        
        self.adult=tempo[0]#boolean
        self.belong_to_collection=tempo[1]#character varying
        self.budget=tempo[2]#bigint
        self.genre=tempo[3]#character varying
        self.homepage=tempo[4]#character varying
        self.id=tempo[5]#int
        self.imdb_id=tempo[6]#character varying
        self.original_language=tempo[7]#character varying
        self.original_title=tempo[8]#character varying
        self.overview=tempo[9]#character varying
        self.popularity=tempo[10]#real
        self.poster_path=tempo[11]#character varying
        self.production_companies=tempo[12]#character varying
        self.production_countries=tempo[13]#character varying
        self.release_date=tempo[14]#character varying
        self.revenue=tempo[15]#bigint
        self.runtime=tempo[16]#real
        self.spoken_languages=tempo[17]#character varying
        self.status=tempo[18]#character varying
        self.tagline=tempo[19]#character varying
        self.title=tempo[20]#character varying
        self.video=tempo[21]#boolean
        self.vote_average=tempo[22]#real
        self.vote_count=tempo[23]#int
        print(self.title)
    def add_keywords(self):
        self.cur.execute("SELECT * FROM keywords WHERE id = %s", (self.id,))
        try:
            self.keywords=eval(self.cur.fetchone()[1])
        except:
            pass
    def keywords_vector(self):
        self.add_keywords()
        answer_vector=[]
        for common in self.usual_keymords:
            if word_dict_in_liste_dict_on_id(common,self.keywords):
                answer_vector.append(1)
            else:
                answer_vector.append(0)
        return(answer_vector)
    def genres_vector(self):
        
        answer_vector=[]
        for common in self.usual_genres:
            if word_dict_in_liste_dict_on_id(common,self.genre):
                answer_vector.append(1)
            else:
                answer_vector.append(0)
        return(answer_vector)
    
    def caracteristiques_vector(self):
        return(self.keywords_vector()+self.genres_vector())
        
        

    def __str__(self):
        print("_____________________________________________________________")
        try:
            fetch_image(self.poster_path)
        except:pass
        print("popularité=",self.popularity)
        print("tagline:",self.tagline)
        print("overview:",self.overview)
        print("id:",self.id)
        return(self.title)
        
        
    



    

