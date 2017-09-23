# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(1240, 900)
        Home.setAutoFillBackground(True)
        Home.setStyleSheet("")
        self.label = QtWidgets.QLabel(Home)
        self.label.setGeometry(QtCore.QRect(-350, 40, 1611, 1101))
        self.label.setStyleSheet("background-image:url(:/img/2.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Home)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1251, 121))
        self.label_2.setStyleSheet("background-color:rgb(0, 85, 0)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Home)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 681, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Home)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 208, 95))
        self.label_4.setStyleSheet("background-image:url(:/img/NirmaUniversity_Logo.jpg)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(Home)
        self.groupBox.setGeometry(QtCore.QRect(760, 230, 371, 321))
        self.groupBox.setObjectName("groupBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setGeometry(QtCore.QRect(150, 60, 201, 31))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pass.setGeometry(QtCore.QRect(150, 110, 201, 31))
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.label_bt_login = QtWidgets.QLabel(self.groupBox)
        self.label_bt_login.setGeometry(QtCore.QRect(100, 180, 161, 51))
        self.label_bt_login.setMouseTracking(False)
        self.label_bt_login.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_bt_login.setText("")
        self.label_bt_login.setPixmap(QtGui.QPixmap(":/img/login-button-png-28.png"))
        self.label_bt_login.setScaledContents(True)
        self.label_bt_login.setObjectName("label_bt_login")
        self.label_bt_signup = QtWidgets.QLabel(self.groupBox)
        self.label_bt_signup.setGeometry(QtCore.QRect(100, 240, 161, 51))
        self.label_bt_signup.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_bt_signup.setText("")
        self.label_bt_signup.setPixmap(QtGui.QPixmap(":/img/Sign-Up-Button-Transparent-Background.png"))
        self.label_bt_signup.setScaledContents(True)
        self.label_bt_signup.setObjectName("label_bt_signup")
        self.label_5 = QtWidgets.QLabel(Home)
        self.label_5.setGeometry(QtCore.QRect(760, 210, 371, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Home)
        self.label_6.setGeometry(QtCore.QRect(770, 220, 121, 31))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Dialog"))
        self.label_2.setText(_translate("Home", "<html><head/><body><p><span style=\" font-weight:600; color:#005500;width:1200;height:500;\">vdsvas</span></p></body></html>"))
        self.label_3.setText(_translate("Home", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Student Evaluation System</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Home", "GroupBox"))
        self.label_7.setText(_translate("Home", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Email</span></p></body></html>"))
        self.label_8.setText(_translate("Home", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_5.setText(_translate("Home", "<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#454545;background-color:#454545\">TextLabel</span></p></body></html>"))
        self.label_6.setText(_translate("Home", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">LOGIN</span></p></body></html>"))

import resource

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QDialog()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())

