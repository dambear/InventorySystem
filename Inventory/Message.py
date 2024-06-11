from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class Messsage:
    def __init__(self,message,parent) -> None:
        msgBox = QMessageBox(parent)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(message)
        msgBox.setWindowTitle("Warning")
        msgBox.setStandardButtons(QMessageBox.Ok)
        #msgBox.buttonClicked.connect(msgButtonClick)

        #msgBox.setStyleSheet("QLabel{min-width: 100px; text-align:left;}");
        returnValue = msgBox.exec()