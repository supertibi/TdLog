#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:28:55 2018

@author: Clarisse
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

import numpy as np
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import psycopg2
from common_keywords_build import retrieve_most_common_keywords_list
from common_metadata_build import retrieve_most_common_genres_list
import bdd

class QLineEdit2(QtWidgets.QLineEdit):
    pressed=pyqtSignal()
    def enterPressed(self,event):
#        liste_de_reco=bdd.recomandation(self.text())
#        self.pressed.emit(liste_de_reco)
        self.pressed.emit()
        