# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupscreenmodified.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import tkinter.messagebox

class Ui_SignUpScreenModified(object):
    def setupUi(self, SignUpScreenModified):
        SignUpScreenModified.setObjectName("SignUpScreenModified")
        SignUpScreenModified.resize(1240, 900)
        self.label = QtWidgets.QLabel(SignUpScreenModified)
        self.label.setGeometry(QtCore.QRect(-350, 40, 1611, 1101))
        self.label.setStyleSheet("background-image:url(:/img/2.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(SignUpScreenModified)
        self.label_3.setGeometry(QtCore.QRect(460, 30, 681, 61))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(SignUpScreenModified)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1251, 121))
        self.label_2.setStyleSheet("background-color:rgb(0, 85, 0)")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(SignUpScreenModified)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 208, 95))
        self.label_4.setStyleSheet("background-image:url(:/img/NirmaUniversity_Logo.jpg)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(SignUpScreenModified)
        self.label_5.setGeometry(QtCore.QRect(760, 300, 371, 51))
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(SignUpScreenModified)
        self.groupBox.setGeometry(QtCore.QRect(760, 320, 371, 321))
        self.groupBox.setObjectName("groupBox")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_email_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email_6.setGeometry(QtCore.QRect(150, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_email_6.setFont(font)
        self.lineEdit_email_6.setToolTip("")
        self.lineEdit_email_6.setObjectName("lineEdit_email_6")
        self.lineEdit_pass_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pass_6.setGeometry(QtCore.QRect(150, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_pass_6.setFont(font)
        self.lineEdit_pass_6.setObjectName("lineEdit_pass_6")
        self.label_bt_signup_6 = QtWidgets.QLabel(self.groupBox)
        self.label_bt_signup_6.setGeometry(QtCore.QRect(100, 240, 161, 51))
        self.label_bt_signup_6.setText("")
        self.label_bt_signup_6.setPixmap(QtGui.QPixmap(":/img/Sign-Up-Button-Transparent-Background.png"))
        self.label_bt_signup_6.setScaledContents(True)
        self.label_bt_signup_6.setObjectName("label_bt_signup_6")
        
        self.pushButton_signup_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_signup_6.setGeometry(QtCore.QRect(100, 230, 161, 51))
        self.pushButton_signup_6.setStyleSheet("background-color:transparent;\n"
"border-image:url(:/img/signupp.png);\n"
"background:none;\n"
"border:none;\n"
"background-repeat:none;")
        self.pushButton_signup_6.setText("")
        self.pushButton_signup_6.setObjectName("pushButton_signup_6")
        
        self.pushButton_signup_6.clicked.connect(self.dataentry)
        
        self.label_6 = QtWidgets.QLabel(SignUpScreenModified)
        self.label_6.setGeometry(QtCore.QRect(770, 310, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_19 = QtWidgets.QLabel(SignUpScreenModified)
        self.label_19.setGeometry(QtCore.QRect(760, 300, 431, 51))
        self.label_19.setObjectName("label_19")
        self.groupBox_2 = QtWidgets.QGroupBox(SignUpScreenModified)
        self.groupBox_2.setGeometry(QtCore.QRect(760, 320, 431, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.label_21.setObjectName("label_21")
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_username.setGeometry(QtCore.QRect(190, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setToolTip("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_password.setGeometry(QtCore.QRect(190, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_bt_signup_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_bt_signup_7.setGeometry(QtCore.QRect(100, 240, 161, 51))
        self.label_bt_signup_7.setText("")
        self.label_bt_signup_7.setPixmap(QtGui.QPixmap(":/img/Sign-Up-Button-Transparent-Background.png"))
        self.label_bt_signup_7.setScaledContents(True)
        self.label_bt_signup_7.setObjectName("label_bt_signup_7")
        self.pushButton_signup_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_signup_7.setGeometry(QtCore.QRect(150, 270, 161, 51))
        self.pushButton_signup_7.setStyleSheet("background-color:transparent;\n"
"border-image:url(:/img/signupp.png);\n"
"background:none;\n"
"border:none;\n"
"background-repeat:none;")
        self.pushButton_signup_7.setText("")
        self.pushButton_signup_7.setObjectName("pushButton_signup_7")
        
        self.pushButton_signup_7.clicked.connect(self.dataentry)
        
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(20, 160, 101, 31))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(20, 210, 141, 31))
        self.label_23.setObjectName("label_23")
        self.lineEdit_repass = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_repass.setGeometry(QtCore.QRect(190, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_repass.setFont(font)
        self.lineEdit_repass.setObjectName("lineEdit_repass")
        self.lineEdit_email_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_email_9.setGeometry(QtCore.QRect(190, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_email_9.setFont(font)
        self.lineEdit_email_9.setToolTip("")
        self.lineEdit_email_9.setObjectName("lineEdit_email_9")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        
        self.label_5.raise_()
        self.groupBox_2.raise_()
        self.label_19.raise_()
        self.label_6.raise_()

        self.retranslateUi(SignUpScreenModified)
        QtCore.QMetaObject.connectSlotsByName(SignUpScreenModified)
        
        
        
    def dataentry(self):
        #connection
        con = mysql.connector.connect(user='root',password='',host='localhost',database='studentevaluation')
        cur = con.cursor()
        
        email=self.lineEdit_email_9.text()
        user=self.lineEdit_username.text()
        passs=self.lineEdit_password.text()
        repass=self.lineEdit_repass.text()
        
        if (email!="" and user!="" and passs!="" and repass!=""):
            if(passs == repass):
                cur.execute("""INSERT INTO signup VALUES (%s,%s,%s,%s)""",("",email,user,passs))
                tkinter.messagebox.showinfo("Successful","SignUp Successful")
                con.commit()
                con.close()
            else:
                tkinter.messagebox.showwarning("Fail","Password Doesnt Match")
        else:
            tkinter.messagebox.showinfo("Invalid","All Fields are required")

    def retranslateUi(self, SignUpScreenModified):
        _translate = QtCore.QCoreApplication.translate
        SignUpScreenModified.setWindowTitle(_translate("SignUpScreenModified", "Sign Up"))
        SignUpScreenModified.setWindowIcon(QtGui.QIcon('C:/Users/Afreen/Desktop/Canteen App Photos/logo.png'))
        self.label_3.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Student Evaluation System</span></p></body></html>"))
        self.label_2.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-weight:600; color:#005500;width:1200;height:500;\">vdsvas</span></p></body></html>"))
        self.label_5.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#454545;background-color:#454545\">TextLabel</span></p></body></html>"))
        self.groupBox.setTitle(_translate("SignUpScreenModified", "GroupBox"))
        self.label_17.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Email</span></p></body></html>"))
        self.label_18.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_6.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">SIGN UP</span></p></body></html>"))
        self.label_19.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#454545;background-color:#454545\">TextLabel</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("SignUpScreenModified", "GroupBox"))
        self.label_20.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Email</span></p></body></html>"))
        self.label_21.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Username</span></p></body></html>"))
        self.label_22.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#000000;\">Password</span></p></body></html>"))
        self.label_23.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#000000;\">Re Password</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpScreenModified = QtWidgets.QDialog() 
    ui = Ui_SignUpScreenModified()
    ui.setupUi(SignUpScreenModified)
    SignUpScreenModified.show()
    sys.exit(app.exec_())

