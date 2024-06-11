from asyncio.windows_events import NULL
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from UIManager import *

from Message import Messsage
import sqlite3

from DataManipulator import DataManipulator

class Customer(DataManipulator):
    def __init__(self, data, ui) -> None:
        self.ui = ui
        self.data = data

        self.selectedRow = -1
        self.selectedColumn = -1

        self.uim = UIManager(self.ui)

        self.refreshData()

        self.ui.customer_btn.clicked.connect(lambda: self.dashboardOpen())
        self.ui.add_cust_btn.clicked.connect(lambda: self.prepareAdd())
        self.ui.upd_cust_btn.clicked.connect(lambda: self.prepareUpdate())

        self.ui.custAdd_btn.clicked.connect(lambda: self.addNewData())
        self.ui.custAddCancel_btn.clicked.connect(lambda: self.cancel())

        self.ui.custUpt_btn.clicked.connect(lambda: self.updateData())
        self.ui.custUptCancel_btn.clicked.connect(lambda: self.cancel())

        self.ui.del_cust_btn.clicked.connect(lambda: self.deleteData())
        self.ui.cust_search_btn.clicked.connect(lambda: self.searchData())

        self.ui.customer_tbl.selectionModel().selectionChanged.connect(self.selectionChanged)
    
        self.ui.custAddContactno.setValidator(QIntValidator())
        self.ui.custUptContactno.setValidator(QIntValidator())


    def selectionChanged(self, selected, deselected):
        for i in selected.indexes():
            self.selectedRow = i.row() 
            self.selectedColumn = i.column()
        for i in deselected.indexes():
            self.selectedRow = -1 
            self.selectedColumn = -1

    def prepareAdd(self):
        self.getLastID()
        self.uim.SwitchFrame('AddCust')

    def prepareUpdate(self):
        row = self.selectedRow
        if not row == -1:

            id = self.ui.customer_tbl.item(row, 0).text()
            name = self.ui.customer_tbl.item(row, 1).text().split()
            address = self.ui.customer_tbl.item(row, 2).text()
            contact = self.ui.customer_tbl.item(row, 3).text()

            self.ui.custUptId.setText(id)
            self.ui.custUptFName.setText(name[0])
            self.ui.custUptLName.setText(name[1])
            self.ui.custUptAddress.setText(address)
            self.ui.custUptContactno.setText(contact)

            self.uim.SwitchFrame('UptCust')

        else:
            Messsage("Click a data first!", self.ui)


    def dashboardOpen(self):
        self.uim.SwitchFrame('Customer')
        self.refreshData()
    
    def cancel(self):
        self.dashboardOpen()

        self.ui.custUptId.clear()
        self.ui.custUptFName.clear()
        self.ui.custUptLName.clear()
        self.ui.custUptAddress.clear()
        self.ui.custUptContactno.clear()

        self.ui.custAddId.clear()
        self.ui.custAddFName.clear()
        self.ui.custAddLName.clear()
        self.ui.custAddAddress.clear()
        self.ui.custAddContactno.clear()

    def addNewData(self):
        if self.ui.custAddFName.text() == "" or self.ui.custAddLName.text() == "" or self.ui.custAddAddress.text() == "" or self.ui.custAddContactno.text() == "":

            Messsage("Fill all the field!", self.ui)

        else:
            try:
                self.data.addData('CustomerTbl',

                '{0},\'{1}\',\'{2}\',\'{3}\',{4}'.

                format(
                    self.ui.custAddId.text(),#0
                    self.ui.custAddFName.text(),#1
                    self.ui.custAddLName.text(),#2
                    self.ui.custAddAddress.text(),#3
                    self.ui.custAddContactno.text(),#4
                ))

                Messsage("Success!", self.ui)
            except Exception as e:
                print(e)
                Messsage("An error encountered", self.ui)

                
    def updateData(self):
        try:
            self.data.updateData('CustomerTbl',
            'customerFName = \'{0}\',customerLName = \'{1}\',customerAddress = \'{2}\',customerContact={3}'.

            format(
                self.ui.custUptFName.text(),#0
                self.ui.custUptLName.text(),#1
                self.ui.custUptAddress.text(),#2
                self.ui.custUptContactno.text(),#3
            )
            , 'customerID = {0}'.format(self.ui.custUptId.text())
            )
            Messsage("Success!", self.ui)
        except Exception as e:
            print(e)
            Messsage("An error encountered", self.ui)


    def deleteData(self): 

        row = self.selectedRow
        if not row == -1:
            try:
                self.data.deleteData('CustomerTbl','customerID = {0}'.format(self.ui.customer_tbl.item(row, 0).text()))

                self.refreshData()
            except Exception as e:
                print(e)
                Messsage("An error encountered", self.ui)

        else:
            Messsage("Click a data first!", self.ui)


    def refreshData(self):
        customer_records = self.data.showDataLimited("customerID, customerFName || \" \" || customerLName AS \'Name\', customerAddress, customerContact","CustomerTbl")#get data of customer table check DBManager script for more

        self.uim.RefreshTable(customer_records, self.ui.customer_tbl)

    def searchData(self):
        if not self.ui.cust_search.text() == "":
            customer_records = self.data.showDataSpecific("customerID, customerFName || \" \" || customerLName AS \'Name\', customerAddress, customerContact",
            "CustomerTbl",
            "WHERE Name LIKE \'%{0}%\'".format(self.ui.cust_search.text()))

            self.uim.RefreshTable(customer_records, self.ui.customer_tbl)
        else:
            self.refreshData()

    def getLastID(self):
        count = self.ui.customer_tbl.rowCount()
        row = count - 1

        newid = int(self.ui.customer_tbl.item(row, 0).text())+1

        self.ui.custAddId.setText("{}".format(newid))
