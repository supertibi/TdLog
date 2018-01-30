import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import pandas as pd
import requests
from PIL import Image
from PIL.ImageQt import ImageQt
from io import BytesIO
import psycopg2
from common_keywords_build import retrieve_most_common_keywords_list
from common_metadata_build import retrieve_most_common_genres_list

from pageaccueil import Ui_PageAccueil
from PageRechercheFilms import Ui_PageRechercheFilms
from PageKevinBacon import Ui_PageKevinBacon
from PageFilmsTrouves import Ui_PageFilmsTrouves
from PageInfosFilm import Ui_PageInfosFilm
import bdd


def QuelID(db,nom):
        requete="SELECT id FROM metadata WHERE upper(title) LIKE "+"upper('"+nom+"')"
        print(requete)
        db.cur.execute(requete)
        liste=db.cur.fetchall()
        if(len(liste)>0):
            IDfilm=str(liste[0])
            IDfilm=int(IDfilm[1:-2])
        else:
            return None
        return(IDfilm)

class PageAccueil2(QtWidgets.QWidget,Ui_PageAccueil):
    def __init__(self, parent=None):
        super(PageAccueil2,self).__init__(parent)
        self.setupUi(self)
        
        
class PageRechercheFilms2(QtWidgets.QWidget,Ui_PageRechercheFilms):
    def __init__(self, parent=None):
        super(PageRechercheFilms2,self).__init__(parent)
        self.setupUi(self)
                
    def ecritureCell(self):
        print("dedans")
        cell=self.TableFilmsCorrespondants.currentItem()
        cell=cell.text()
        print(cell)
        self.ReponseID.setText(cell)
        
        
    def afficheFilmCourant(self):
        db=bdd.Base_de_films()
        IDfilm=QuelID(db,self.ReponseID.text())
        if(IDfilm != None):
            f=bdd.Film(IDfilm)
            self.TitreFilmCourant.setText(f.title)
            image=bdd.fetch_image(f.poster_path,False)
            qimage = ImageQt(image)
            pixmap = QtGui.QPixmap.fromImage(qimage)
        
            self.AfficheFilmCourant.setPixmap(pixmap)
        
        
    def ouvertureTrouves(self):
        db=bdd.Base_de_films()
        db.Matrix_DB_fast(full_database=True)
        IDfilm=QuelID(db,self.ReponseID.text())
        liste_de_reco=db.recomandation(IDfilm)
        
        #On ouvre la page avec les films trouves et on met en forme
        
        self.PageFilmsTrouves = QtWidgets.QWidget()
        self.uiPFT=PageFilmsTrouves2()
        self.uiPFT.setupUi(self.PageFilmsTrouves)
        
        f1=liste_de_reco[0]
        f2=liste_de_reco[1]
        f3=liste_de_reco[2]
    
        self.uiPFT.TitreFilm1.setText(f1.title)
        self.uiPFT.TitreFilm2.setText(f2.title)
        self.uiPFT.TitreFilm3.setText(f3.title)
        
        self.uiPFT.DateSortie1.setText(f1.release_date)
        self.uiPFT.DateSortie2.setText(f2.release_date)
        self.uiPFT.DateSortie3.setText(f3.release_date)
        
        f1.image=bdd.fetch_image(f1.poster_path)
        qimage1 = ImageQt(f1.image)
        pixmap1 = QtGui.QPixmap.fromImage(qimage1)
        self.uiPFT.AfficheFilm1.setPixmap(pixmap1)
        f2.image=bdd.fetch_image(f2.poster_path)
        qimage2 = ImageQt(f2.image)
        pixmap2 = QtGui.QPixmap.fromImage(qimage2)
        self.uiPFT.AfficheFilm2.setPixmap(pixmap2)
        f3.image=bdd.fetch_image(f3.poster_path)
        qimage3 = ImageQt(f3.image)
        pixmap3 = QtGui.QPixmap.fromImage(qimage3)
        self.uiPFT.AfficheFilm3.setPixmap(pixmap3)
        
        
        #On parametre les fonctionnalites d'information sur les films        
        self.uiPFT.AfficheFilm1.clicked.connect(self.infosFilm1)
        self.uiPFT.AfficheFilm2.clicked.connect(self.infosFilm2)
        self.uiPFT.AfficheFilm3.clicked.connect(self.infosFilm3)
        
        
        self.PageFilmsTrouves.show()  

    def trouveFilms(self):
        db=bdd.Base_de_films()
        requete="SELECT title FROM metadata WHERE title LIKE '%"+self.ReponseID.text()+"%'"
        db.cur.execute(requete)
        liste_noms=db.cur.fetchall()
        texte_noms=""
        for i in range(len(liste_noms)):
            titre=str(liste_noms[i])[1:-2]
            texte_noms=texte_noms+titre[1:-1]+"\n"
