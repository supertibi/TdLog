# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageFilmsTrouves.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PageFilmsTrouves(object):
    def setupUi(self, PageFilmsTrouves):
        PageFilmsTrouves.setObjectName("PageFilmsTrouves")
        PageFilmsTrouves.resize(800, 500)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PageFilmsTrouves.setPalette(palette)
        self.AfficheFilm2 = QtWidgets.QLabel(PageFilmsTrouves)
        self.AfficheFilm2.setGeometry(QtCore.QRect(290, 100, 220, 320))
        self.AfficheFilm2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AfficheFilm2.setText("")
        self.AfficheFilm2.setPixmap(QtGui.QPixmap("Images/classic-poster1-movie.jpg"))
        self.AfficheFilm2.setScaledContents(True)
        self.AfficheFilm2.setObjectName("AfficheFilm2")
        self.DateSortie1 = QtWidgets.QLabel(PageFilmsTrouves)
        self.DateSortie1.setGeometry(QtCore.QRect(30, 450, 241, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.DateSortie1.setPalette(palette)
        self.DateSortie1.setAlignment(QtCore.Qt.AlignCenter)
        self.DateSortie1.setObjectName("DateSortie1")
        self.TitreFilm3 = QtWidgets.QLabel(PageFilmsTrouves)
        self.TitreFilm3.setGeometry(QtCore.QRect(530, 430, 241, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(251, 252, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 252, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TitreFilm3.setPalette(palette)
        self.TitreFilm3.setAlignment(QtCore.Qt.AlignCenter)
        self.TitreFilm3.setObjectName("TitreFilm3")
        self.AfficheFilm3 = QtWidgets.QLabel(PageFilmsTrouves)
        self.AfficheFilm3.setGeometry(QtCore.QRect(540, 100, 220, 320))
        self.AfficheFilm3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AfficheFilm3.setText("")
        self.AfficheFilm3.setPixmap(QtGui.QPixmap("Images/classic-poster1-movie.jpg"))
        self.AfficheFilm3.setScaledContents(True)
        self.AfficheFilm3.setObjectName("AfficheFilm3")
        self.DateSortie2 = QtWidgets.QLabel(PageFilmsTrouves)
        self.DateSortie2.setGeometry(QtCore.QRect(280, 450, 241, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.DateSortie2.setPalette(palette)
        self.DateSortie2.setAlignment(QtCore.Qt.AlignCenter)
        self.DateSortie2.setObjectName("DateSortie2")
        self.DateSortie3 = QtWidgets.QLabel(PageFilmsTrouves)
        self.DateSortie3.setGeometry(QtCore.QRect(530, 450, 241, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.DateSortie3.setPalette(palette)
        self.DateSortie3.setAlignment(QtCore.Qt.AlignCenter)
        self.DateSortie3.setObjectName("DateSortie3")
        self.TitreFilm1 = QtWidgets.QLabel(PageFilmsTrouves)
        self.TitreFilm1.setGeometry(QtCore.QRect(30, 430, 241, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TitreFilm1.setPalette(palette)
        self.TitreFilm1.setAlignment(QtCore.Qt.AlignCenter)
        self.TitreFilm1.setObjectName("TitreFilm1")
        self.AfficheFilm1 = QtWidgets.QLabel(PageFilmsTrouves)
        self.AfficheFilm1.setGeometry(QtCore.QRect(40, 100, 220, 320))
        self.AfficheFilm1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AfficheFilm1.setText("")
        self.AfficheFilm1.setPixmap(QtGui.QPixmap("Images/classic-poster1-movie.jpg"))
        self.AfficheFilm1.setScaledContents(True)
        self.AfficheFilm1.setObjectName("AfficheFilm1")
        self.TitreFilm2 = QtWidgets.QLabel(PageFilmsTrouves)
        self.TitreFilm2.setGeometry(QtCore.QRect(280, 430, 241, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 228, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TitreFilm2.setPalette(palette)
        self.TitreFilm2.setAlignment(QtCore.Qt.AlignCenter)
        self.TitreFilm2.setObjectName("TitreFilm2")
        self.TitreLabel = QtWidgets.QLabel(PageFilmsTrouves)
        self.TitreLabel.setGeometry(QtCore.QRect(0, -10, 781, 81))
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
        self.TitreLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.TitreLabel.setFont(font)
        self.TitreLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TitreLabel.setObjectName("TitreLabel")
        self.Cadre1 = QLabel2(PageFilmsTrouves)
        self.Cadre1.setGeometry(QtCore.QRect(40, 100, 220, 320))
        self.Cadre1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cadre1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Cadre1.setText("")
        self.Cadre1.setScaledContents(True)
        self.Cadre1.setObjectName("Cadre1")
        self.Cadre3 = QLabel2(PageFilmsTrouves)
        self.Cadre3.setGeometry(QtCore.QRect(540, 100, 220, 320))
        self.Cadre3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cadre3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Cadre3.setText("")
        self.Cadre3.setScaledContents(True)
        self.Cadre3.setObjectName("Cadre3")
        self.Cadre2 = QLabel2(PageFilmsTrouves)
        self.Cadre2.setGeometry(QtCore.QRect(290, 100, 220, 320))
        self.Cadre2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cadre2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Cadre2.setText("")
        self.Cadre2.setScaledContents(True)
        self.Cadre2.setObjectName("Cadre2")

        self.retranslateUi(PageFilmsTrouves)
        QtCore.QMetaObject.connectSlotsByName(PageFilmsTrouves)

    def retranslateUi(self, PageFilmsTrouves):
        _translate = QtCore.QCoreApplication.translate
        PageFilmsTrouves.setWindowTitle(_translate("PageFilmsTrouves", "Form"))
        self.DateSortie1.setText(_translate("PageFilmsTrouves", "Date de sortie"))
        self.TitreFilm3.setText(_translate("PageFilmsTrouves", "Titre"))
        self.DateSortie2.setText(_translate("PageFilmsTrouves", "Date de sortie"))
        self.DateSortie3.setText(_translate("PageFilmsTrouves", "Date de sortie"))
        self.TitreFilm1.setText(_translate("PageFilmsTrouves", "Titre"))
        self.TitreFilm2.setText(_translate("PageFilmsTrouves", "Titre"))
        self.TitreLabel.setText(_translate("PageFilmsTrouves", "MOVIE RECOMMENDATION"))

from QLabel2 import QLabel2