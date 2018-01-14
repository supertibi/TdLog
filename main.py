import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import psycopg2
from common_keywords_build import retrieve_most_common_keywords_list
from common_metadata_build import retrieve_most_common_genres_list

from pageaccueil import Ui_PageAccueil
from PageRechercheFilms import Ui_PageRechercheFilms
from PageKevinBacon import Ui_PageKevinBacon
from PageFilmsTrouves import Ui_PageFilmsTrouves
from PageHelp import Ui_PageHelp
import bdd


class PageAccueil2(QtWidgets.QWidget,Ui_PageAccueil):
    def __init__(self, parent=None):
        super(PageAccueil2,self).__init__(parent)
        self.setupUi(self)
        
        
class PageRechercheFilms2(QtWidgets.QWidget,Ui_PageRechercheFilms):
    def __init__(self, parent=None):
        super(PageRechercheFilms2,self).__init__(parent)
        self.setupUi(self)
    
    def AlgorithmeDB(self):
        IDfilm=int(self.ReponseID.text())
        liste_de_reco=db.recomandation(IDfilm)
#        f1=liste_de_reco[0]
#        f2=liste_de_reco[1]
#        f3=liste_de_reco[2]
#        self.TitreFilm1.setText(f1.title)
#        self.TitreFilm2.setText(f2.title)
#        self.TitreFilm3.setText(f3.title)
#        self.DateSortie1.setText(f1.release_date)
#        self.DateSortie2.setText(f2.release_date)
#        self.DateSortie3.setText(f3.release_date)
#        f1.image=bdd.fetch_image(f1.poster_path)
#        f2.image=bdd.fetch_image(f2.poster_path)
#        f3.image=bdd.fetch_image(f3.poster_path)
#        self.AfficheFilm1.pixmap(f1.image)
#        self.AfficheFilm2.pixmap(f2.image)
#        self.AfficheFilm3.pixmap(f3.image)
        return liste_de_reco
        
        
    def afficheFilmCourant(self):
       # IDfilm=int(self.ReponseID.text())
        requete="SELECT id FROM metadata WHERE title="+"'"+self.ReponseID.text()+"'"
        db.cur.execute(requete)
        IDfilm=str(db.cur.fetchall()[0])
        IDfilm=IDfilm[1:-2]
        print(IDfilm)
        f=bdd.Film(IDfilm)
        self.TitreFilmCourant.setText(f.title)
#        image=bdd.fetch_image(f.poster_path)
#        self.AfficheFilmCourant.pixmap(image)
        
    def ouvertureTrouves(self,uiPFT,PageFilmsTrouves):
        liste_de_reco=self.AlgorithmeDB()
        f1=liste_de_reco[0]
        f2=liste_de_reco[1]
        f3=liste_de_reco[2]
        uiPFT.TitreFilm1.setText(f1.title)
        uiPFT.TitreFilm2.setText(f2.title)
        uiPFT.TitreFilm3.setText(f3.title)
        uiPFT.DateSortie1.setText(f1.release_date)
        uiPFT.DateSortie2.setText(f2.release_date)
        uiPFT.DateSortie3.setText(f3.release_date)
#        f1.image=bdd.fetch_image(f1.poster_path)
#        f2.image=bdd.fetch_image(f2.poster_path)
#        f3.image=bdd.fetch_image(f3.poster_path)
#        self.AfficheFilm1.pixmap(f1.image)
#        self.AfficheFilm2.pixmap(f2.image)
#        self.AfficheFilm3.pixmap(f3.image)
        PageFilmsTrouves.show()
    
            
        
class PageKevinBacon2(QtWidgets.QWidget,Ui_PageKevinBacon):
    def __init__(self, parent=None):
        super(PageKevinBacon2,self).__init__(parent)
        self.setupUi(self)   
        
class PageFilmsTrouves2(QtWidgets.QWidget,Ui_PageFilmsTrouves):
    def __init__(self, parent=None):
        super(PageFilmsTrouves2,self).__init__(parent)
        self.setupUi(self)   
        
    def ouvertureFenetre(self,liste_de_reco):
        f1=liste_de_reco[0]
        f2=liste_de_reco[1]
        f3=liste_de_reco[2]
        self.TitreFilm1.setText(f1.title)
        self.TitreFilm2.setText(f2.title)
        self.TitreFilm3.setText(f3.title)
        self.DateSortie1.setText(f1.release_date)
        self.DateSortie2.setText(f2.release_date)
        self.DateSortie3.setText(f3.release_date)
#        f1.image=bdd.fetch_image(f1.poster_path)
#        f2.image=bdd.fetch_image(f2.poster_path)
#        f3.image=bdd.fetch_image(f3.poster_path)
#        self.AfficheFilm1.pixmap(f1.image)
#        self.AfficheFilm2.pixmap(f2.image)
#        self.AfficheFilm3.pixmap(f3.image)
        
