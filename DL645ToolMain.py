from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
import sys, DL645MakeUI
from DL645MakeFrame import *


__author__ = 'jiangzy'


class MainWindow(QMainWindow, DL645MakeUI.Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 将响应函数绑定到指定Button
        # self.pushButton.clicked.connect(self.showMessage)
        self.createActions()
        self.dt = {'rtn':False, 'FrameHead':'', 'MtrAddr':'', 'Ctrl':'', 'DI':'', 'data':''}

    def createActions(self):
        self.pushButton_Code.clicked.connect(self.buttonCode)
        self.pushButton_DeCode.clicked.connect(self.button_DeCode)
        self.pushButton_Add33.clicked.connect(self.buttonAdd33)
        self.pushButton_Sub33.clicked.connect(self.buttonSub33)
        self.pushButton_CS.clicked.connect(self.buttonCS)

        #menu
        self.action_TempCali.triggered.connect(self.menuTempCali)
        self.action_MtrCali.triggered.connect(self.menuMtrCali)
        self.action_MtrZoneLine.triggered.connect(self.menuMtrCali_ZeroLine)
        self.action_MtrStart.triggered.connect(self.menuMtrCali_Start)
        self.action_MtrEnd.triggered.connect(self.menuMtrCali_End)

    def buttonCode(self):
        self.getLineEdit()
        s = self.dt_make645Frame()

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

    def getLineEdit(self):
        self.dt['FrameHead'] = self.lineEdit_FEFE.text()
        self.dt['MtrAddr'] = self.lineEdit_Addr.text()
        self.dt['Ctrl'] = self.lineEdit_Ctrl.text()
        self.dt['DI'] = self.lineEdit_DI.text()
        self.dt['data'] = self.lineEdit_Data.text()

    def setLineEdit(self):
        self.lineEdit_FEFE.setText(self.dt['FrameHead'].upper())
        self.lineEdit_Addr.setText(self.dt['MtrAddr'].upper())
        self.lineEdit_Ctrl.setText(self.dt['Ctrl'].upper())
        self.lineEdit_DI.setText(self.dt['DI'].upper())
        self.lineEdit_Data.setText(self.dt['data'].upper())

    def dt_make645Frame(self):
        try:
            dl645data = self.dt['DI'] + self.dt['data']
            self.dt['dl645data'] = Dl645DataAdd33(dl645data)
            s = make645Frame(self.dt['FrameHead'], self.dt['MtrAddr'], self.dt['Ctrl'], self.dt['dl645data'])
            s = pub.frameaddspace(s)
            s = s.upper()
        except:
            s = ''
            print('dt_make645Frame err')
        return s

    def menuTempCali(self):
        self.getLineEdit()
        makeTempCaliData(self.dt)
        if self.dt['rtn']:
            self.setLineEdit()
        else:
            self.alert(self.dt['msg'])

    def menuMtrCali(self):
        self.getLineEdit()
        makeMtrCaliData(self.dt)
        if self.dt['rtn']:
            self.setLineEdit()
        else:
            self.alert(self.dt['msg'])

    def menuMtrCali_ZeroLine(self):
        self.getLineEdit()
        makeMtrCaliData_ZeroLine(self.dt)
        if self.dt['rtn']:
            self.setLineEdit()
        else:
            self.alert(self.dt['msg'])

    def menuMtrCali_Start(self):
        self.getLineEdit()
        makeMtrCaliData(self.dt)
        self.dt['data'] = self.dt['data'][:8] + '55555555'
        self.dt['DI'] = 'F0FF'
        if self.dt['rtn']:
            self.setLineEdit()
        else:
            self.alert(self.dt['msg'])

    def menuMtrCali_End(self):
        self.getLineEdit()
        makeMtrCaliData(self.dt)
        self.dt['data'] = self.dt['data'][:8] + 'AAAAAAAA'
        self.dt['DI'] = 'F0FF'
        if self.dt['rtn']:
            self.setLineEdit()
        else:
            self.alert(self.dt['msg'])

    def alert(self, message):
        QMessageBox.warning(self, "Warning", message)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())