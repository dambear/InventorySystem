from typing import OrderedDict
from urllib.request import OpenerDirector
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from DBManager import *
from UIManager import *

from Home import *
from Customer import *
from Order import *
from OrderForm import *
from Product import *
from Report import *

from Message import Messsage
import sys
import datetime

def close(): 
    sys.exit(0)

app = QtWidgets.QApplication([])
ui = uic.loadUi("default.ui")#change according to the UI name

ui.setFixedSize(ui.size())#disable resize
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | #remove frame borders
                                      QtCore.Qt.WindowStaysOnTopHint)

ui.setWindowFlags(flags)

db = DBManager()
uim = UIManager(ui)

Home(db, ui)
Customer(db,ui)
Product(db,ui)
Order(db,ui)
OrderForm(db,ui)
Report(db,ui)

ui.quit_btn.clicked.connect(close)
e = datetime.datetime.now()


ui.dateTimeText.setText(e.strftime("%d-%m-%Y %H:%M"))

ui.show()
app.exec()

