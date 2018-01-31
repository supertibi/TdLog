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
from PageHelp import Ui_PageHelp
from PageLiensFilms import Ui_PageLiensFilms
import bdd
import graphe

##/////////////////////////////////////////////////////////////////////
##///////////////////////Une fonction utile///////////////////////
##/////////////////////////////////////////////////////////////////////

def QuelID(db,nom):
        requete="SELECT id FROM metadata WHERE upper(title) LIKE "+"upper('"+nom+"')"
        db.cur.execute(requete)
        liste=db.cur.fetchall()
        if(len(liste)>0):
            IDfilm=str(liste[0])
            IDfilm=int(IDfilm[1:-2])
        else:
            return None
        return(IDfilm)
        
##/////////////////////////////////////////////////////////////////////
##///////////////////////Classe PageAccueil///////////////////////
##/////////////////////////////////////////////////////////////////////
        
class PageAccueil2(QtWidgets.QWidget,Ui_PageAccueil):
    def __init__(self, parent=None):
        super(PageAccueil2,self).__init__(parent)
        self.setupUi(self)
        
##/////////////////////////////////////////////////////////////////////
##///////////////////////Classe PageHelp///////////////////////
##/////////////////////////////////////////////////////////////////////
        
class PageHelp2(QtWidgets.QWidget,Ui_PageHelp):
    def __init__(self, parent=None):
        super(PageHelp2,self).__init__(parent)
        self.setupUi(self)
        
    def trouveFilms(self):
        if(len(self.TitreFilm.text())>1):
            db=bdd.Base_de_films()
            requete="SELECT title FROM metadata WHERE title LIKE '%"+self.TitreFilm.text()+"%'"
            db.cur.execute(requete)
            liste_noms=db.cur.fetchall()
            self.setTable(liste_noms)
        
    def setTable(self,liste_noms):
        self.TableFilmsCorrespondants.setRowCount(len(liste_noms))
        for i in range(len(liste_noms)):
            titre=str(liste_noms[i])[1:-2]
            titre=titre[1:-1]
            self.TableFilmsCorrespondants.setItem(i, 0, QtWidgets.QTableWidgetItem(titre))
     
    def ecritureCell(self):
        cell=self.TableFilmsCorrespondants.currentItem()
        cell=cell.text()
        print(cell)
        self.TitreFilm.setText(cell)

##/////////////////////////////////////////////////////////////////////
##///////////////////////Classe PageRechercheFilms///////////////////////        
##/////////////////////////////////////////////////////////////////////
        
class PageRechercheFilms2(QtWidgets.QWidget,Ui_PageRechercheFilms):
    def __init__(self, parent=None):
        super(PageRechercheFilms2,self).__init__(parent)
        self.setupUi(self)
                
    def ecritureCell(self):
        cell=self.TableFilmsCorrespondants.currentItem()
        cell=cell.text()
        print(cell)
        self.ReponseID.setText(cell)
        
        
    def afficheFilmCourant(self):
        db=bdd.Base_de_films()
        IDfilm=QuelID(db,self.ReponseID.text())
        if(IDfilm != None):
            self.CadreFilmCourant.setEnabled(True)
            
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
        self.uiPFT.Cadre1.clicked.connect(self.infosFilm1)
        self.uiPFT.Cadre2.clicked.connect(self.infosFilm2)
        self.uiPFT.Cadre3.clicked.connect(self.infosFilm3)
        
        self.uiPFT.Return.clicked.connect(self.PageFilmsTrouves.close)
        
        
        self.PageFilmsTrouves.show()  

    def trouveFilms(self):
        if(len(self.ReponseID.text())>1):
            db=bdd.Base_de_films()
            requete="SELECT title FROM metadata WHERE upper(title) LIKE upper('%"+self.ReponseID.text()+"%')"
            db.cur.execute(requete)
            liste_noms=db.cur.fetchall()
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
        
        note=f.vote_average
        
        self.uiPIF.Etoile1.setPixmap(QtGui.QPixmap("Images/EtoileGrise.gif"))
        self.uiPIF.Etoile2.setPixmap(QtGui.QPixmap("Images/EtoileGrise.gif"))
        self.uiPIF.Etoile3.setPixmap(QtGui.QPixmap("Images/EtoileGrise.gif"))
        self.uiPIF.Etoile4.setPixmap(QtGui.QPixmap("Images/EtoileGrise.gif"))
        self.uiPIF.Etoile5.setPixmap(QtGui.QPixmap("Images/EtoileGrise.gif"))
        if(note>=1):
            self.uiPIF.Etoile1.setPixmap(QtGui.QPixmap("Images/FullStar.gif"))
        if(note>=3):
            self.uiPIF.Etoile2.setPixmap(QtGui.QPixmap("Images/FullStar.gif"))
        if(note>=5):
            self.uiPIF.Etoile3.setPixmap(QtGui.QPixmap("Images/FullStar.gif"))
        if(note>=7):
            self.uiPIF.Etoile4.setPixmap(QtGui.QPixmap("Images/FullStar.gif"))
        if(note>=9):
            self.uiPIF.Etoile5.setPixmap(QtGui.QPixmap("Images/FullStar.gif"))
            
        
        self.PageInfosFilm.show()

