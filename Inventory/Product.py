from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from UIManager import *

from Message import Messsage
import sqlite3

from DataManipulator import DataManipulator

class Product(DataManipulator):
    def __init__(self, data, ui) -> None:
        self.ui = ui
        self.data = data
        
        self.selectedRow = -1
        self.selectedColumn = -1

        self.uim = UIManager(self.ui)

        self.refreshData()

        self.ui.product_btn.clicked.connect(lambda: self.dashboardOpen())
        self.ui.add_prod_btn.clicked.connect(lambda: self.prepareAdd())
        self.ui.upd_prod_btn.clicked.connect(lambda: self.prepareUpdate())

        self.ui.prodAdd_btn.clicked.connect(lambda: self.addNewData())
        self.ui.prodAddCancel_btn.clicked.connect(lambda: self.cancel())

        self.ui.prodUpt_btn.clicked.connect(lambda: self.updateData())
        self.ui.prodUptCancel_btn.clicked.connect(lambda: self.cancel())

        self.ui.del_prod_btn.clicked.connect(lambda: self.deleteData())
        self.ui.prod_search_btn.clicked.connect(lambda: self.searchData())

        self.ui.product_tbl.selectionModel().selectionChanged.connect(self.selectionChanged)
    
        self.ui.prodAddPrice.setValidator(QDoubleValidator())
        self.ui.prodAddOnhand.setValidator(QIntValidator())
        self.ui.prodUptPrice.setValidator(QIntValidator())
        self.ui.prodUptOnhand.setValidator(QIntValidator())
    
    def selectionChanged(self, selected, deselected):
        for i in selected.indexes():
            self.selectedRow = i.row() 
            self.selectedColumn = i.column()
        for i in deselected.indexes():
            self.selectedRow = -1 
            self.selectedColumn = -1

    def prepareAdd(self):
        self.getLastID()
        self.uim.SwitchFrame('AddProd')

    def prepareUpdate(self):

        row = self.selectedRow
        if not row == -1:

            id = self.ui.product_tbl.item(row, 0).text()
            pName = self.ui.product_tbl.item(row, 1).text()
            price = self.ui.product_tbl.item(row, 2).text()
            Onhand = self.ui.product_tbl.item(row, 3).text()
            desc = self.ui.product_tbl.item(row, 4).text()
            availability = self.ui.product_tbl.item(row, 5).text()

            self.ui.prodUptId.setText(id)
            self.ui.prodUptName.setText(pName)
            self.ui.prodUptPrice.setText(price)
            self.ui.prodUptOnhand.setText(Onhand)
            self.ui.prodUptDescription.setText(desc)
            
            if availability == 'Available':
                self.ui.prodUptAvailabilityComboBox.setCurrentText('Available')
            else:
                self.ui.prodUptAvailabilityComboBox.setCurrentText('Not Available')

            self.uim.SwitchFrame('UptProd')
            
        else:
            Messsage("Click a data first!", self.ui)


    def dashboardOpen(self):
        self.uim.SwitchFrame('Product')
        self.refreshData()
    
    def cancel(self):
        self.dashboardOpen()

        self.ui.prodUptId.clear()
        self.ui.prodUptName.clear()
        self.ui.prodUptPrice.clear()
        self.ui.prodUptOnhand.clear()
        self.ui.prodUptDescription.clear()
        self.ui.prodAddAvailabilityComboBox.setCurrentText('Available')

        self.ui.prodAddId.clear()
        self.ui.prodAddName.clear()
        self.ui.prodAddPrice.clear()
        self.ui.prodAddOnhand.clear()
        self.ui.prodAddDescription.clear()
        self.ui.prodAddAvailabilityComboBox.setCurrentText('Available')

    def addNewData(self):
        if self.ui.prodAddName.text() == "" or self.ui.prodAddPrice.text() == "" or self.ui.prodAddOnhand.text() == "" or self.ui.prodAddAvailabilityComboBox.currentText() == "":

            Messsage("Fill all the field!", self.ui)

        else:
            try:
                self.data.addData('ProductTbl',

                '{0},\'{1}\',{2},{3},\'{4}\',\'{5}\''.

                format(
                    self.ui.prodAddId.text(),#0
                    self.ui.prodAddName.text(),#1
                    self.ui.prodAddPrice.text(),#2
                    self.ui.prodAddOnhand.text(),#3
                    self.ui.prodAddDescription.text(),#4
                    self.ui.prodAddAvailabilityComboBox.currentText()#5
                ))

                Messsage("Success!", self.ui)
            except Exception as e:
                print(e)
                Messsage("An error encountered", self.ui)

                
    def updateData(self):
        try:
            self.data.updateData('ProductTbl',
            'productName = \'{0}\',productPrice = {1},productOnHand = {2},productDesc = \'{3}\',productAvailability = \'{4}\''.

            format(
                self.ui.prodUptName.text(),#0
                self.ui.prodUptPrice.text(),#1
                self.ui.prodUptOnhand.text(),#2
                self.ui.prodUptDescription.text(),#3
                self.ui.prodUptAvailabilityComboBox.currentText()#3
                
            )
            , 'productID = {0}'.format(self.ui.prodUptId.text())
            )
            Messsage("Success!", self.ui)
        except Exception as e:
            print(e)
            Messsage("An error encountered", self.ui)


    def deleteData(self): 
        row = self.selectedRow
        if not row == -1:
            try:
                self.data.deleteData('ProductTbl','productID = {0}'.format(self.ui.product_tbl.item(row, 0).text()))

                self.refreshData()
            except Exception as e:
                print(e)
                Messsage("An error encountered", self.ui)

        else:
            Messsage("Click a data first!", self.ui)


    def refreshData(self):
        product_records = self.data.showData("ProductTbl")#get data of product table check DBManager script for more

        self.uim.RefreshTable(product_records, self.ui.product_tbl)

    def searchData(self):
        if not self.ui.prod_search.text() == "":
            records = self.data.showDataSpecific("*",
            "ProductTbl",
            "WHERE productName LIKE \'%{0}%\'".format(self.ui.prod_search.text()))

            self.uim.RefreshTable(records, self.ui.product_tbl)
        else:
            self.refreshData()
    
    def getLastID(self):
        count = self.ui.product_tbl.rowCount()
        row = count - 1

        newid = int(self.ui.product_tbl.item(row, 0).text())+1

        self.ui.prodAddId.setText("{}".format(newid))

