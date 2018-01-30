#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:22:13 2018

@author: Clarisse
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

class QTableWidget2(QtWidgets.QTableWidget):
        
    clicked=pyqtSignal()

    def cellClicked(self,event):
        print("double")
        self.doubleClicked.emit()
    