# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageRechercheFilms.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PageRechercheFilms(object):
    def setupUi(self, PageRechercheFilms):
        PageRechercheFilms.setObjectName("PageRechercheFilms")
        PageRechercheFilms.resize(800, 500)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PageRechercheFilms.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Hebrew")
        font.setPointSize(14)
        PageRechercheFilms.setFont(font)
        self.ReponseID = QLineEdit2(PageRechercheFilms)
        self.ReponseID.setGeometry(QtCore.QRect(40, 145, 141, 21))
        self.ReponseID.setText("")
        self.ReponseID.setObjectName("ReponseID")
        self.Action = QtWidgets.QCheckBox(PageRechercheFilms)
        self.Action.setGeometry(QtCore.QRect(50, 250, 101, 20))
        self.Action.setObjectName("Action")
        self.Adventure = QtWidgets.QCheckBox(PageRechercheFilms)
        self.Adventure.setGeometry(QtCore.QRect(50, 290, 101, 20))
        self.Adventure.setObjectName("Adventure")
        self.Comedy = QtWidgets.QCheckBox(PageRechercheFilms)
        self.Comedy.setGeometry(QtCore.QRect(50, 270, 121, 20))
        self.Comedy.setObjectName("Comedy")
        self.QuestionID = QtWidgets.QLabel(PageRechercheFilms)
        self.QuestionID.setGeometry(QtCore.QRect(40, 115, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.QuestionID.setFont(font)
        self.QuestionID.setObjectName("QuestionID")
        self.QuestionGenres = QtWidgets.QLabel(PageRechercheFilms)
        self.QuestionGenres.setGeometry(QtCore.QRect(40, 230, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.QuestionGenres.setFont(font)
        self.QuestionGenres.setObjectName("QuestionGenres")
        self.SearchButton = QtWidgets.QPushButton(PageRechercheFilms)
        self.SearchButton.setGeometry(QtCore.QRect(40, 390, 113, 32))
        self.SearchButton.setObjectName("SearchButton")
        self.ReturnButton = QtWidgets.QPushButton(PageRechercheFilms)
        self.ReturnButton.setGeometry(QtCore.QRect(40, 420, 113, 32))
        self.ReturnButton.setObjectName("ReturnButton")
        self.TitreFilmCourant = QtWidgets.QLabel(PageRechercheFilms)
        self.TitreFilmCourant.setGeometry(QtCore.QRect(410, 470, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.TitreFilmCourant.setFont(font)
        self.TitreFilmCourant.setAlignment(QtCore.Qt.AlignCenter)
        self.TitreFilmCourant.setObjectName("TitreFilmCourant")
        self.AfficheFilmCourant = QtWidgets.QLabel(PageRechercheFilms)
        self.AfficheFilmCourant.setEnabled(True)
        self.AfficheFilmCourant.setGeometry(QtCore.QRect(470, 90, 251, 371))
        self.AfficheFilmCourant.setText("")
        self.AfficheFilmCourant.setPixmap(QtGui.QPixmap("Images/classic-poster1-movie.jpg"))
        self.AfficheFilmCourant.setScaledContents(True)
        self.AfficheFilmCourant.setObjectName("AfficheFilmCourant")
        self.HelpButton = QtWidgets.QPushButton(PageRechercheFilms)
        self.HelpButton.setGeometry(QtCore.QRect(190, 140, 113, 32))
        self.HelpButton.setObjectName("HelpButton")
        self.label = QtWidgets.QLabel(PageRechercheFilms)
        self.label.setGeometry(QtCore.QRect(0, -10, 781, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(234, 144, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 144, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 243, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.retranslateUi(PageRechercheFilms)
        QtCore.QMetaObject.connectSlotsByName(PageRechercheFilms)

    def retranslateUi(self, PageRechercheFilms):
        _translate = QtCore.QCoreApplication.translate
        PageRechercheFilms.setWindowTitle(_translate("PageRechercheFilms", "Form"))
        self.Action.setText(_translate("PageRechercheFilms", "Action"))
        self.Adventure.setText(_translate("PageRechercheFilms", "Comedy"))
        self.Comedy.setText(_translate("PageRechercheFilms", "Adventure"))
        self.QuestionID.setText(_translate("PageRechercheFilms", "Enter the title of a movie you liked"))
        self.QuestionGenres.setText(_translate("PageRechercheFilms", "Which kind of movie do you want to see ?"))
        self.SearchButton.setText(_translate("PageRechercheFilms", "Search"))
        self.ReturnButton.setText(_translate("PageRechercheFilms", "Return"))
        self.TitreFilmCourant.setText(_translate("PageRechercheFilms", "STAR WARS I"))
        self.HelpButton.setText(_translate("PageRechercheFilms", "Need help ?"))
        self.label.setText(_translate("PageRechercheFilms", "FILM RECOMANDATION"))

from QLineEdit2 import QLineEdit2