##/////////////////////////////////////////////////////////////////////      
##///////////////////////Classe PageKevinBacon///////////////////////           
##/////////////////////////////////////////////////////////////////////
        
class PageKevinBacon2(QtWidgets.QWidget,Ui_PageKevinBacon):
    def __init__(self, parent=None):
        super(PageKevinBacon2,self).__init__(parent)
        self.setupUi(self)
        
    def afficheFilmCourant1(self):
        pixmap=self.afficheFilmCourant(self.TitreFilm1.text())
        if(pixmap is not None):
            self.AfficheFilm1.setPixmap(pixmap)
        
    def afficheFilmCourant2(self):
        pixmap=self.afficheFilmCourant(self.TitreFilm2.text())
        if(pixmap is not None):
            self.AfficheFilm2.setPixmap(pixmap)
        
    def afficheFilmCourant(self,nom):
        db=bdd.Base_de_films()
        IDfilm=QuelID(db,nom)
        if(IDfilm != None):
            f=bdd.Film(IDfilm)
            imageC=bdd.fetch_image(f.poster_path,False)
            qimageC = ImageQt(imageC)
            pixmapC = QtGui.QPixmap.fromImage(qimageC)
            return pixmapC
        
    def ouvertureHelp1(self):
        self.PageHelp = QtWidgets.QWidget()
        self.uiPH=PageHelp2()
        self.uiPH.setupUi(self.PageHelp)
        
        self.uiPH.TitreFilm.textChanged.connect(self.uiPH.trouveFilms)
        self.uiPH.TableFilmsCorrespondants.cellDoubleClicked.connect(self.uiPH.ecritureCell)
        
        self.uiPH.OK.clicked.connect(self.retourHelp1)
        
        self.PageHelp.show()
    def ouvertureHelp2(self):
        self.PageHelp = QtWidgets.QWidget()
        self.uiPH=PageHelp2()
        self.uiPH.setupUi(self.PageHelp)
        
        self.uiPH.TitreFilm.textChanged.connect(self.uiPH.trouveFilms)
        self.uiPH.TableFilmsCorrespondants.cellDoubleClicked.connect(self.uiPH.ecritureCell)
        
        self.uiPH.OK.clicked.connect(self.retourHelp2)
        
        self.PageHelp.show()
        
    def retourHelp1(self):
        self.TitreFilm1.setText(self.uiPH.TitreFilm.text())
        self.PageHelp.close()
    def retourHelp2(self):
        self.TitreFilm2.setText(self.uiPH.TitreFilm.text())
        self.PageHelp.close()
        
        
    def trouveLiens(self):
        db=bdd.Base_de_films()
        A=graphe.retrieve_graph()
        liste_IDfilms=graphe.plus_court_chemin(A,QuelID(db,self.TitreFilm1.text()),QuelID(db,self.TitreFilm2.text()))
        self.liste_films=[]
        for i in range(len(liste_IDfilms)):
            self.liste_films.append(bdd.Film(liste_IDfilms[i]))
            
        self.PageLiensFilms = QtWidgets.QWidget()
        self.uiPLF=PageLiensFilms2()
        self.uiPLF.setupUi(self.PageLiensFilms)
        
        self.i=0
        
        
        self.uiPLF.PointDroitFleche.clicked.connect(self.avance)
        self.uiPLF.PointGaucheFleche.clicked.connect(self.recule)
        self.uiPLF.Cadre1.clicked.connect(self.infosFilm1)
        self.uiPLF.Cadre2.clicked.connect(self.infosFilm2)
        
        self.afficheAffiches()
        self.PageLiensFilms.show()
        
    def afficheAffiches(self):
        f1=self.liste_films[self.i]
        f2=self.liste_films[self.i+1]
        self.uiPLF.Titre1.setText(f1.title)
        self.uiPLF.Titre2.setText(f2.title)
        f1.image=bdd.fetch_image(f1.poster_path)
        qimage1 = ImageQt(f1.image)
        pixmap1 = QtGui.QPixmap.fromImage(qimage1)
        self.uiPLF.Affiche1.setPixmap(pixmap1)
        f2.image=bdd.fetch_image(f2.poster_path)
        qimage2 = ImageQt(f2.image)
        pixmap2 = QtGui.QPixmap.fromImage(qimage2)
        self.uiPLF.Affiche2.setPixmap(pixmap2)
        
    def avance(self):
        self.i+=1
        if(self.i<1):
            self.uiPLF.PointGauche.setEnabled(False)
        else:
            self.uiPLF.PointGauche.setEnabled(True)
        if(self.i>=len(self.liste_films)-2):
            self.uiPLF.PointDroit.setEnabled(False)
        else:
            self.uiPLF.PointDroit.setEnabled(True)
        
        self.afficheAffiches()
        
    def recule(self):
        self.i-=1
        if(self.i<1):
            self.uiPLF.PointGauche.setEnabled(False)
        else:
            self.uiPLF.PointGauche.setEnabled(True)
        if(self.i>=len(self.liste_films)-2):
            self.uiPLF.PointDroit.setEnabled(False)
        else:
            self.uiPLF.PointDroit.setEnabled(True)
        
        self.afficheAffiches()
        
    def infosFilm1(self):
        self.infosFilm(self.uiPLF.Titre1.text())    
    def infosFilm2(self):
        self.infosFilm(self.uiPLF.Titre2.text())
    
    
    def infosFilm(self,nom):
        db=bdd.Base_de_films()
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
        
        
        
