from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys, MeterCalibrationUI
from DL645MakeFrame import *
from dl645 import *

__author__ = 'jiangzy'


class MainWindow(QMainWindow, MeterCalibrationUI.Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 将响应函数绑定到指定Button
        # self.pushButton.clicked.connect(self.showMessage)
        self.createActions()
        self.dt = {'rtn': False, 'FrameHead': '', 'MtrAddr': '', 'Ctrl': '', 'DI': '', 'data': '', 'meterParm': '', 'tempParm': '',
                   'Vol':[0]*3, 'Amp':[0]*3, 'PPwr':[0]*3, 'QPwr':[0]*3, 'conste':0, 'startip':0, 'ub':0, 'ib':0, 'imax':0,
                   'freq':0, 'wriemode':0, 'inmode':0, 'addmode':0, 'pclass':0, 'qclass':0, 'volgain':0, 'ampgain':0,
                   'ZeroLineAmp':[0]*3, 'PowerOffset':[0]*3}
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
        self.pushButton_DataRead.clicked.connect(self.buttonRead)
        self.pushButton_DataSave.clicked.connect(self.buttonSave)

        # menu
        self.action_TempCali.triggered.connect(self.menuTempCali)
        self.action_MtrCali.triggered.connect(self.menuMtrCali)
        self.action_MtrZoneLine.triggered.connect(self.menuMtrCali_ZeroLine)
        self.action_MtrZoneLineOffset.triggered.connect(self.menuMtrCali_ZeroLineOffset)
        self.action_MtrStart.triggered.connect(self.menuMtrCali_Start)
        self.action_MtrPoffset.triggered.connect(self.menuMtrCali_PowerOffset)
        self.action_MtrVirt.triggered.connect(self.menuMtrVirtual_SetIns)
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
        # self.getLineEdit()
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

    def buttonRead(self):
        self.dt['fileName'] = "cfgMtrCali.json"
        self.dt = loadCfg(self.dt)
        if self.dt['rtn'] == False:
            return
        self.setLineEdit()

    def buttonSave(self):
        if self.dt['rtn'] == True:
            saveCfg(self.dt)

    def getLineEdit(self):
        # if self.dt['rtn'] == False:
        #     self.dt['fileName'] = "cfgMtrCali.json"
        #     self.dt = loadCfg(self.dt)
        self.dt['FrameHead'] = self.lineEdit_FEFE.text()
        self.dt['MtrAddr'] = pub.strReverse(self.lineEdit_Addr.text())
        self.dt['Ctrl'] = self.lineEdit_Ctrl.text()
        self.dt['DI'] = pub.strReverse(self.lineEdit_DI.text())
        self.dt['Password'] = self.lineEdit_Password.text()
        # self.dt['data'] = self.lineEdit_Data.text()
        # vol
        self.dt['Vol'][0] = float(self.lineEdit_Vol_A.text())
        self.dt['Vol'][1] = float(self.lineEdit_Vol_B.text())
        self.dt['Vol'][2] = float(self.lineEdit_Vol_C.text())
        # amp
        self.dt['Amp'][0] = float(self.lineEdit_Amp_A.text())
        self.dt['Amp'][1] = float(self.lineEdit_Amp_B.text())
        self.dt['Amp'][2] = float(self.lineEdit_Amp_C.text())
        # ppwr
        self.dt['PPwr'][0] = float(self.lineEdit_PPwr_A.text())
        self.dt['PPwr'][1] = float(self.lineEdit_PPwr_B.text())
        self.dt['PPwr'][2] = float(self.lineEdit_PPwr_C.text())
        # qpwr
        self.dt['QPwr'][0] = float(self.lineEdit_QPwr_A.text())
        self.dt['QPwr'][1] = float(self.lineEdit_QPwr_B.text())
        self.dt['QPwr'][2] = float(self.lineEdit_QPwr_C.text())
        # conste
        self.dt['conste'] = float(self.lineEdit_conste.text())
        # startip
        self.dt['startip'] = float(self.lineEdit_startip.text())
        # ub
        self.dt['ub'] = float(self.lineEdit_ub.text())
        # ib
        self.dt['ib'] = float(self.lineEdit_ib.text())
        # imax
        self.dt['imax'] = float(self.lineEdit_imax.text())
        # freq
        self.dt['freq'] = float(self.lineEdit_freq.text())
        # imax
        self.dt['wriemode'] = float(self.lineEdit_wriemode.text())
        # inmode
        self.dt['inmode'] = float(self.lineEdit_inmode.text())
        # addmode
        self.dt['addmode'] = float(self.lineEdit_addmode.text())
        # pclass
        self.dt['pclass'] = float(self.lineEdit_pclass.text())
        # qclass
        self.dt['qclass'] = float(self.lineEdit_qclass.text())
        # volgain
        self.dt['volgain'] = float(self.lineEdit_volgain.text())
        # ampgain
        self.dt['ampgain'] = float(self.lineEdit_ampgain.text())
        # ZeroLineAmp
        self.dt['ZeroLineAmp'][0] = float(self.lineEdit_ZeroLineAmp.text())
        # PowerOffset
        self.dt['PowerOffset'][0] = float(self.lineEdit_PowerOffset_A.text())
        self.dt['PowerOffset'][1] = float(self.lineEdit_PowerOffset_B.text())
        self.dt['PowerOffset'][2] = float(self.lineEdit_PowerOffset_C.text())

    def setLineEdit(self):
        self.lineEdit_FEFE.setText(self.dt['FrameHead'].upper())
        self.lineEdit_Addr.setText(pub.strReverse(self.dt['MtrAddr'].upper()))
        self.lineEdit_Ctrl.setText(self.dt['Ctrl'].upper())
        self.lineEdit_DI.setText(pub.strReverse(self.dt['DI'].upper()))
        self.lineEdit_Password.setText(self.dt['Password'])
        # self.lineEdit_Data.setText(self.dt['data'].upper())
        # vol
        self.lineEdit_Vol_A.setText(str(self.dt['Vol'][0]))
        self.lineEdit_Vol_B.setText(str(self.dt['Vol'][1]))
        self.lineEdit_Vol_C.setText(str(self.dt['Vol'][2]))
        # amp
        self.lineEdit_Amp_A.setText(str(self.dt['Amp'][0]))
        self.lineEdit_Amp_B.setText(str(self.dt['Amp'][1]))
        self.lineEdit_Amp_C.setText(str(self.dt['Amp'][2]))
        # ppwr
        self.lineEdit_PPwr_A.setText(str(self.dt['PPwr'][0]))
        self.lineEdit_PPwr_B.setText(str(self.dt['PPwr'][1]))
        self.lineEdit_PPwr_C.setText(str(self.dt['PPwr'][2]))
        # qpwr
        self.lineEdit_QPwr_A.setText(str(self.dt['QPwr'][0]))
        self.lineEdit_QPwr_B.setText(str(self.dt['QPwr'][1]))
        self.lineEdit_QPwr_C.setText(str(self.dt['QPwr'][2]))
        # conste
        self.lineEdit_conste.setText(str(self.dt['conste']))
        # startip
        self.lineEdit_startip.setText(str(self.dt['startip']))
        # ub
        self.lineEdit_ub.setText(str(self.dt['ub']))
        # ib
        self.lineEdit_ib.setText(str(self.dt['ib']))
        # imax
        self.lineEdit_imax.setText(str(self.dt['imax']))
        # freq
        self.lineEdit_freq.setText(str(self.dt['freq']))
        # imax
        self.lineEdit_wriemode.setText(str(self.dt['wriemode']))
        # inmode
        self.lineEdit_inmode.setText(str(self.dt['inmode']))
        # addmode
        self.lineEdit_addmode.setText(str(self.dt['addmode']))
        # pclass
        self.lineEdit_pclass.setText(str(self.dt['pclass']))
        # qclass
        self.lineEdit_qclass.setText(str(self.dt['qclass']))
        # volgain
        self.lineEdit_volgain.setText(str(self.dt['volgain']))
        # ampgain
        self.lineEdit_ampgain.setText(str(self.dt['ampgain']))
        # ZeroLineAmp
        self.lineEdit_ZeroLineAmp.setText(str(self.dt['ZeroLineAmp'][0]))
        # PowerOffset
        self.lineEdit_PowerOffset_A.setText(str(self.dt['PowerOffset'][0]))
        self.lineEdit_PowerOffset_B.setText(str(self.dt['PowerOffset'][1]))
        self.lineEdit_PowerOffset_C.setText(str(self.dt['PowerOffset'][2]))

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

    def menuMtrVirtual_SetIns(self):
        self.getLineEdit()
        makeMtrVirtualData_Ins(self.dt)
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
