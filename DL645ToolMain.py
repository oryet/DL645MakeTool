from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
import sys, DL645MakeUI
from PublicLib.Protocol.dl645resp import *
from PublicLib.Protocol.dl645 import *
from PublicLib.Protocol.dl645format import *

__author__ = 'jiangzy'


class MainWindow(QMainWindow, DL645MakeUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 将响应函数绑定到指定Button
        # self.pushButton.clicked.connect(self.showMessage)
        self.createActions()

    def createActions(self):
        self.pushButton_Code.clicked.connect(self.buttonCode)
        self.pushButton_DeCode.clicked.connect(self.button_DeCode)
        self.pushButton_Add33.clicked.connect(self.buttonAdd33)
        self.pushButton_Sub33.clicked.connect(self.buttonSub33)
        self.pushButton_CS.clicked.connect(self.buttonCS)

    def buttonCode(self):
        FrameHead = self.lineEdit_FEFE.text()
        MtrAddr = self.lineEdit_Addr.text()
        Ctrl = self.lineEdit_Ctrl.text()
        DI   = self.lineEdit_DI.text()
        data = self.lineEdit_Data.text()

        dl645data = DI + data
        dl645data = Dl645DataAdd33(dl645data)
        s = make645Frame(FrameHead, MtrAddr, Ctrl, dl645data)
        self.textEdit_CodeData.setText(s)

    def button_DeCode(self):
        s = self.textEdit_DecodeData.toPlainText()
        s = s.replace(' ', '')
        l = deal645Frame(s)
        low = self.lineEdit_Low.text()
        try:
            ilow = int(low)
        except:
            ilow = 0
        if l[0] and ilow > 0:
            s = str2hex(l[3], 1)
            l[3] = hex2str(s, 0)
            d = l[3][8:]
            l += dl645_str2nxx(d, ilow)

        self.textEdit_CodeData.setPlainText(str(l))

    def buttonAdd33(self):
        s = self.textEdit_DecodeData.toPlainText()
        s = s.replace(' ', '')
        s = str2hex(s, 0)
        s = hex2str(s, 1)
        self.textEdit_CodeData.setPlainText(s)

    def buttonSub33(self):
        s = self.textEdit_DecodeData.toPlainText()
        s = s.replace(' ', '')
        s = str2hex(s, 1)
        s = hex2str(s, 0)
        self.textEdit_CodeData.setPlainText(s)

    def buttonCS(self):
        s = self.textEdit_DecodeData.toPlainText()
        s = s.replace(' ', '')
        cs = pfun.calcCheckSum(s)
        self.textEdit_CodeData.setPlainText(cs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())