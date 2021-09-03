# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DL645MakeUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.lineEdit_Ctrl.setMaximumSize(QtCore.QSize(50, 16777215))
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
        self.lineEdit_DI.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_DI.setObjectName("lineEdit_DI")
        self.horizontalLayout.addWidget(self.lineEdit_DI)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Data = QtWidgets.QLabel(self.centralwidget)
        self.label_Data.setObjectName("label_Data")
        self.horizontalLayout_3.addWidget(self.label_Data)
        self.lineEdit_Data = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Data.setObjectName("lineEdit_Data")
        self.horizontalLayout_3.addWidget(self.lineEdit_Data)
        self.pushButton_Code = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Code.setObjectName("pushButton_Code")
        self.horizontalLayout_3.addWidget(self.pushButton_Code)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textEdit_DecodeData = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_DecodeData.setObjectName("textEdit_DecodeData")
        self.verticalLayout.addWidget(self.textEdit_DecodeData)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Head.setText(_translate("MainWindow", "Head"))
        self.label_Addr.setText(_translate("MainWindow", "Addr"))
        self.label_Ctrl.setText(_translate("MainWindow", "Ctrl"))
        self.label_DI.setText(_translate("MainWindow", "DI"))
        self.label_Data.setText(_translate("MainWindow", "Data"))
        self.pushButton_Code.setText(_translate("MainWindow", "组帧"))
        self.pushButton_Add33.setText(_translate("MainWindow", "+33"))
        self.pushButton_Sub33.setText(_translate("MainWindow", "-33"))
        self.pushButton_CS.setText(_translate("MainWindow", "CS"))
        self.pushButton_DeCode.setText(_translate("MainWindow", "解帧"))