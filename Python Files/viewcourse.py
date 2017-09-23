# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewcourse.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource
import mysql.connector

class Ui_viewcourse(object):
    def setupUi(self, viewcourse):
        viewcourse.setObjectName("viewcourse")
        viewcourse.resize(1240, 900)
        self.label = QtWidgets.QLabel(viewcourse)
        self.label.setGeometry(QtCore.QRect(-320, 20, 1611, 1101))
        self.label.setStyleSheet("background-image:url(:/img/2.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(viewcourse)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 208, 95))
        self.label_4.setStyleSheet("background-image:url(:/img/NirmaUniversity_Logo.jpg)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(viewcourse)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1251, 121))
        self.label_2.setStyleSheet("background-color:rgb(0, 85, 0)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(viewcourse)
        self.label_3.setGeometry(QtCore.QRect(460, 30, 681, 61))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(viewcourse)
        self.tableWidget.setGeometry(QtCore.QRect(620, 250, 221, 361))
    
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        self.tableWidget.setHorizontalHeaderLabels(['Roll', 'Grade'])
        
        self.label_17 = QtWidgets.QLabel(viewcourse)
        self.label_17.setGeometry(QtCore.QRect(470, 180, 131, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_email_6 = QtWidgets.QLineEdit(viewcourse)
        self.lineEdit_email_6.setGeometry(QtCore.QRect(650, 180, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_email_6.setFont(font)
        self.lineEdit_email_6.setToolTip("")
        self.lineEdit_email_6.setObjectName("lineEdit_email_6")
        self.pushButton_add = QtWidgets.QPushButton(viewcourse)
        self.pushButton_add.setGeometry(QtCore.QRect(910, 160, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.clicked.connect(self.show)
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.tableWidget.raise_()
        self.label_17.raise_()
        self.lineEdit_email_6.raise_()
        self.pushButton_add.raise_()

        self.retranslateUi(viewcourse)
        QtCore.QMetaObject.connectSlotsByName(viewcourse)
        
    
    def show(self):
        
        code= self.lineEdit_email_6.text()
        
        con = mysql.connector.connect(user='root',password='',host='localhost',database='studentevaluation')
        cur = con.cursor()
        str = "SELECT roll,grade from marks WHERE code = '{code}'".format(code=code)
        cur.execute(str)
        rows=cur.fetchall()
        self.tableWidget.setRowCount(0)

     
        
        for row_number,row_data in enumerate(rows):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(data))
        
        
        con.close()
    

    def retranslateUi(self, viewcourse):
        _translate = QtCore.QCoreApplication.translate
        viewcourse.setWindowTitle(_translate("viewcourse", "View Courses"))
        viewcourse.setWindowIcon(QtGui.QIcon('C:/Users/Afreen/Desktop/Canteen App Photos/logo.png'))
        self.label_2.setText(_translate("viewcourse", "<html><head/><body><p><span style=\" font-weight:600; color:#005500;width:1200;height:500;\">vdsvas</span></p></body></html>"))
        self.label_3.setText(_translate("viewcourse", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Student Evaluation System</span></p></body></html>"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
       
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_17.setText(_translate("viewcourse", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Course Code</span></p></body></html>"))
        self.pushButton_add.setText(_translate("viewcourse", "SHOW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewcourse = QtWidgets.QDialog()
    ui = Ui_viewcourse()
    ui.setupUi(viewcourse)
    viewcourse.show()
    sys.exit(app.exec_())

