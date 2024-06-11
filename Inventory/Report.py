from asyncio.windows_events import NULL
from tkinter import HIDDEN
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

from UIManager import *

from Message import Messsage
import sqlite3

from DataManipulator import DataManipulator

class Report(DataManipulator):
    def __init__(self, data, ui) -> None:
        self.ui = ui
        self.data = data

        self.uim = UIManager(self.ui)

        self.ui.report_btn.clicked.connect(lambda: self.dashboardOpen())
        
        
        #CustReportTable
        self.ui.rep_cust_btn.clicked.connect(lambda: self.CustomerReport())
        
        #ProdReportTable
        self.ui.rep_prod_btn.clicked.connect(lambda: self.ProdReport())
        
        #COrderReportTable
        self.ui.rep_order_btn.clicked.connect(lambda: self.OrderReport())
        
        #SaleReportTable
        self.ui.rep_sale_btn.clicked.connect(lambda: self.SaleReport())
        
        self.ui.rep_search_btn.clicked.connect(lambda: self.searchData())

    def dashboardOpen(self):
        self.uim.SwitchFrame('Report')
        
    
    def CustomerReport(self):
        
        self.ui.frame_rep_cust.setHidden(False)
        self.ui.frame_rep_prod.setHidden(True)
        self.ui.frame_rep_order.setHidden(True)
        self.ui.frame_rep_sale.setHidden(True)
        
        self.ui.rep_search_btn.clicked.connect(lambda: searchData())
        
        def refreshData():
            customerreport = self.data.showDataSpecific("OrderHistoryView.Name AS CustomerName,SUM(OrderHistoryView.orderTotal) totalAmountBought",
            "OrderHistoryView",
            "GROUP BY CustomerName")

            self.uim.RefreshTable(customerreport, self.ui.rep_cust_tbl)
            
            

        def searchData():
            if not self.ui.rep_search.text() == "":
                records = self.data.showDataSpecific("*",
                "CustomerReportView",
                "WHERE CustomerName LIKE \'%{0}%\'".format(self.ui.rep_search.text()))

                self.uim.RefreshTable(records, self.ui.rep_cust_tbl)
            else:
                refreshData()
                
        refreshData()
        
        
    def ProdReport(self):
        self.ui.frame_rep_cust.setHidden(True)
        self.ui.frame_rep_prod.setHidden(False)
        self.ui.frame_rep_order.setHidden(True)
        self.ui.frame_rep_sale.setHidden(True)
        
        self.ui.rep_search_btn.clicked.connect(lambda: searchData())
        
        def refreshData():
            productreport = self.data.showDataSpecific("OrderHistoryView.productName,ProductTbl.productDesc,ProductTbl.productPrice,SUM(OrderHistoryView.quantity) productSold",
            "OrderHistoryView, ProductTbl",
            "WHERE OrderHistoryView.productName = ProductTbl.productName GROUP BY OrderHistoryView.productName")

            self.uim.RefreshTable(productreport, self.ui.rep_prod_tbl)
            
            

        def searchData():
            if not self.ui.rep_search.text() == "":
                records = self.data.showDataSpecific("*",
                "ProductReportView",
                "WHERE productName LIKE \'%{0}%\' OR productSold LIKE \'%{0}%\'".format(self.ui.rep_search.text()))

                self.uim.RefreshTable(records, self.ui.rep_prod_tbl)
            else:
                refreshData()
                
        refreshData()
        
    def OrderReport(self):
        self.ui.frame_rep_cust.setHidden(True)
        self.ui.frame_rep_prod.setHidden(True)
        self.ui.frame_rep_order.setHidden(False)
        self.ui.frame_rep_sale.setHidden(True)
        
        self.ui.rep_search_btn.clicked.connect(lambda: searchData())
        
        def refreshData():
            orderreport = self.data.showDataSpecific("OrderHistoryView.orderDate,OrderHistoryView.Name AS CustomerName,OrderHistoryView.productName,OrderHistoryView.quantity AS productQuantity,OrderHistoryView.orderTotal AS productTotalToPay",
            "OrderHistoryView",
            "")

            self.uim.RefreshTable(orderreport, self.ui.rep_order_tbl)
            
            

        def searchData():
            if not self.ui.rep_search.text() == "":
                records = self.data.showDataSpecific("*",
                "OrderReportView",
                "WHERE productName LIKE \'%{0}%\' OR CustomerName LIKE \'%{0}%\' OR orderDate LIKE \'%{0}%\'".format(self.ui.rep_search.text()))

                self.uim.RefreshTable(records, self.ui.rep_order_tbl)
            else:
                refreshData()
                
        refreshData()
        
        
    def SaleReport(self):
        self.ui.frame_rep_cust.setHidden(True)
        self.ui.frame_rep_prod.setHidden(True)
        self.ui.frame_rep_order.setHidden(True)
        self.ui.frame_rep_sale.setHidden(False)
        
        self.ui.rep_search_btn.clicked.connect(lambda: searchData())
        
        def refreshData():
            salereport = self.data.showDataSpecific("OrderHistoryView.orderDate,OrderHistoryView.productName,SUM(OrderHistoryView.quantity) productSold,SUM(OrderHistoryView.orderTotal) productTotalEarn",
            "OrderHistoryView",
            "GROUP BY OrderHistoryView.orderDate, OrderHistoryView.productName")

            self.uim.RefreshTable(salereport, self.ui.rep_sale_tbl)
            
            

        def searchData():
            if not self.ui.rep_search.text() == "":
                records = self.data.showDataSpecific("*",
                "SaleReportView",
                "WHERE productName LIKE \'%{0}%\' OR orderDate LIKE \'%{0}%\'".format(self.ui.rep_search.text()))

                self.uim.RefreshTable(records, self.ui.rep_sale_tbl)
            else:
                refreshData()
                
        refreshData()
        