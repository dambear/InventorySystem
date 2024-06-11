from asyncio.windows_events import NULL
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from UIManager import *

from Message import Messsage
import sqlite3

from DataManipulator import DataManipulator

class Home(DataManipulator):
    def __init__(self, data, ui) -> None:
        self.ui = ui
        self.data = data

        self.uim = UIManager(self.ui)

        self.createTable()

        self.ui.home_btn.clicked.connect(lambda: self.uim.SwitchFrame('Home'))

        record = self.data.showDataLimited('SUM(orderTotal)','OrderTbl')
        self.ui.homeOverallSale.setText(str(record[0][0]))

        record = self.data.showDataSpecific('COUNT(*)','ProductTbl','Where productAvailability = \'Available\'')
        self.ui.itemsAvailable.setText(str(record[0][0]))

        record = self.data.showDataLimited('COUNT(*)','CustomerTbl')
        self.ui.noOfCustomer.setText(str(record[0][0]))

        record = self.data.showDataLimited('SUM(quantity)','OrderItemTbl')
        self.ui.noOfItemSold.setText(str(record[0][0]))
    
    def createTable(self):

        self.data.create_table("\'CustomerTbl\'",
        """"customerID"	INTEGER NOT NULL,
            "customerFName"	TEXT NOT NULL,
            "customerLName"	TEXT NOT NULL,
            "customerAddress"	TEXT,
            "customerContact"	INTEGER,
            PRIMARY KEY("customerID" AUTOINCREMENT)""")
        
        self.data.create_table("\'OrderItemTbl\'",
        """"orderID"	INTEGER NOT NULL,
            "productID"	INTEGER NOT NULL,
            "quantity"	INTEGER NOT NULL,
            "salePrice"	NUMERIC NOT NULL,
            FOREIGN KEY("productID") REFERENCES "ProductTbl",
            FOREIGN KEY("orderID") REFERENCES "OrderTbl" """)
        
        self.data.create_table("\'OrderTbl\'",
        """"orderID"	INTEGER NOT NULL,
            "customerID"	INTEGER NOT NULL,
            "orderDate"	TEXT NOT NULL,
            "orderTotal"	NUMERIC NOT NULL,
            PRIMARY KEY("orderID"),
            FOREIGN KEY("customerID") REFERENCES "CustomerTbl" """)
        
        self.data.create_table("\'ProductTbl\'",
        """"productID"	INTEGER NOT NULL,
            "productName"	TEXT NOT NULL,
            "productPrice"	NUMERIC DEFAULT 0.0,
            "productOnHand"	INTEGER DEFAULT 1,
            "productDesc"	TEXT,
            "productAvailability"	TEXT NOT NULL DEFAULT 'Available',
            PRIMARY KEY("productID" AUTOINCREMENT)""")
    
    """CREATE TABLE "CustomerTbl" (
        "customerID"	INTEGER NOT NULL,
        "customerFName"	TEXT NOT NULL,
        "customerLName"	TEXT NOT NULL,
        "customerAddress"	TEXT,
        "customerContact"	INTEGER,
        PRIMARY KEY("customerID" AUTOINCREMENT)
    );"""

    """CREATE TABLE "OrderItemTbl" (
        "orderID"	INTEGER NOT NULL,
        "productID"	INTEGER NOT NULL,
        "quantity"	INTEGER NOT NULL,
        "salePrice"	NUMERIC NOT NULL,
        FOREIGN KEY("productID") REFERENCES "ProductTbl",
        FOREIGN KEY("orderID") REFERENCES "OrderTbl"
    );"""

    """CREATE TABLE "OrderTbl" (
        "orderID"	INTEGER NOT NULL,
        "customerID"	INTEGER NOT NULL,
        "orderDate"	TEXT NOT NULL,
        "orderTotal"	NUMERIC NOT NULL,
        PRIMARY KEY("orderID"),
        FOREIGN KEY("customerID") REFERENCES "CustomerTbl"
    );"""
    """CREATE TABLE "ProductTbl" (
        "productID"	INTEGER NOT NULL,
        "productName"	TEXT NOT NULL,
        "productPrice"	NUMERIC DEFAULT 0.0,
        "productOnHand"	INTEGER DEFAULT 1,
        "productDesc"	TEXT,
        "productAvailability"	TEXT NOT NULL DEFAULT 'Available',
        PRIMARY KEY("productID" AUTOINCREMENT)
    );"""