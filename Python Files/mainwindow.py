# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from signup_screen import Ui_Signup_Screen
from signupscreennew import Ui_SignUpScreenNew


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 345)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.login = QtWidgets.QPushButton(self.centralWidget)
        self.login.setGeometry(QtCore.QRect(150, 80, 101, 41))
        self.login.setObjectName("login")
        
        self.login.clicked.connect(self.loginredirect)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 150, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.signupredirect)
        
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def loginredirect(self):
        self.login_screen = QtWidgets.QMainWindow()
        self.ui = Ui_Signup_Screen()
        self.ui.setupUi(self.login_screen)
        self.login_screen.show()
        
    def signupredirect(self):
        self.signup_screen = QtWidgets.QMainWindow()
        self.ui = Ui_SignUpScreenNew()
        self.ui.setupUi(self.signup_screen)
        self.signup_screen.show()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_2.setText(_translate("MainWindow", "SIGN UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

