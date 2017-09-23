# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupscreenmodifiednew.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.label_5.setGeometry(QtCore.QRect(760, 300, 411, 51))
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(SignUpScreenModified)
        self.groupBox.setGeometry(QtCore.QRect(760, 320, 411, 361))
        self.groupBox.setObjectName("groupBox")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 101, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_email_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email_6.setGeometry(QtCore.QRect(180, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_email_6.setFont(font)
        self.lineEdit_email_6.setToolTip("")
        self.lineEdit_email_6.setObjectName("lineEdit_email_6")
        self.lineEdit_username_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_username_6.setGeometry(QtCore.QRect(180, 110, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_username_6.setFont(font)
        self.lineEdit_username_6.setObjectName("lineEdit_username_6")
        self.label_bt_signup_6 = QtWidgets.QLabel(self.groupBox)
        self.label_bt_signup_6.setGeometry(QtCore.QRect(100, 240, 161, 51))
        self.label_bt_signup_6.setText("")
        self.label_bt_signup_6.setPixmap(QtGui.QPixmap(":/img/Sign-Up-Button-Transparent-Background.png"))
        self.label_bt_signup_6.setScaledContents(True)
        self.label_bt_signup_6.setObjectName("label_bt_signup_6")
        self.pushButton_signup_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_signup_6.setGeometry(QtCore.QRect(130, 270, 161, 51))
        self.pushButton_signup_6.setStyleSheet("background-color:transparent;\n"
"border-image:url(:/img/signupp.png);\n"
"background:none;\n"
"border:none;\n"
"background-repeat:none;")
        self.pushButton_signup_6.setText("")
        self.pushButton_signup_6.setObjectName("pushButton_signup_6")
        self.lineEdit_pass_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pass_7.setGeometry(QtCore.QRect(180, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_pass_7.setFont(font)
        self.lineEdit_pass_7.setObjectName("lineEdit_pass_7")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(20, 160, 111, 31))
        self.label_19.setObjectName("label_19")
        self.lineEdit_repass_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_repass_8.setGeometry(QtCore.QRect(180, 210, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_repass_8.setFont(font)
        self.lineEdit_repass_8.setObjectName("lineEdit_repass_8")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(20, 210, 141, 31))
        self.label_20.setObjectName("label_20")
        self.label_6 = QtWidgets.QLabel(SignUpScreenModified)
        self.label_6.setGeometry(QtCore.QRect(770, 310, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.groupBox.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(SignUpScreenModified)
        QtCore.QMetaObject.connectSlotsByName(SignUpScreenModified)

    def retranslateUi(self, SignUpScreenModified):
        _translate = QtCore.QCoreApplication.translate
        SignUpScreenModified.setWindowTitle(_translate("SignUpScreenModified", "Dialog"))
        self.label_3.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Student Evaluation System</span></p></body></html>"))
        self.label_2.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-weight:600; color:#005500;width:1200;height:500;\">vdsvas</span></p></body></html>"))
        self.label_5.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#454545;background-color:#454545\">TextLabel</span></p></body></html>"))
        self.groupBox.setTitle(_translate("SignUpScreenModified", "GroupBox"))
        self.label_17.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Email</span></p></body></html>"))
        self.label_18.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Username</span></p><p><br/></p></body></html>"))
        self.label_19.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_20.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Re-Password</span></p></body></html>"))
        self.label_6.setText(_translate("SignUpScreenModified", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">SIGNUP</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpScreenModified = QtWidgets.QDialog()
    ui = Ui_SignUpScreenModified()
    ui.setupUi(SignUpScreenModified)
    SignUpScreenModified.show()
    sys.exit(app.exec_())