#        self.ListeFilmsCorrespondants.setText(texte_noms)
        self.setTable(liste_noms)
        
    def setTable(self,liste_noms):
        self.TableFilmsCorrespondants.setRowCount(len(liste_noms))
        for i in range(len(liste_noms)):
            titre=str(liste_noms[i])[1:-2]
            titre=titre[1:-1]
            self.TableFilmsCorrespondants.setItem(i, 0, QtWidgets.QTableWidgetItem(titre))
     
    def infosFilm0(self):
        self.infosFilm(self.ReponseID.text())
    def infosFilm1(self):
        self.infosFilm(self.uiPFT.TitreFilm1.text())    
    def infosFilm2(self):
        self.infosFilm(self.uiPFT.TitreFilm2.text())
    def infosFilm3(self):
        self.infosFilm(self.uiPFT.TitreFilm3.text())    
    
    
    def infosFilm(self,nom):
        db=bdd.Base_de_films()
#        nom=self.ReponseID
        IDfilm=QuelID(db,nom)
        f=bdd.Film(IDfilm)
        
        self.PageInfosFilm = QtWidgets.QWidget()
        self.uiPIF=PageInfosFilm2()
        self.uiPIF.setupUi(self.PageInfosFilm)
        
        self.uiPIF.Date.setText("Released "+f.release_date)
        if('NaN'==f.belong_to_collection):
            self.uiPIF.Collection.setText(f.title)
        else:
            self.uiPIF.Collection.setText(f.belong_to_collection['name'][:-11])
        self.uiPIF.Synopsis.setText(f.overview)
        self.uiPIF.Tagline.setText(f.tagline)
        self.uiPIF.Titre.setText(f.title)
        self.uiPIF.Runtime.setText(str(int(f.runtime))+"min")
        textVotes="/10 - "
        textVotes=str(f.vote_average)+textVotes+str(f.vote_count)+" votes"
        self.uiPIF.Votes.setText(textVotes)
        f.image=bdd.fetch_image(f.poster_path)
        qimage = ImageQt(f.image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.uiPIF.Affiche.setPixmap(pixmap)
        
        self.PageInfosFilm.show()
        
            
        
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
        f1.image=bdd.fetch_image(f1.poster_path)
        f2.image=bdd.fetch_image(f2.poster_path)
        f3.image=bdd.fetch_image(f3.poster_path)
        self.AfficheFilm1.pixmap(f1.image)
        self.AfficheFilm2.pixmap(f2.image)
        self.AfficheFilm3.pixmap(f3.image)
        

        
        
class PageInfosFilm2(QtWidgets.QWidget,Ui_PageInfosFilm):
    def __init__(self, parent=None):
        super(PageInfosFilm2,self).__init__(parent)
        self.setupUi(self)
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Home')
        self.resize(800, 500)
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
       
        
        self.PageAccueil = QtWidgets.QWidget()
        self.uiPA = PageAccueil2()
        self.uiPA.setupUi(self.PageAccueil)
        
        palette = self.PageAccueil.palette()
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        
        
        self.PageRechercheFilms = QtWidgets.QMainWindow()
        self.uiPR=PageRechercheFilms2()
        self.uiPR.setupUi(self.PageRechercheFilms)
        
        self.PageKevinBacon = QtWidgets.QWidget()
        self.uiPKB=PageKevinBacon2()
        self.uiPKB.setupUi(self.PageKevinBacon)
        
        
        ##=============Fonctionnalites de la page d'accueil=============
        self.uiPA.KevinBacon.setGeometry(QtCore.QRect(self.PageAccueil.width()/9,self.PageAccueil.height()/6,self.PageAccueil.width()/3,self.PageAccueil.width()/3*1.3))
        self.uiPA.AffichesFilms.setGeometry(QtCore.QRect(self.PageAccueil.width()*(1-1/9)-self.uiPA.KevinBacon.width(),self.PageAccueil.height()/6,self.PageAccueil.width()/3,self.PageAccueil.width()/3*1.3))
        self.font=QtGui.QFont()
        self.font.setPointSize(self.uiPA.KevinBacon.width()/7)
        self.font.setFamily('Haettenschweiler')
        self.uiPA.KevinBaconLabel.setFont(self.font)
        self.uiPA.FilmRecoLabel.setFont(self.font)
        self.uiPA.FilmRecoLabel.adjustSize()
        self.uiPA.KevinBaconLabel.setGeometry(QtCore.QRect(self.uiPA.KevinBacon.x(),self.uiPA.KevinBacon.y()-10+self.uiPA.KevinBacon.height(),self.uiPA.KevinBacon.width(),self.PageAccueil.height()))
        self.uiPA.FilmRecoLabel.setGeometry(QtCore.QRect(self.uiPA.AffichesFilms.x()-((self.uiPA.FilmRecoLabel.width()-self.uiPA.AffichesFilms.width())/2),self.uiPA.AffichesFilms.y()-10+self.uiPA.AffichesFilms.height(),self.uiPA.FilmRecoLabel.width(),self.uiPA.FilmRecoLabel.height()))
        self.font.setPointSize(self.PageAccueil.height()/5)
        self.uiPA.HomeLabel.setGeometry(QtCore.QRect(0,-20,self.PageAccueil.width(),self.PageAccueil.height()))
        self.uiPA.HomeLabel.setFont(self.font)
        
        self.uiPA.AffichesFilms.clicked.connect(self.switchToResearchForm)
        self.uiPA.KevinBacon.clicked.connect(self.switchToKB)
        
        ##=============Fonctionnalites de la page de recommandation=============
        
        self.uiPR.ReponseID.textChanged.connect(self.uiPR.trouveFilms)    
        self.uiPR.ReponseID.textChanged.connect(self.uiPR.afficheFilmCourant)
        self.uiPR.SearchButton.clicked.connect(self.uiPR.ouvertureTrouves) 
        
        self.uiPR.AfficheFilmCourant.clicked.connect(self.uiPR.infosFilm0)
      
        self.uiPR.ReturnButton.clicked.connect(self.switchToHome)
        
        self.uiPR.TableFilmsCorrespondants.cellDoubleClicked.connect(self.uiPR.ecritureCell)
        
        
        
        ##=============On lance la premiere page=============
        self.central_widget.addWidget(self.PageRechercheFilms)
        self.central_widget.addWidget(self.PageKevinBacon)
        self.central_widget.addWidget(self.PageAccueil)
        self.central_widget.setCurrentWidget(self.PageAccueil)
        
    def switchToResearchForm(self):
        self.setWindowTitle('Movie Recommendation')
        self.central_widget.setCurrentWidget(self.PageRechercheFilms)
        
    def switchToHome(self):
        self.setWindowTitle('Home')
        self.central_widget.setCurrentWidget(self.PageAccueil)
        
    def switchToKB(self):
        self.setWindowTitle('Kevin Bacon Game')
        self.central_widget.setCurrentWidget(self.PageKevinBacon)
        
        
        
        
        
    def switchToForm(self):
        self.central_widget.addWidget(self.formWidget)
        self.formWidget.formButton.clicked.connect(self.switchToTable)
        self.central_widget.setCurrentWidget(self.formWidget)

    def switchToTable(self):
        self.central_widget.addWidget(self.tableWidget)
        self.central_widget.setCurrentWidget(self.tableWidget)        
    
    
if __name__ == '__main__':
    
    ##=============Initialisation des differentes pages=============
    app = QtWidgets.QApplication(sys.argv)

    
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())