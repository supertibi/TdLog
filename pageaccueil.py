# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageAccueil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PageAccueil(object):
    def setupUi(self, PageAccueil):
        PageAccueil.setObjectName("PageAccueil")
        PageAccueil.resize(800, 500)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PageAccueil.setPalette(palette)
        PageAccueil.setMouseTracking(True)
        self.HomeLabel = QtWidgets.QLabel(PageAccueil)
        self.HomeLabel.setGeometry(QtCore.QRect(0, -20, 771, 91))
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
        self.HomeLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.HomeLabel.setFont(font)
        self.HomeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.HomeLabel.setObjectName("HomeLabel")
        self.KevinBacon = QLabel2(PageAccueil)
        self.KevinBacon.setGeometry(QtCore.QRect(50, 70, 271, 341))
        self.KevinBacon.setMouseTracking(True)
        self.KevinBacon.setFrameShape(QtWidgets.QFrame.Box)
        self.KevinBacon.setLineWidth(12)
        self.KevinBacon.setMidLineWidth(10)
        self.KevinBacon.setText("")
        self.KevinBacon.setPixmap(QtGui.QPixmap("Images/kevin-bacon1.jpg"))
        self.KevinBacon.setScaledContents(True)
        self.KevinBacon.setObjectName("KevinBacon")
        self.AffichesFilms = QLabel2(PageAccueil)
        self.AffichesFilms.setGeometry(QtCore.QRect(450, 70, 261, 341))
        self.AffichesFilms.setMouseTracking(True)
        self.AffichesFilms.setFrameShape(QtWidgets.QFrame.Box)
        self.AffichesFilms.setLineWidth(15)
        self.AffichesFilms.setText("")
        self.AffichesFilms.setPixmap(QtGui.QPixmap("Images/affiches_films_otto_preminger.jpg"))
        self.AffichesFilms.setScaledContents(True)
        self.AffichesFilms.setObjectName("AffichesFilms")
        self.KevinBaconLabel = QtWidgets.QLabel(PageAccueil)
        self.KevinBaconLabel.setGeometry(QtCore.QRect(30, 400, 301, 81))
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
        self.KevinBaconLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.KevinBaconLabel.setFont(font)
        self.KevinBaconLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.KevinBaconLabel.setObjectName("KevinBaconLabel")
        self.FilmRecoLabel = QtWidgets.QLabel(PageAccueil)
        self.FilmRecoLabel.setGeometry(QtCore.QRect(430, 400, 331, 81))
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
        self.FilmRecoLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.FilmRecoLabel.setFont(font)
        self.FilmRecoLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.FilmRecoLabel.setObjectName("FilmRecoLabel")

        self.retranslateUi(PageAccueil)
        QtCore.QMetaObject.connectSlotsByName(PageAccueil)

    def retranslateUi(self, PageAccueil):
        _translate = QtCore.QCoreApplication.translate
        PageAccueil.setWindowTitle(_translate("PageAccueil", "PageAccueil"))
        self.HomeLabel.setText(_translate("PageAccueil", "HOME"))
        self.KevinBaconLabel.setText(_translate("PageAccueil", "KEVIN BACON"))
        self.FilmRecoLabel.setText(_translate("PageAccueil", "FILM RECOMANDATION"))

from QLabel2 import QLabel2