##/////////////////////////////////////////////////////////////////////
##///////////////////////Classe PageLiensFilms///////////////////////
##/////////////////////////////////////////////////////////////////////
        
class PageLiensFilms2(QtWidgets.QWidget,Ui_PageLiensFilms):
    def __init__(self, parent=None):
        super(PageLiensFilms2,self).__init__(parent)
        self.setupUi(self)  

##/////////////////////////////////////////////////////////////////////
##///////////////////////Classe PageFilmsTrouves///////////////////////
##/////////////////////////////////////////////////////////////////////
        
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
        
##/////////////////////////////////////////////////////////////////////
##///////////////////////Classe PageInfoFilms///////////////////////        
##/////////////////////////////////////////////////////////////////////
        
class PageInfosFilm2(QtWidgets.QWidget,Ui_PageInfosFilm):
    def __init__(self, parent=None):
        super(PageInfosFilm2,self).__init__(parent)
        self.setupUi(self)
        

##/////////////////////////////////////////////////////////////////////
##///////////////////////Classe MainWindow///////////////////////        
##/////////////////////////////////////////////////////////////////////
        
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
        
        self.uiPR.CadreFilmCourant.clicked.connect(self.uiPR.infosFilm0)
      
        self.uiPR.ReturnButton.clicked.connect(self.switchToHome)
        
        self.uiPR.TableFilmsCorrespondants.cellDoubleClicked.connect(self.uiPR.ecritureCell)
        
        ##=============Fonctionnalites de la page de Kevin Bacon=============
        
        self.uiPKB.TitreFilm1.textChanged.connect(self.uiPKB.afficheFilmCourant1)
        self.uiPKB.TitreFilm2.textChanged.connect(self.uiPKB.afficheFilmCourant2)
        self.uiPKB.Browse1.clicked.connect(self.uiPKB.ouvertureHelp1)
        self.uiPKB.Browse2.clicked.connect(self.uiPKB.ouvertureHelp2)
        
        self.uiPKB.ReturnButton.clicked.connect(self.switchToHome)
        
        self.uiPKB.Search.clicked.connect(self.uiPKB.trouveLiens)
        
        
        
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
 
##/////////////////////////////////////////////////////////////////////    
##///////////////////////Main///////////////////////
##/////////////////////////////////////////////////////////////////////
    
if __name__ == '__main__':
    
    ##=============Initialisation des differentes pages=============
    app = QtWidgets.QApplication(sys.argv)

    
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())