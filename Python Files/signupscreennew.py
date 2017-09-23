# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupscreennew.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import tkinter.messagebox


class Ui_SignUpScreenNew(object):
    def setupUi(self, SignUpScreenNew):
        SignUpScreenNew.setObjectName("SignUpScreenNew")
        SignUpScreenNew.resize(640, 480)
        
        self.label_5 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_5.setGeometry(QtCore.QRect(-10, 0, 651, 81))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_6.setGeometry(QtCore.QRect(120, 20, 421, 41))
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(SignUpScreenNew)
        self.groupBox.setGeometry(QtCore.QRect(180, 130, 251, 241))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 46, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.lineEdit_email.setObjectName("lineEdit_email")
        
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_username.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pass.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_repass = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_repass.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.lineEdit_repass.setObjectName("lineEdit_repass")
        self.pushButton_signup = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_signup.setGeometry(QtCore.QRect(20, 150, 211, 31))
        self.pushButton_signup.setObjectName("pushButton_signup")
        
        self.pushButton_signup.clicked.connect(self.dataentry)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 190, 211, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(SignUpScreenNew)
        QtCore.QMetaObject.connectSlotsByName(SignUpScreenNew)
        
        
        
        
    def dataentry(self):
        #connection
        con = mysql.connector.connect(user='root',password='',host='localhost',database='studentevaluation')
        cur = con.cursor()
        
        email=self.lineEdit_email.text()
        user=self.lineEdit_username.text()
        passs=self.lineEdit_pass.text()
        repass=self.lineEdit_repass.text()
        
        if (email!="" and user!="" and passs!="" and repass!=""):
            if(passs == repass):
                cur.execute("""INSERT INTO signup VALUES (%s,%s,%s,%s)""",("",self.lineEdit_email.text(),self.lineEdit_username.text(),self.lineEdit_pass.text()))
                tkinter.messagebox.showinfo("Successful","SignUp Successful")
                con.commit()
                con.close()
            else:
                tkinter.messagebox.showwarning("Fail","Password Doesnt Match")
        else:
            tkinter.messagebox.showinfo("Invalid","All Fields are required")
                
                
            
        
        

    def retranslateUi(self, SignUpScreenNew):
        _translate = QtCore.QCoreApplication.translate
        SignUpScreenNew.setWindowTitle(_translate("SignUpScreenNew", "Sign Up "))
        self.label_5.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:72pt;background-color:#000000\">klvn\'ds\'nvlsnvjnsfkjvnsfk;jnvjskfnvjknfvj nsfkjv fskjv jsfvk;vsk;v sf vkj;fsvjkfs;nvkjfsvkjsfvjksf vkjfs vjk;svjfv</span></p></body></html>"))
        self.label_6.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Student Evaluation System</span></p></body></html>"))
        self.groupBox.setTitle(_translate("SignUpScreenNew", "SignUp"))
        self.label.setText(_translate("SignUpScreenNew", "Email"))
        self.label_2.setText(_translate("SignUpScreenNew", "Username"))
        self.label_3.setText(_translate("SignUpScreenNew", "Password"))
        self.label_4.setText(_translate("SignUpScreenNew", "Reset Password"))
        self.pushButton_signup.setText(_translate("SignUpScreenNew", "SIGN UP"))
        self.pushButton_2.setText(_translate("SignUpScreenNew", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpScreenNew = QtWidgets.QDialog()
    ui = Ui_SignUpScreenNew()
    ui.setupUi(SignUpScreenNew)
    SignUpScreenNew.show()
    sys.exit(app.exec_())

