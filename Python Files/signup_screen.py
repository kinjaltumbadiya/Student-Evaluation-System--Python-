# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_screen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Signup_Screen(object):
    def setupUi(self, Signup_Screen):
        Signup_Screen.setObjectName("Signup_Screen")
        Signup_Screen.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Signup_Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(360, 110, 207, 141))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_user = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.horizontalLayout.addWidget(self.lineEdit_user)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_pass = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.horizontalLayout_2.addWidget(self.lineEdit_pass)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_signup = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.verticalLayout.addWidget(self.pushButton_signup)
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(50, 90, 231, 191))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        Signup_Screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Signup_Screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Signup_Screen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Signup_Screen)
        self.statusbar.setObjectName("statusbar")
        Signup_Screen.setStatusBar(self.statusbar)

        self.retranslateUi(Signup_Screen)
        QtCore.QMetaObject.connectSlotsByName(Signup_Screen)

    def retranslateUi(self, Signup_Screen):
        _translate = QtCore.QCoreApplication.translate
        Signup_Screen.setWindowTitle(_translate("Signup_Screen", "MainWindow"))
        self.groupBox.setTitle(_translate("Signup_Screen", "Login"))
        self.label.setText(_translate("Signup_Screen", "Username"))
        self.label_2.setText(_translate("Signup_Screen", "Password"))
        self.pushButton_signup.setText(_translate("Signup_Screen", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup_Screen = QtWidgets.QMainWindow()
    ui = Ui_Signup_Screen()
    ui.setupUi(Signup_Screen)
    Signup_Screen.show()
    sys.exit(app.exec_())

