import psycopg2
import csv
import json
import pandas as pd

#conn = psycopg2.connect("dbname=dbmovies user=postgres password=admin") (celui de sacha)
conn = psycopg2.connect(dbname="dbmovies", user="postgres")
cur = conn.cursor()

    

##Remplissage de la table keywords
#avec fichier original

#keywords=open('C:\\Users\\thibaut\\Documents\\Ponts_2A\\tdlog\\projet_cinema\\keywords.csv',"r", encoding="UTF8")
#reader=csv.reader(keywords)
# 

#file=pd.read_csv("C:\\Users\\thibaut\\Documents\\Ponts_2A\\tdlog\\projet_cinema\\the-movies-dataset\\keywords.csv")
## 
#file1=file.as_matrix()
#
#
#i=0
#for row in file1:
#    id1=file1[i][0]
#    txt=file1[i][1]
#    cur.execute("INSERT INTO keywords(id,keywords)"  "VALUES (%s,%s)", (id1,txt))
#    conn.commit()
#    i+=1
#    


#keywords.close()

##Remplissage de la table movies_metadata
# 
#metadata=open('C:\\Users\\thibaut\\Documents\\Ponts_2A\\tdlog\\projet_cinema\\wetransfer-81c866\\movies_metadata_exp\\movies_metadata_exp.txt',"r", encoding="UTF8")
 
#reader2=csv.reader(metadata)
# 
#meta_0=pd.read_csv('C:\\Users\\thibaut\\Documents\\Ponts_2A\\tdlog\\projet_cinema\\wetransfer-81c866\\movies_metadata_exp\\movies_metadata_exp.txt' )
# 
#meta1=meta_0.as_matrix()
#
#
#i=0
#for row in meta1:
#    adult=meta1[i][0]
#    belong_to_collection=meta1[i][1]
#    budget=meta1[i][2]    
#    genre=meta1[i][3]
#    homepage=meta1[i][4]
#    id=meta1[i][5]
#    imdb_id=meta1[i][6]
#    original_language=meta1[i][7]
#    original_title=meta1[i][8]
#    overview=meta1[i][9]
#    popularity=meta1[i][10]
#    poster_path=meta1[i][11]
#    production_companies=meta1[i][12]
#    production_countries=meta1[i][13]
#    release_date=meta1[i][14]
#    revenue=meta1[i][15]
#    runtime=meta1[i][16]
#    spoken_languages=meta1[i][17]
#    status=meta1[i][18]
#    tagline=meta1[i][19]
#    title=meta1[i][20]
#    video=meta1[i][21]
#    vote_average=meta1[i][22]
#    vote_count=meta1[i][23]
#    
#    insert_data="INSERT INTO metadata(adult,belong_to_collection,budget,genre,homepage,id,imdb_id,original_language, original_title, overview, popularity, poster_path, production_companies, production_countries, release_date, revenue,runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count)"  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#
# 
#    cur.execute(insert_data, (adult,belong_to_collection,budget,genre,homepage,id,imdb_id,original_language, original_title, overview, popularity, poster_path, production_companies, production_countries, release_date, revenue,runtime, spoken_languages, status, tagline, title, video, vote_average, vote_count))
#    conn.commit()
#    i=i+1

#metadata.close()

##Remplissage de la table movies_credits

# credits=open('/Users/sachabozou/Desktop/PONTS 2A/TDLOG/Projet/the-movies-dataset/credits.csv',"r", encoding="UTF8")
# 
# reader3=csv.reader(credits)
# 
cred_0=pd.read_csv('C:\\Users\\thibaut\\Documents\\Ponts_2A\\tdlog\\projet_cinema\\credits_sacha2.csv' )

cred=cred_0.as_matrix()

i=0
for row in cred:
    if i<1:
        a=eval(cred[i][0])
        print(a[0]['character'],a[0]['name'])
    cast=cred[i][0]
    crew=cred[i][1]
    id=cred[i][2]
    insert_data="""INSERT INTO credits("cast",crew,id) VALUES (%s,%s,%s)"""
    cur.execute(insert_data,(cast,crew,id))
    conn.commit()
    i+=1
"""adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,
original_title,overview,popularity,poster_path,production_companies,production_countries,
release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count"""



cur.close()
conn.close()