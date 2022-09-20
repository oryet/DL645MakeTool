# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MeterCalibrationUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(703, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_CodeData = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_CodeData.setObjectName("textEdit_CodeData")
        self.verticalLayout.addWidget(self.textEdit_CodeData)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Head = QtWidgets.QLabel(self.centralwidget)
        self.label_Head.setObjectName("label_Head")
        self.horizontalLayout.addWidget(self.label_Head)
        self.lineEdit_FEFE = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_FEFE.sizePolicy().hasHeightForWidth())
        self.lineEdit_FEFE.setSizePolicy(sizePolicy)
        self.lineEdit_FEFE.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_FEFE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_FEFE.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_FEFE.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_FEFE.setMaxLength(8)
        self.lineEdit_FEFE.setObjectName("lineEdit_FEFE")
        self.horizontalLayout.addWidget(self.lineEdit_FEFE)
        self.label_Addr = QtWidgets.QLabel(self.centralwidget)
        self.label_Addr.setObjectName("label_Addr")
        self.horizontalLayout.addWidget(self.label_Addr)
        self.lineEdit_Addr = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Addr.sizePolicy().hasHeightForWidth())
        self.lineEdit_Addr.setSizePolicy(sizePolicy)
        self.lineEdit_Addr.setMinimumSize(QtCore.QSize(3, 0))
        self.lineEdit_Addr.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_Addr.setMaxLength(12)
        self.lineEdit_Addr.setObjectName("lineEdit_Addr")
        self.horizontalLayout.addWidget(self.lineEdit_Addr)
        self.label_Ctrl = QtWidgets.QLabel(self.centralwidget)
        self.label_Ctrl.setObjectName("label_Ctrl")
        self.horizontalLayout.addWidget(self.label_Ctrl)
        self.lineEdit_Ctrl = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Ctrl.sizePolicy().hasHeightForWidth())
        self.lineEdit_Ctrl.setSizePolicy(sizePolicy)
        self.lineEdit_Ctrl.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit_Ctrl.setMaxLength(2)
        self.lineEdit_Ctrl.setObjectName("lineEdit_Ctrl")
        self.horizontalLayout.addWidget(self.lineEdit_Ctrl)
        self.label_DI = QtWidgets.QLabel(self.centralwidget)
        self.label_DI.setObjectName("label_DI")
        self.horizontalLayout.addWidget(self.label_DI)
        self.lineEdit_DI = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_DI.sizePolicy().hasHeightForWidth())
        self.lineEdit_DI.setSizePolicy(sizePolicy)
        self.lineEdit_DI.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_DI.setMaxLength(8)
        self.lineEdit_DI.setObjectName("lineEdit_DI")
        self.horizontalLayout.addWidget(self.lineEdit_DI)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.horizontalLayout.addWidget(self.lineEdit_Password)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelVol = QtWidgets.QLabel(self.centralwidget)
        self.labelVol.setObjectName("labelVol")
        self.horizontalLayout_4.addWidget(self.labelVol)
        self.lineEdit_Vol_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Vol_A.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Vol_A.setObjectName("lineEdit_Vol_A")
        self.horizontalLayout_4.addWidget(self.lineEdit_Vol_A)
        self.lineEdit_Vol_B = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Vol_B.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Vol_B.setObjectName("lineEdit_Vol_B")
        self.horizontalLayout_4.addWidget(self.lineEdit_Vol_B)
        self.lineEdit_Vol_C = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Vol_C.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Vol_C.setObjectName("lineEdit_Vol_C")
        self.horizontalLayout_4.addWidget(self.lineEdit_Vol_C)
        self.labelAmp = QtWidgets.QLabel(self.centralwidget)
        self.labelAmp.setObjectName("labelAmp")
        self.horizontalLayout_4.addWidget(self.labelAmp)
        self.lineEdit_Amp_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Amp_A.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Amp_A.setObjectName("lineEdit_Amp_A")
        self.horizontalLayout_4.addWidget(self.lineEdit_Amp_A)
        self.lineEdit_Amp_B = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Amp_B.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Amp_B.setObjectName("lineEdit_Amp_B")
        self.horizontalLayout_4.addWidget(self.lineEdit_Amp_B)
        self.lineEdit_Amp_C = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Amp_C.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Amp_C.setObjectName("lineEdit_Amp_C")
        self.horizontalLayout_4.addWidget(self.lineEdit_Amp_C)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit_PPwr_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PPwr_A.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_PPwr_A.setObjectName("lineEdit_PPwr_A")
        self.horizontalLayout_5.addWidget(self.lineEdit_PPwr_A)
        self.lineEdit_PPwr_B = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PPwr_B.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_PPwr_B.setObjectName("lineEdit_PPwr_B")
        self.horizontalLayout_5.addWidget(self.lineEdit_PPwr_B)
        self.lineEdit_PPwr_C = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PPwr_C.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_PPwr_C.setObjectName("lineEdit_PPwr_C")
        self.horizontalLayout_5.addWidget(self.lineEdit_PPwr_C)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_QPwr_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_QPwr_A.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_QPwr_A.setObjectName("lineEdit_QPwr_A")
        self.horizontalLayout_5.addWidget(self.lineEdit_QPwr_A)
        self.lineEdit_QPwr_B = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_QPwr_B.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_QPwr_B.setObjectName("lineEdit_QPwr_B")
        self.horizontalLayout_5.addWidget(self.lineEdit_QPwr_B)
        self.lineEdit_QPwr_C = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_QPwr_C.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_QPwr_C.setObjectName("lineEdit_QPwr_C")
        self.horizontalLayout_5.addWidget(self.lineEdit_QPwr_C)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit_conste = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_conste.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_conste.setObjectName("lineEdit_conste")
        self.horizontalLayout_7.addWidget(self.lineEdit_conste)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_startip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_startip.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_startip.setObjectName("lineEdit_startip")
        self.horizontalLayout_7.addWidget(self.lineEdit_startip)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_ub = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ub.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_ub.setObjectName("lineEdit_ub")
        self.horizontalLayout_7.addWidget(self.lineEdit_ub)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_ib = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ib.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_ib.setObjectName("lineEdit_ib")
        self.horizontalLayout_7.addWidget(self.lineEdit_ib)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_imax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_imax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_imax.setObjectName("lineEdit_imax")
        self.horizontalLayout_7.addWidget(self.lineEdit_imax)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_freq = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_freq.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_freq.setObjectName("lineEdit_freq")
        self.horizontalLayout_8.addWidget(self.lineEdit_freq)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_wriemode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_wriemode.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_wriemode.setObjectName("lineEdit_wriemode")
        self.horizontalLayout_8.addWidget(self.lineEdit_wriemode)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.lineEdit_inmode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inmode.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_inmode.setObjectName("lineEdit_inmode")
        self.horizontalLayout_8.addWidget(self.lineEdit_inmode)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.lineEdit_addmode = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_addmode.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_addmode.setObjectName("lineEdit_addmode")
        self.horizontalLayout_8.addWidget(self.lineEdit_addmode)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.lineEdit_pclass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pclass.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_pclass.setObjectName("lineEdit_pclass")
        self.horizontalLayout_9.addWidget(self.lineEdit_pclass)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.lineEdit_qclass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_qclass.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_qclass.setObjectName("lineEdit_qclass")
        self.horizontalLayout_9.addWidget(self.lineEdit_qclass)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.lineEdit_volgain = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_volgain.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_volgain.setObjectName("lineEdit_volgain")
        self.horizontalLayout_9.addWidget(self.lineEdit_volgain)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.lineEdit_ampgain = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ampgain.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_ampgain.setObjectName("lineEdit_ampgain")
        self.horizontalLayout_9.addWidget(self.lineEdit_ampgain)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.lineEdit_ZeroLineAmp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ZeroLineAmp.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_ZeroLineAmp.setObjectName("lineEdit_ZeroLineAmp")
        self.horizontalLayout_11.addWidget(self.lineEdit_ZeroLineAmp)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.lineEdit_PowerOffset_A = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PowerOffset_A.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_PowerOffset_A.setObjectName("lineEdit_PowerOffset_A")
        self.horizontalLayout_10.addWidget(self.lineEdit_PowerOffset_A)
        self.lineEdit_PowerOffset_B = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PowerOffset_B.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_PowerOffset_B.setObjectName("lineEdit_PowerOffset_B")
        self.horizontalLayout_10.addWidget(self.lineEdit_PowerOffset_B)
        self.lineEdit_PowerOffset_C = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PowerOffset_C.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_PowerOffset_C.setObjectName("lineEdit_PowerOffset_C")
        self.horizontalLayout_10.addWidget(self.lineEdit_PowerOffset_C)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.pushButton_DataRead = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DataRead.setObjectName("pushButton_DataRead")
        self.horizontalLayout_3.addWidget(self.pushButton_DataRead)
        self.pushButton_DataSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DataSave.setObjectName("pushButton_DataSave")
        self.horizontalLayout_3.addWidget(self.pushButton_DataSave)
        self.pushButton_Code = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Code.setObjectName("pushButton_Code")
        self.horizontalLayout_3.addWidget(self.pushButton_Code)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textEdit_DecodeData = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_DecodeData.setObjectName("textEdit_DecodeData")
        self.verticalLayout.addWidget(self.textEdit_DecodeData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.pushButton_Add33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Add33.setObjectName("pushButton_Add33")
        self.horizontalLayout_2.addWidget(self.pushButton_Add33)
        self.pushButton_Sub33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sub33.setObjectName("pushButton_Sub33")
        self.horizontalLayout_2.addWidget(self.pushButton_Sub33)
        self.pushButton_CS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CS.setObjectName("pushButton_CS")
        self.horizontalLayout_2.addWidget(self.pushButton_CS)
        self.lineEdit_Low = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Low.sizePolicy().hasHeightForWidth())
        self.lineEdit_Low.setSizePolicy(sizePolicy)
        self.lineEdit_Low.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_Low.setObjectName("lineEdit_Low")
        self.horizontalLayout_2.addWidget(self.lineEdit_Low)
        self.pushButton_DeCode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DeCode.setObjectName("pushButton_DeCode")
        self.horizontalLayout_2.addWidget(self.pushButton_DeCode)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action_TempCali = QtWidgets.QAction(mainWindow)
        self.action_TempCali.setObjectName("action_TempCali")
        self.action_MtrCali = QtWidgets.QAction(mainWindow)
        self.action_MtrCali.setObjectName("action_MtrCali")
        self.action_MtrStart = QtWidgets.QAction(mainWindow)
        self.action_MtrStart.setObjectName("action_MtrStart")
        self.action_MtrEnd = QtWidgets.QAction(mainWindow)
        self.action_MtrEnd.setObjectName("action_MtrEnd")
        self.action_4 = QtWidgets.QAction(mainWindow)
        self.action_4.setObjectName("action_4")
        self.action_MtrZoneLine = QtWidgets.QAction(mainWindow)
        self.action_MtrZoneLine.setObjectName("action_MtrZoneLine")
        self.action_Energy = QtWidgets.QAction(mainWindow)
        self.action_Energy.setObjectName("action_Energy")
        self.action_Parm = QtWidgets.QAction(mainWindow)
        self.action_Parm.setObjectName("action_Parm")
        self.action_Curr = QtWidgets.QAction(mainWindow)
        self.action_Curr.setObjectName("action_Curr")
        self.action_Cuver = QtWidgets.QAction(mainWindow)
        self.action_Cuver.setObjectName("action_Cuver")
        self.action_FreezeDay = QtWidgets.QAction(mainWindow)
        self.action_FreezeDay.setObjectName("action_FreezeDay")
        self.action_FreezeMon = QtWidgets.QAction(mainWindow)
        self.action_FreezeMon.setObjectName("action_FreezeMon")
        self.action_SettlementDate = QtWidgets.QAction(mainWindow)
        self.action_SettlementDate.setObjectName("action_SettlementDate")
        self.action_MtrEvent = QtWidgets.QAction(mainWindow)
        self.action_MtrEvent.setObjectName("action_MtrEvent")
        self.action_TaskParm = QtWidgets.QAction(mainWindow)
        self.action_TaskParm.setObjectName("action_TaskParm")
        self.action_FileTrans = QtWidgets.QAction(mainWindow)
        self.action_FileTrans.setObjectName("action_FileTrans")
        self.action_CommParm = QtWidgets.QAction(mainWindow)
        self.action_CommParm.setObjectName("action_CommParm")
        self.action_ExParm = QtWidgets.QAction(mainWindow)
        self.action_ExParm.setObjectName("action_ExParm")
        self.action_MtrZoneLineOffset = QtWidgets.QAction(mainWindow)
        self.action_MtrZoneLineOffset.setObjectName("action_MtrZoneLineOffset")
        self.action_MtrPoffset = QtWidgets.QAction(mainWindow)
        self.action_MtrPoffset.setObjectName("action_MtrPoffset")
        self.action_MtrVirt = QtWidgets.QAction(mainWindow)
        self.action_MtrVirt.setObjectName("action_MtrVirt")
        self.action_TempCali_File = QtWidgets.QAction(mainWindow)
        self.action_TempCali_File.setObjectName("action_TempCali_File")
        self.menu.addAction(self.action_TempCali)
        self.menu.addSeparator()
        self.menu.addAction(self.action_MtrStart)
        self.menu.addAction(self.action_MtrCali)
        self.menu.addAction(self.action_MtrZoneLineOffset)
        self.menu.addAction(self.action_MtrZoneLine)
        self.menu.addAction(self.action_MtrPoffset)
        self.menu.addAction(self.action_MtrEnd)
        self.menu.addSeparator()
        self.menu.addAction(self.action_TempCali_File)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MeterCalibration V1.1 20220920"))
        self.label_Head.setText(_translate("mainWindow", "Head"))
        self.lineEdit_FEFE.setText(_translate("mainWindow", "FEFEFE"))
        self.label_Addr.setText(_translate("mainWindow", "Addr"))
        self.lineEdit_Addr.setText(_translate("mainWindow", "000000000000"))
        self.label_Ctrl.setText(_translate("mainWindow", "Ctrl"))
        self.lineEdit_Ctrl.setText(_translate("mainWindow", "3E"))
        self.label_DI.setText(_translate("mainWindow", "  DI"))
        self.lineEdit_DI.setText(_translate("mainWindow", "F0000062"))
        self.label_18.setText(_translate("mainWindow", "  Password"))
        self.lineEdit_Password.setText(_translate("mainWindow", "SZLY"))
        self.labelVol.setText(_translate("mainWindow", "Vol "))
        self.lineEdit_Vol_A.setText(_translate("mainWindow", "220.0"))
        self.lineEdit_Vol_B.setText(_translate("mainWindow", "220.0"))
        self.lineEdit_Vol_C.setText(_translate("mainWindow", "220.0"))
        self.labelAmp.setText(_translate("mainWindow", "Amp "))
        self.lineEdit_Amp_A.setText(_translate("mainWindow", "1.5"))
        self.lineEdit_Amp_B.setText(_translate("mainWindow", "1.5"))
        self.lineEdit_Amp_C.setText(_translate("mainWindow", "1.5"))
        self.label.setText(_translate("mainWindow", "PPwr"))
        self.lineEdit_PPwr_A.setText(_translate("mainWindow", "165.0"))
        self.lineEdit_PPwr_B.setText(_translate("mainWindow", "165.0"))
        self.lineEdit_PPwr_C.setText(_translate("mainWindow", "165.0"))
        self.label_2.setText(_translate("mainWindow", "QPwr"))
        self.lineEdit_QPwr_A.setText(_translate("mainWindow", "285.78"))
        self.lineEdit_QPwr_B.setText(_translate("mainWindow", "285.78"))
        self.lineEdit_QPwr_C.setText(_translate("mainWindow", "285.78"))
        self.label_3.setText(_translate("mainWindow", "Conste"))
        self.lineEdit_conste.setText(_translate("mainWindow", "10000"))
        self.label_4.setText(_translate("mainWindow", " Startip"))
        self.lineEdit_startip.setText(_translate("mainWindow", "0"))
        self.label_5.setText(_translate("mainWindow", "     Ub"))
        self.lineEdit_ub.setText(_translate("mainWindow", "220.0"))
        self.label_6.setText(_translate("mainWindow", "     Ib"))
        self.lineEdit_ib.setText(_translate("mainWindow", "1.5"))
        self.label_7.setText(_translate("mainWindow", "Imax"))
        self.lineEdit_imax.setText(_translate("mainWindow", "6.0"))
        self.label_8.setText(_translate("mainWindow", " Freq "))
        self.lineEdit_freq.setText(_translate("mainWindow", "50"))
        self.label_9.setText(_translate("mainWindow", "Wriemode"))
        self.lineEdit_wriemode.setText(_translate("mainWindow", "0"))
        self.label_10.setText(_translate("mainWindow", " Inmode"))
        self.lineEdit_inmode.setText(_translate("mainWindow", "0"))
        self.label_11.setText(_translate("mainWindow", "Addmode"))
        self.lineEdit_addmode.setText(_translate("mainWindow", "0"))
        self.label_12.setText(_translate("mainWindow", "Pclass"))
        self.lineEdit_pclass.setText(_translate("mainWindow", "0"))
        self.label_13.setText(_translate("mainWindow", "  Qclass"))
        self.lineEdit_qclass.setText(_translate("mainWindow", "0"))
        self.label_14.setText(_translate("mainWindow", "Volgain"))
        self.lineEdit_volgain.setText(_translate("mainWindow", "0"))
        self.label_15.setText(_translate("mainWindow", "Ampgain"))
        self.lineEdit_ampgain.setText(_translate("mainWindow", "0"))
        self.label_16.setText(_translate("mainWindow", "ZeroLineAmp"))
        self.lineEdit_ZeroLineAmp.setText(_translate("mainWindow", "1.5"))
        self.label_17.setText(_translate("mainWindow", "PowerOffset"))
        self.lineEdit_PowerOffset_A.setText(_translate("mainWindow", "0"))
        self.lineEdit_PowerOffset_B.setText(_translate("mainWindow", "0"))
        self.lineEdit_PowerOffset_C.setText(_translate("mainWindow", "0"))
        self.pushButton_DataRead.setText(_translate("mainWindow", "读取"))
        self.pushButton_DataSave.setText(_translate("mainWindow", "保存"))
        self.pushButton_Code.setText(_translate("mainWindow", "组帧"))
        self.pushButton_Add33.setText(_translate("mainWindow", "+33"))
        self.pushButton_Sub33.setText(_translate("mainWindow", "-33"))
        self.pushButton_CS.setText(_translate("mainWindow", "CS"))
        self.lineEdit_Low.setText(_translate("mainWindow", "4"))
        self.pushButton_DeCode.setText(_translate("mainWindow", "解帧"))
        self.menu.setTitle(_translate("mainWindow", "组帧"))
        self.action_TempCali.setText(_translate("mainWindow", "温度补偿"))
        self.action_MtrCali.setText(_translate("mainWindow", "电表校准"))
        self.action_MtrStart.setText(_translate("mainWindow", "启动校表"))
        self.action_MtrEnd.setText(_translate("mainWindow", "结束校表"))
        self.action_4.setText(_translate("mainWindow", "电表校准"))
        self.action_MtrZoneLine.setText(_translate("mainWindow", "零线校准"))
        self.action_Energy.setText(_translate("mainWindow", "电量"))
        self.action_Parm.setText(_translate("mainWindow", "参变量"))
        self.action_Curr.setText(_translate("mainWindow", "瞬时量"))
        self.action_Cuver.setText(_translate("mainWindow", "曲线冻结"))
        self.action_FreezeDay.setText(_translate("mainWindow", "日冻结"))
        self.action_FreezeMon.setText(_translate("mainWindow", "月冻结"))
        self.action_SettlementDate.setText(_translate("mainWindow", "结算日"))
        self.action_MtrEvent.setText(_translate("mainWindow", "事件"))
        self.action_TaskParm.setText(_translate("mainWindow", "任务参数"))
        self.action_FileTrans.setText(_translate("mainWindow", "文件传输"))
        self.action_CommParm.setText(_translate("mainWindow", "通信参数"))
        self.action_ExParm.setText(_translate("mainWindow", "其他参数"))
        self.action_MtrZoneLineOffset.setText(_translate("mainWindow", "零线偏置"))
        self.action_MtrPoffset.setText(_translate("mainWindow", "功率偏置"))
        self.action_MtrVirt.setText(_translate("mainWindow", "模拟数据"))
        self.action_TempCali_File.setText(_translate("mainWindow", "温补文件"))
