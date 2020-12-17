# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.server = QtWidgets.QLineEdit(self.groupBox)
        self.server.setObjectName("server")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.server)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.port = QtWidgets.QLineEdit(self.groupBox)
        self.port.setObjectName("port")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.port)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setObjectName("username")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.hostname = QtWidgets.QLineEdit(self.groupBox)
        self.hostname.setObjectName("hostname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hostname)
        self.connect = QtWidgets.QPushButton(self.groupBox)
        self.connect.setObjectName("connect")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.connect)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.speed = QtWidgets.QComboBox(self.groupBox)
        self.speed.setObjectName("speed")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.speed)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.keyword = QtWidgets.QLineEdit(self.groupBox_2)
        self.keyword.setObjectName("keyword")
        self.gridLayout_2.addWidget(self.keyword, 0, 1, 1, 1)
        self.search = QtWidgets.QPushButton(self.groupBox_2)
        self.search.setObjectName("search")
        self.gridLayout_2.addWidget(self.search, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.results = QtWidgets.QTableWidget(self.groupBox_2)
        self.results.setObjectName("results")
        self.results.setColumnCount(3)
        self.results.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.results.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.results.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.results.setHorizontalHeaderItem(2, item)
        self.results.verticalHeader().setVisible(True)
        self.verticalLayout_2.addWidget(self.results)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.command = QtWidgets.QLineEdit(self.groupBox_3)
        self.command.setObjectName("command")
        self.gridLayout.addWidget(self.command, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.go = QtWidgets.QPushButton(self.groupBox_3)
        self.go.setObjectName("go")
        self.gridLayout.addWidget(self.go, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.commandLine = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.commandLine.setObjectName("commandLine")
        self.verticalLayout_4.addWidget(self.commandLine)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GV-NAPSTER Host"))
        self.groupBox.setTitle(_translate("MainWindow", "Connection"))
        self.label.setText(_translate("MainWindow", "Server Hostname:"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "Username:"))
        self.label_4.setText(_translate("MainWindow", "Hostname:"))
        self.connect.setText(_translate("MainWindow", "Connect"))
        self.label_6.setText(_translate("MainWindow", "Speed:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search"))
        self.label_7.setText(_translate("MainWindow", "Keyword:"))
        self.search.setText(_translate("MainWindow", "Search"))
        item = self.results.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "speed"))
        item = self.results.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "hostname"))
        item = self.results.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "filename"))
        self.groupBox_3.setTitle(_translate("MainWindow", "FTP"))
        self.label_5.setText(_translate("MainWindow", "Enter command:"))
        self.go.setText(_translate("MainWindow", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
