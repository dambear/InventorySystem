from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

class UIManager(object):

    def __init__(self, ui):
        self.ui = ui

    def RefreshTable(self, records, table):
        table.setRowCount(0)

        for row_number,user in enumerate(records):
            table.insertRow(row_number)
            for column_number,data in enumerate(user):
                cell = QtWidgets.QTableWidgetItem(str(data))
                table.setItem(row_number,column_number,cell)

    def SwitchFrame(self,frameName):
        name = 'Frame_'+str(frameName)
        frame = getattr(self,name,lambda :print('No Frame'))
        return frame()

    def Frame_Home(self):
        self.ui.HomeFrame.setHidden(False)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)
        
    def Frame_Customer(self):
        
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(False)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)
        
    def Frame_AddCust(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(False)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)
        
    def Frame_UptCust(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(False)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)
        
    def Frame_Product(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(False)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)
        
    def Frame_AddProd(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(False)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)
        
    def Frame_UptProd(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(False)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)
        
    def Frame_Order(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(False)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(True)

    def Frame_OrderForm(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(False)
        self.ui.Report.setHidden(True)

    def Frame_Report(self):
        self.ui.HomeFrame.setHidden(True)

        self.ui.CustomerFrame.setHidden(True)
        self.ui.CustAddFrame.setHidden(True)
        self.ui.CustUptFrame.setHidden(True)
        
        self.ui.ProductFrame.setHidden(True)
        self.ui.ProdAddFrame.setHidden(True)
        self.ui.ProdUptFrame.setHidden(True)
        
        self.ui.OrderFrame.setHidden(True)
        self.ui.OrderForm.setHidden(True)
        self.ui.Report.setHidden(False)
        
        #tablereports
        self.ui.frame_rep_cust.setHidden(True)
        self.ui.frame_rep_prod.setHidden(True)
        self.ui.frame_rep_order.setHidden(True)
        self.ui.frame_rep_sale.setHidden(True)
    
        
        
        
        
