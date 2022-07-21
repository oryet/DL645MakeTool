from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem, QHeaderView, \
    QAbstractItemView, QHeaderView, QTableWidget, QTableWidgetItem, QTableView
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
import sys, DL645MakeUI
from DL645MakeFrame import *
from DL645OpenExcel import *

__author__ = 'jiangzy'


class MainWindow(QMainWindow, DL645MakeUI.Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 将响应函数绑定到指定Button
        # self.pushButton.clicked.connect(self.showMessage)
        self.createActions()
        self.dt = {'rtn': False, 'FrameHead': '', 'MtrAddr': '', 'Ctrl': '', 'DI': '', 'data': '', 'parm': ''}
        # path = r'F:\Work\NLY1502\需求和协议\NLY1502 NLY1220数据项定义表 - 2021-7-15(1).xlsx'
        # path = os.getcwd() + r'\\NLY1502 NLY1220数据项定义表.xls'
        # self.dl = openExcel(path)
        # self.DIParmUIInit()

    def createActions(self):
        self.pushButton_Code.clicked.connect(self.buttonCode)
        self.pushButton_DeCode.clicked.connect(self.button_DeCode)
        self.pushButton_Add33.clicked.connect(self.buttonAdd33)
        self.pushButton_Sub33.clicked.connect(self.buttonSub33)
        self.pushButton_CS.clicked.connect(self.buttonCS)

        # menu
        self.action_TempCali.triggered.connect(self.menuTempCali)
        self.action_MtrCali.triggered.connect(self.menuMtrCali)
        self.action_MtrZoneLine.triggered.connect(self.menuMtrCali_ZeroLine)
        self.action_MtrZoneLineOffset.triggered.connect(self.menuMtrCali_ZeroLineOffset)
        self.action_MtrStart.triggered.connect(self.menuMtrCali_Start)
        self.action_MtrPoffset.triggered.connect(self.menuMtrCali_PowerOffset)
        self.action_MtrEnd.triggered.connect(self.menuMtrCali_End)

        # self.action_Energy.triggered.connect(self.menuEnergy)
        # self.action_Parm.triggered.connect(self.menuParm)
        # self.action_Curr.triggered.connect(self.menuCurr)
        # self.action_Cuver.triggered.connect(self.menuCuver)
        # self.action_FreezeDay.triggered.connect(self.menuFreezeDay)
        # self.action_FreezeMon.triggered.connect(self.menuFreezeMon)
        # self.action_SettlementDate.triggered.connect(self.menuSettlementDate)
        # self.action_MtrEvent.triggered.connect(self.menuMtrEvent)
        # self.action_TaskParm.triggered.connect(self.menuTaskParm)
        # self.action_FileTrans.triggered.connect(self.menuFileTrans)
        # self.action_CommParm.triggered.connect(self.menuCommParm)
        # self.action_ExParm.triggered.connect(self.menuExParm)

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
        self.dt['MtrAddr'] = pub.strReverse(self.lineEdit_Addr.text())
        self.dt['Ctrl'] = self.lineEdit_Ctrl.text()
        self.dt['DI'] = pub.strReverse(self.lineEdit_DI.text())
        self.dt['data'] = self.lineEdit_Data.text()

    def setLineEdit(self):
        self.lineEdit_FEFE.setText(self.dt['FrameHead'].upper())
        self.lineEdit_Addr.setText(pub.strReverse(self.dt['MtrAddr'].upper()))
        self.lineEdit_Ctrl.setText(self.dt['Ctrl'].upper())
        self.lineEdit_DI.setText(pub.strReverse(self.dt['DI'].upper()))
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

    def menuMtrCali_ZeroLineOffset(self):
        self.getLineEdit()
        makeMtrCaliData_ZeroLineOffset(self.dt)
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

    def menuMtrCali_PowerOffset(self):
        self.getLineEdit()
        makeMtrCaliData_DataPowerOffset(self.dt)
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

    '''
    def DIParmUIInit(self):
        self.tableWidget_DI.setRowCount(4)  # 行数
        self.tableWidget_DI.setColumnCount(5)  # 列数
        self.tableWidget_DI.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tableWidget_DI.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        # self.tableWidget_DI.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        # self.tableWidget_DI.setSelectionBehavior(QAbstractItemView.SelectItems)  # 设置选中一个
        self.tableWidget_DI.setHorizontalHeaderLabels(
            ['DI', '数据格式', '数据长度(字节)', '单位', '数据项名称'])  # 横向标题

    def tableSetValue(self, dlt, i):
        item = QTableWidgetItem(dlt['DI'][i])
        self.tableWidget_DI.setItem(i, 0, item)
        item = QTableWidgetItem(dlt['DIFormat'][i])
        self.tableWidget_DI.setItem(i, 1, item)
        item = QTableWidgetItem(dlt['DILen'][i])
        self.tableWidget_DI.setItem(i, 2, item)
        item = QTableWidgetItem(dlt['DIUnit'][i])
        self.tableWidget_DI.setItem(i, 3, item)
        item = QTableWidgetItem(dlt['DIName'][i])
        self.tableWidget_DI.setItem(i, 4, item)

    def menuEnergy(self):
        dlt = self.dl['7.4.1电量']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuParm(self):
        dlt = self.dl['7.4.2参变量']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuCurr(self):
        dlt = self.dl['7.4.3瞬时量']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuCuver(self):
        dlt = self.dl['7.4.4曲线冻结']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuFreezeDay(self):
        dlt = self.dl['7.4.6日冻结']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuFreezeMon(self):
        dlt = self.dl['7.4.7月冻结']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuSettlementDate(self):
        dlt = self.dl['7.4.7.1结算日']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuMtrEvent(self):
        dlt = self.dl['7.4.8电能表事件']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuTaskParm(self):
        dlt = self.dl['7.4.9任务参数']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuFileTrans(self):
        dlt = self.dl['7.4.10文件传输']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuCommParm(self):
        dlt = self.dl['7.4.11通信参数']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)

    def menuExParm(self):
        dlt = self.dl['7.4.14其他参数']
        RowCount = len(dlt['DI'])
        self.tableWidget_DI.setRowCount(RowCount)  # 行数
        for i in range(RowCount):
            self.tableSetValue(dlt, i)
    '''

    def alert(self, message):
        QMessageBox.warning(self, "Warning", message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