class PageHelp2(QtWidgets.QWidget,Ui_PageHelp):
    def __init__(self, parent=None):
        super(PageHelp2,self).__init__(parent)
        self.setupUi(self)  
        
    def trouveFilms(self):
        db=bdd.Base_de_films()
        requete="SELECT title FROM metadata WHERE title LIKE '%"+self.NomFilm.text()+"%'"
        db.cur.execute(requete)
        liste_noms=db.cur.fetchall()
        texte_noms=""
        for i in range(len(liste_noms)):
            titre=str(liste_noms[i])[1:-2]
            texte_noms=texte_noms+titre[1:-1]+"\n"
        self.ListeFilmsCorrespondants.setText(texte_noms)
            
 #       self.ReponseID.setText(idTitre)


        
    
    
if __name__ == '__main__':
    import sys
    
    ##=============Initialisation des differentes pages=============
    app = QtWidgets.QApplication(sys.argv)
    PageAccueil = QtWidgets.QWidget()
    uiPA = PageAccueil2()
    uiPA.setupUi(PageAccueil)
    
    
    PageRechercheFilms = QtWidgets.QWidget()
    uiPR=PageRechercheFilms2()
    uiPR.setupUi(PageRechercheFilms)
    
    PageKevinBacon = QtWidgets.QWidget()
    uiPKB=PageKevinBacon2()
    uiPKB.setupUi(PageKevinBacon)
    
    PageFilmsTrouves = QtWidgets.QWidget()
    uiPFT=PageFilmsTrouves2()
    uiPFT.setupUi(PageFilmsTrouves)
    
    PageHelp = QtWidgets.QWidget()
    uiPH=PageHelp2()
    uiPH.setupUi(PageHelp)
    
    ##=============Fonctionnalites de la page d'accueil=============
    uiPA.KevinBacon.setGeometry(QtCore.QRect(PageAccueil.width()/9,PageAccueil.height()/6,PageAccueil.width()/3,PageAccueil.width()/3*1.3))
    uiPA.AffichesFilms.setGeometry(QtCore.QRect(PageAccueil.width()*(1-1/9)-uiPA.KevinBacon.width(),PageAccueil.height()/6,PageAccueil.width()/3,PageAccueil.width()/3*1.3))
    font=QtGui.QFont()
    font.setPointSize(uiPA.KevinBacon.width()/7)
    font.setFamily('Haettenschweiler')
    uiPA.KevinBaconLabel.setFont(font)
    uiPA.FilmRecoLabel.setFont(font)
    uiPA.FilmRecoLabel.adjustSize()
    uiPA.KevinBaconLabel.setGeometry(QtCore.QRect(uiPA.KevinBacon.x(),uiPA.KevinBacon.y()-10+uiPA.KevinBacon.height(),uiPA.KevinBacon.width(),PageAccueil.height()))
    uiPA.FilmRecoLabel.setGeometry(QtCore.QRect(uiPA.AffichesFilms.x()-((uiPA.FilmRecoLabel.width()-uiPA.AffichesFilms.width())/2),uiPA.AffichesFilms.y()-10+uiPA.AffichesFilms.height(),uiPA.FilmRecoLabel.width(),uiPA.FilmRecoLabel.height()))
    font.setPointSize(PageAccueil.height()/5)
    uiPA.HomeLabel.setGeometry(QtCore.QRect(0,-20,PageAccueil.width(),PageAccueil.height()))
    uiPA.HomeLabel.setFont(font)
    
    uiPA.AffichesFilms.clicked.connect(PageRechercheFilms.show)
    uiPA.KevinBacon.clicked.connect(PageKevinBacon.show)
    
    ##=============Fonctionnalites de la page de recommandation=============
    db=bdd.Base_de_films()
    db.Matrix_DB_fast(full_database=True)
    
    uiPR.HelpButton.clicked.connect(PageHelp.show)    
    uiPR.ReponseID.textChanged.connect(uiPR.afficheFilmCourant)
    uiPR.SearchButton.clicked.connect(uiPFT.ouvertureFenetre)  
    uiPR.SearchButton.clicked.connect(PageFilmsTrouves.show)
  
    uiPR.ReturnButton.clicked.connect(PageRechercheFilms.close)
    
    ##=============Fonctionnalites de la page films trouves=============
    
    ##=============Fonctionnalites de la page d'aide=============
    uiPH.NomFilm.textChanged.connect(uiPH.trouveFilms)
    
    
    ##=============Execution=============
    
    PageAccueil.show()
    PageAccueil.raise_()
    

    sys.exit(app.exec_())