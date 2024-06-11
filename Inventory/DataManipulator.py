from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

import sqlite3

class DataManipulator:
    def __init__(self) -> None:
        pass

    def selectionChanged(self, selected, deselected):pass
    
    def prepareAdd(self): pass
    def prepareUpdate(self):pass

    def dashboardOpen(self): pass
    def cancel(self):pass

    def addNewData(self): pass
    def updateData(self): pass
    def deleteData(self): pass

    def refreshData(self): pass
    def searchData(self): pass

    def getLastID(self): pass