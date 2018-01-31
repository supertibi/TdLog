#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:43:55 2018

@author: Clarisse
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

class QLabel3(QtWidgets.QLabel):
    def enterEvent(self, event):
        self.setGeometry(self.x()-10,self.y()-10,self.width()+20,self.height()+20)
    def leaveEvent(self, event):
        self.setGeometry(self.x()+10,self.y()+10,self.width()-20,self.height()-20)
        
    clicked=pyqtSignal()

    def mousePressEvent(self,event):
        if(self.underMouse()):
            self.clicked.emit()
