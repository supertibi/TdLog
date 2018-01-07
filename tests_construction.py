# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:03:33 2018

@author: thibaut
"""



import bdd
import time
import numpy as np

def test_film_class():

    
    
    for k in range(100):
        try:
            print(bdd.Film(k))
        except:
            pass
    
    
    pass




def main1():
    temps_initial=time.time()
    
    #test_film_class()
    
    db=bdd.Base_de_films()
    db.Matrix_DB(full_database=False)
    
    #print(db.M)
    liste_de_reco=db.recomandation(39467)
    for film_recommande in liste_de_reco:
        print(film_recommande)
        
    print('sont des films qui ressemblent à ')
    print(bdd.Film(39467))


    temps_total=time.time()- temps_initial
    m, s = divmod(temps_total, 60)
    h, m = divmod(m, 60)
    print("%d:%02d:%02d" % (h, m, s))
    print('test main1 terminé')
    pass
def main2():
    temps_initial=time.time()
    
    #test_film_class()
    
    db=bdd.Base_de_films()
    db.Matrix_DB_fast(full_database=True)
    
    
    print(bdd.Film(11))
    print('voici les suggestions de films qui ressemblent au film ci dessus ')
    
    
    liste_de_reco=db.recomandation(11)
    for film_recommande in liste_de_reco:
        print(film_recommande)
        



    temps_total=time.time()- temps_initial
    m, s = divmod(temps_total, 60)
    h, m = divmod(m, 60)
    print("%d:%02d:%02d" % (h, m, s))
    print('test main2 terminé')
    pass


if __name__=='__main__':
    main2()