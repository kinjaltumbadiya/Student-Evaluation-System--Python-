# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'afterlogin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from addcourse import Ui_addcourse
from viewcourse import Ui_viewcourse
from marks import Ui_SignUpScreenNew

class Ui_AfterLogin(object):
    def setupUi(self, AfterLogin):
        AfterLogin.setObjectName("AfterLogin")
        AfterLogin.resize(1240, 900)
        self.label = QtWidgets.QLabel(AfterLogin)
        self.label.setGeometry(QtCore.QRect(-320, -40, 1611, 1101))
        self.label.setStyleSheet("background-image:url(:/img/2.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(AfterLogin)
        self.label_3.setGeometry(QtCore.QRect(460, 30, 681, 61))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(AfterLogin)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1251, 121))
        self.label_2.setStyleSheet("background-color:rgb(0, 85, 0)")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(AfterLogin)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 208, 95))
        self.label_4.setStyleSheet("background-image:url(:/img/NirmaUniversity_Logo.jpg)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_add = QtWidgets.QPushButton(AfterLogin)
        self.pushButton_add.setGeometry(QtCore.QRect(390, 180, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        
        self.pushButton_add.clicked.connect(self.addCourseredirect)
        
        self.pushButton_view = QtWidgets.QPushButton(AfterLogin)
        self.pushButton_view.setGeometry(QtCore.QRect(580, 180, 161, 71))
        
        self.pushButton_view.clicked.connect(self.addMaksredirect)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_view.setFont(font)
        self.pushButton_view.setObjectName("pushButton_view")
        self.pushButton_logout = QtWidgets.QPushButton(AfterLogin)
        self.pushButton_logout.setGeometry(QtCore.QRect(780, 180, 161, 71))
        
        self.pushButton_logout.clicked.connect(self.viewCourseredirect)
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.label_5 = QtWidgets.QLabel(AfterLogin)
        self.label_5.setGeometry(QtCore.QRect(490, 370, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(48)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.pushButton_add.raise_()
        self.pushButton_view.raise_()
        self.pushButton_logout.raise_()
        self.label_5.raise_()

        self.retranslateUi(AfterLogin)
        QtCore.QMetaObject.connectSlotsByName(AfterLogin)
        
    def addCourseredirect(self):
        self.addCourse_screen = QtWidgets.QMainWindow()
        self.ui = Ui_addcourse()
        self.ui.setupUi(self.addCourse_screen)
        self.addCourse_screen.show()
        
    def viewCourseredirect(self):
        self.viewCourse_screen = QtWidgets.QMainWindow()
        self.ui = Ui_viewcourse()
        self.ui.setupUi(self.viewCourse_screen)
        self.viewCourse_screen.show()
        
    def addMaksredirect(self):
        self.addMarks_screen = QtWidgets.QMainWindow()
        self.ui = Ui_SignUpScreenNew()
        self.ui.setupUi(self.addMarks_screen)
        self.addMarks_screen.show()

    def retranslateUi(self, AfterLogin):
        _translate = QtCore.QCoreApplication.translate
        AfterLogin.setWindowTitle(_translate("AfterLogin", "Home"))
        AfterLogin.setWindowIcon(QtGui.QIcon('C:/Users/Afreen/Desktop/Canteen App Photos/logo.png'))
        self.label_3.setText(_translate("AfterLogin", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Student Evaluation System</span></p></body></html>"))
        self.label_2.setText(_translate("AfterLogin", "<html><head/><body><p><span style=\" font-weight:600; color:#005500;width:1200;height:500;\">vdsvas</span></p></body></html>"))
        self.pushButton_add.setText(_translate("AfterLogin", "Add Course"))
        self.pushButton_view.setText(_translate("AfterLogin", "Add Marks"))
        self.pushButton_logout.setText(_translate("AfterLogin", "View Course"))
        self.label_5.setText(_translate("AfterLogin", "WELCOME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AfterLogin = QtWidgets.QDialog()
    ui = Ui_AfterLogin()
    ui.setupUi(AfterLogin)
    AfterLogin.show()
    sys.exit(app.exec_())

