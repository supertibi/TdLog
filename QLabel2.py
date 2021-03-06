#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:43:55 2018

@author: Clarisse
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

class QLabel2(QtWidgets.QLabel):
    def enterEvent(self, event):
        if(self.isEnabled()):
            self.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.setLineWidth(3)

    def leaveEvent(self, event):
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        
    clicked=pyqtSignal()

    def mousePressEvent(self,event):
        if(self.underMouse()):
            self.clicked.emit()
