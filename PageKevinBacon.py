# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageKevinBacon.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PageKevinBacon(object):
    def setupUi(self, PageKevinBacon):
        PageKevinBacon.setObjectName("PageKevinBacon")
        PageKevinBacon.resize(779, 489)
        self.SearchButton = QtWidgets.QPushButton(PageKevinBacon)
        self.SearchButton.setGeometry(QtCore.QRect(640, 65, 113, 32))
        self.SearchButton.setObjectName("SearchButton")
        self.SearchTextBar = QtWidgets.QLineEdit(PageKevinBacon)
        self.SearchTextBar.setGeometry(QtCore.QRect(32, 70, 601, 21))
        self.SearchTextBar.setObjectName("SearchTextBar")

        self.retranslateUi(PageKevinBacon)
        QtCore.QMetaObject.connectSlotsByName(PageKevinBacon)

    def retranslateUi(self, PageKevinBacon):
        _translate = QtCore.QCoreApplication.translate
        PageKevinBacon.setWindowTitle(_translate("PageKevinBacon", "Form"))
        self.SearchButton.setText(_translate("PageKevinBacon", "Search"))

