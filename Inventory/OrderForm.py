from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from UIManager import *
from datetime import date
from Message import Messsage
import sqlite3

from DataManipulator import DataManipulator

class OrderForm(DataManipulator):
    def __init__(self, data, ui) -> None:
        self.ui = ui
        self.data = data

        self.totalToPay = 0
        
        self.selectedRow = -1
        self.selectedColumn = -1

        self.uim = UIManager(self.ui)

        self.ui.order_form_btn.clicked.connect(lambda: self.dashboardOpen())

        self.setOrderID()
        self.customerDropDown()
        self.productDropDown()
        self.ui.orderDate_of.setDate(date.today())

        self.ui.orderItemQuantity_of.setValidator(QIntValidator())
        self.ui.orderCash_of.setValidator(QIntValidator())

        self.ui.orderProdComboBox_of.currentIndexChanged.connect(self.showPrice)
        self.ui.orderAddItem_of_btn.clicked.connect(self.addItemToPay)
        self.ui.orderRemItem_of_btn.clicked.connect(self.deleteItem)
        self.ui.orderPay_of_btn.clicked.connect(self.pay)
        self.ui.orderNewOrder_of_btn.clicked.connect(self.newOrder)
        

        self.ui.orderItem_tbl.selectionModel().selectionChanged.connect(self.selectionChanged)
        self.ui.orderCash_of.editingFinished.connect(self.calculateChange)
    
    def dashboardOpen(self):
        self.uim.SwitchFrame('OrderForm')
        self.newOrder()
    def selectionChanged(self, selected, deselected):
        for i in selected.indexes():
            self.selectedRow = i.row() 
            self.selectedColumn = i.column()
        for i in deselected.indexes():
            self.selectedRow = -1 
            self.selectedColumn = -1

    def setOrderID(self):
        record = self.data.showDataSpecific('*','OrderTbl','ORDER BY orderID DESC LIMIT 1')
        newID = int(record[0][0])+1
        self.ui.orderID_of.setText('{}'.format(newID))
    
    def customerDropDown(self):
        self.ui.orderCustComboBox_of.clear()
        record = self.data.showDataSpecific("customerFName || \" \" || customerLName AS \'Name\'",'CustomerTbl','ORDER BY Name ASC')
        for row in record:
            self.ui.orderCustComboBox_of.addItem(str(row[0]), row[0])

    def productDropDown(self):
        self.ui.orderProdComboBox_of.clear()
        record = self.data.showDataSpecific("productName",'ProductTbl','WHERE productOnHand > 0 ORDER BY productName ASC')
        for row in record:
            self.ui.orderProdComboBox_of.addItem(str(row[0]), row[0])

    def showPrice(self):
        if not self.ui.orderProdComboBox_of.currentText() == "":
            record = self.data.showDataSpecific("productPrice",'ProductTbl','WHERE productName = \'{}\''.format(self.ui.orderProdComboBox_of.currentText()))
            self.ui.orderItemPrice_of.setText(str(record[0][0]))

    def addItemToPay(self):
        if not self.ui.orderItemQuantity_of.text() == "" and not self.ui.orderItemPrice_of.text() == "":
            row = self.ui.orderItem_tbl.rowCount()
            self.ui.orderItem_tbl.insertRow(row)

            name = QtWidgets.QTableWidgetItem(self.ui.orderProdComboBox_of.currentText())
            self.ui.orderItem_tbl.setItem(row,0, name )

            price = QtWidgets.QTableWidgetItem(self.ui.orderItemPrice_of.text())
            self.ui.orderItem_tbl.setItem(row,1, price )

            quantity = QtWidgets.QTableWidgetItem(self.ui.orderItemQuantity_of.text())
            self.ui.orderItem_tbl.setItem(row,2, quantity)

            totalPrice = float(self.ui.orderItemPrice_of.text()) * int(self.ui.orderItemQuantity_of.text())
            itemTotalPrice = QtWidgets.QTableWidgetItem(str(totalPrice))
            self.ui.orderItem_tbl.setItem(row,3, itemTotalPrice)
            
            self.totalToPay += totalPrice

            self.ui.orderTotalToPay_of.setText(str(self.totalToPay))

        else:
            Messsage("Some field is empty",self.ui)

    def deleteItem(self):
        row = self.selectedRow
        if not row == -1:
            self.totalToPay -= float(self.ui.orderItem_tbl.item(row,3).text())

            self.ui.orderTotalToPay_of.setText(str(self.totalToPay))
            self.ui.orderItem_tbl.removeRow(row)
        else:
            Messsage("Click an item first!", self.ui)
    
    def calculateChange(self):
        cash = float(self.ui.orderCash_of.text())
        amount = float(self.ui.orderTotalToPay_of.text())

        change = cash - amount
        self.ui.orderChange_of.setText(str(change))

    def pay(self):
        try:
            record = self.data.showDataSpecific("customerID ,customerFName || \" \" || customerLName AS \'Name\'",'CustomerTbl','WHERE Name = \'{}\''.format(self.ui.orderCustComboBox_of.currentText()))
            customerID = record[0][0]

            self.data.addData('OrderTbl',
            "{0}, {1}, \'{2}\', {3}".
            
            format(
                self.ui.orderID_of.text(),
                str(customerID),
                self.ui.orderDate_of.date().toString('dd-MMM-yy'),
                self.ui.orderTotalToPay_of.text()
            ))

            for row in range(self.ui.orderItem_tbl.rowCount()):
                name = self.ui.orderItem_tbl.item(row, 0).text()
                price = self.ui.orderItem_tbl.item(row, 1).text()
                quantity = self.ui.orderItem_tbl.item(row, 2).text() 
                salePrice = self.ui.orderItem_tbl.item(row, 3).text()

                #print('{} {} {} {}'.format(name,price,quantity,salePrice))
                
                record = self.data.showDataSpecific("productID",'ProductTbl','WHERE productName = \'{}\''.format(name))
                customerID = record[0][0]

                #print(str(customerID))

                self.data.addData('OrderItemTbl',
                "{},{},{},{}".
                format(
                    self.ui.orderID_of.text(),
                    str(customerID),
                    quantity,
                    salePrice
                ) )
            Messsage("Item/s ordered successfully!",self.ui)
        except Exception as e:
            Messsage("Something Went Wrong!",self.ui)
    
    def newOrder(self):
        self.setOrderID()
        self.customerDropDown()
        self.productDropDown()
        self.ui.orderDate_of.setDate(date.today())

        self.ui.orderItemPrice_of.setText(str(0))
        self.ui.orderItemQuantity_of.setText(str(0))
        self.ui.orderCash_of.setText(str(0))
        self.ui.orderTotalToPay_of.setText(str(0))
        self.ui.orderChange_of.setText(str(0))

        self.ui.orderItem_tbl.setRowCount(0)

        Messsage("Ready to accept new order",self.ui)



        


        