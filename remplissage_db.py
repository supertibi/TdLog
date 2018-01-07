# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 20:15:43 2017

@author: thibaut
"""

import psycopg2
import pandas as pd

def main():
    #donnees=pd.read_csv('C:\\Users\\thibaut\\Documents\\Ponts_2A\\tdlog\\projet_cinema\\wetransfer-81c866\\credits_1.csv')
    #yolo=[['aze','qsd',3],['aze','qsd',3],['aze','qsd',3]]
    try:
        conn = psycopg2.connect(dbname="dbmovies", user="postgres")
    except:
        print("I am unable to connect to the database")
    
    cur = conn.cursor()
    
    
    for ligne in yolo:
        
        sql = """INSERT INTO credits("cast",crew,id)
                 VALUES(%s,%s,%s) ;"""
        cur.execute(sql, (ligne[0],ligne[1],ligne[2]))
    
    conn.commit()
    cur.close()
    conn.close()
    pass

def supprime_data():
    sure=eval(input("etes vous certain de vouloir supprimer la bdd? (True ou False)"))
    if(sure==True):
        conn = psycopg2.connect(dbname="dbmovies", user="postgres")
        cur = conn.cursor()
        table_a_supprimer='credits'
        cur.execute("DELETE FROM "+table_a_supprimer+" WHERE 0<id ")
        conn.commit()
        cur.close()
        conn.close()
    else:
        pass
if __name__=='__main__':
    pass