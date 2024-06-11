from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

from UIManager import *

from Message import Messsage
import sqlite3

from DataManipulator import DataManipulator

class Order(DataManipulator):
    def __init__(self, data, ui) -> None:
        self.ui = ui
        self.data = data

        self.uim = UIManager(self.ui)

        self.refreshData()

        self.ui.order_btn.clicked.connect(lambda: self.dashboardOpen())
        
        self.ui.order_search_btn.clicked.connect(lambda: self.searchData())
    
    def dashboardOpen(self):
        self.uim.SwitchFrame('Order')
        self.refreshData()

    def refreshData(self):
        orderhistory = self.data.showDataSpecific("OrderTbl.orderID, CustomerTbl.customerFName || ' ' || CustomerTbl.customerLName AS Name, OrderTbl.orderDate, ProductTbl.productName, ProductTbl.productPrice, OrderItemTbl.quantity, OrderItemTbl.salePrice, OrderTbl.orderTotal",
        "OrderItemTbl, OrderTbl, CustomerTbl, ProductTbl",
        "WHERE OrderItemTbl.orderID = OrderTbl.orderID AND OrderItemTbl.productID = ProductTbl.productID AND OrderTbl.customerID = CustomerTbl.customerID ORDER BY OrderTbl.orderID DESC")

        self.uim.RefreshTable(orderhistory, self.ui.order_tbl)
        
    def searchData(self):
        if not self.ui.order_search.text() == "":
            records = self.data.showDataSpecific("*",
            "OrderHistoryView",
            "WHERE productName LIKE \'%{0}%\' OR Name LIKE \'%{0}%\' OR orderDate LIKE \'%{0}%\'".format(self.ui.order_search.text()))

            self.uim.RefreshTable(records, self.ui.order_tbl)
        else:
            self.refreshData()
        
        

