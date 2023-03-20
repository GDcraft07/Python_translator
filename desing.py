from PyQt5 import QtCore, QtWidgets


class Registrating(object):
    def setupui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logos = QtWidgets.QLabel(self.widget)
        self.logos.setText("")
        self.logos.setObjectName("logos")
        self.verticalLayout_2.addWidget(self.logos)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.users_login = QtWidgets.QLineEdit(self.widget)
        self.users_login.setObjectName("users_login")
        self.verticalLayout_2.addWidget(self.users_login)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.users_password = QtWidgets.QLineEdit(self.widget)
        self.users_password.setObjectName("users_password")
        self.verticalLayout_2.addWidget(self.users_password)
        self.error_password = QtWidgets.QLabel(self.widget)
        self.error_password.setEnabled(False)
        self.error_password.setObjectName("error_password")
        self.verticalLayout_2.addWidget(self.error_password)
        self.registrates = QtWidgets.QPushButton(self.widget)
        self.registrates.setObjectName("registrates")
        self.verticalLayout_2.addWidget(self.registrates)
        self.sing_in = QtWidgets.QPushButton(self.widget)
        self.sing_in.setObjectName("sing_in")
        self.verticalLayout_2.addWidget(self.sing_in)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"
                                                      "Ввелите логин:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"
                                                      "Введите пароль:</p></body></html>"))
        self.error_password.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">"
                                                             "<br/></p></body></html>"))
        self.registrates.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.sing_in.setText(_translate("MainWindow", "Войти"))


class MainWindows(object):
    def setupui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 290)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(6, "")
        self.gridLayout.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Русский"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Английский"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Испанский"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Французский"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Китайский"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Немецкий"))
        self.pushButton.setText(_translate("MainWindow", "\n"
                                                         "\n"
                                                         "\n"
                                                         "перевести текст\n"
                                                         "\n"
                                                         "\n"""))
        self.comboBox.setItemText(0, _translate("MainWindow", "Английский"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Русский"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Испанский"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Французский"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Китайский"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Немецкий"))
        self.pushButton_2.setText(_translate("MainWindow", "->\n"
                                                           "<-"))
        self.pushButton_3.setText(_translate("MainWindow", "История переводов"))
        self.pushButton_4.setText(_translate("MainWindow", "Авторизация"))
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)


class HistoryTrans(object):
    def setupui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "History"))