# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'marks.ui'
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
        SignUpScreenNew.resize(1240, 900)
        self.label = QtWidgets.QLabel(SignUpScreenNew)
        self.label.setGeometry(QtCore.QRect(-340, 20, 1611, 1101))
        self.label.setStyleSheet("background-image:url(:/img/2.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_3.setGeometry(QtCore.QRect(460, 30, 681, 61))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1251, 121))
        self.label_2.setStyleSheet("background-color:rgb(0, 85, 0)")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 208, 95))
        self.label_4.setStyleSheet("background-image:url(:/img/NirmaUniversity_Logo.jpg)\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_17 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_17.setGeometry(QtCore.QRect(440, 170, 131, 31))
        self.label_17.setObjectName("label_17")
        self.lineEdit_code = QtWidgets.QLineEdit(SignUpScreenNew)
        self.lineEdit_code.setGeometry(QtCore.QRect(600, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_code.setFont(font)
        self.lineEdit_code.setToolTip("")
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.label_18 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_18.setGeometry(QtCore.QRect(440, 270, 131, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_19.setGeometry(QtCore.QRect(440, 320, 131, 31))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_20.setGeometry(QtCore.QRect(440, 370, 131, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_21.setGeometry(QtCore.QRect(440, 420, 131, 31))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_22.setGeometry(QtCore.QRect(440, 470, 131, 31))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(SignUpScreenNew)
        self.label_23.setGeometry(QtCore.QRect(440, 220, 131, 31))
        self.label_23.setObjectName("label_23")
        self.lineEdit_roll = QtWidgets.QLineEdit(SignUpScreenNew)
        self.lineEdit_roll.setGeometry(QtCore.QRect(600, 220, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_roll.setFont(font)
        self.lineEdit_roll.setToolTip("")
        self.lineEdit_roll.setObjectName("lineEdit_roll")
        self.lineEdit_ct = QtWidgets.QLineEdit(SignUpScreenNew)
        self.lineEdit_ct.setGeometry(QtCore.QRect(600, 270, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_ct.setFont(font)
        self.lineEdit_ct.setToolTip("")
        self.lineEdit_ct.setObjectName("lineEdit_ct")
        self.lineEdit_sess = QtWidgets.QLineEdit(SignUpScreenNew)
        self.lineEdit_sess.setGeometry(QtCore.QRect(600, 320, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_sess.setFont(font)
        self.lineEdit_sess.setToolTip("")
        self.lineEdit_sess.setObjectName("lineEdit_sess")
        self.lineEdit_tut = QtWidgets.QLineEdit(SignUpScreenNew)
        self.lineEdit_tut.setGeometry(QtCore.QRect(600, 370, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_tut.setFont(font)
        self.lineEdit_tut.setToolTip("")
        self.lineEdit_tut.setObjectName("lineEdit_tut")
        self.lineEdit_lpw = QtWidgets.QLineEdit(SignUpScreenNew)
        self.lineEdit_lpw.setGeometry(QtCore.QRect(600, 420, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_lpw.setFont(font)
        self.lineEdit_lpw.setToolTip("")
        self.lineEdit_lpw.setObjectName("lineEdit_lpw")
        self.lineEdit_see = QtWidgets.QLineEdit(SignUpScreenNew)
        self.lineEdit_see.setGeometry(QtCore.QRect(600, 470, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_see.setFont(font)
        self.lineEdit_see.setToolTip("")
        self.lineEdit_see.setObjectName("lineEdit_see")
        self.pushButton_add = QtWidgets.QPushButton(SignUpScreenNew)
        self.pushButton_add.setGeometry(QtCore.QRect(530, 540, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        
        self.pushButton_add.clicked.connect(self.dataentry)
        
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_17.raise_()
        self.lineEdit_code.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.lineEdit_roll.raise_()
        self.lineEdit_ct.raise_()
        self.lineEdit_sess.raise_()
        self.lineEdit_tut.raise_()
        self.lineEdit_lpw.raise_()
        self.lineEdit_see.raise_()
        self.pushButton_add.raise_()

        self.retranslateUi(SignUpScreenNew)
        QtCore.QMetaObject.connectSlotsByName(SignUpScreenNew)
        
    def dataentry(self):
        #connection
        con = mysql.connector.connect(user='root',password='',host='localhost',database='studentevaluation')
        cur = con.cursor()
        
        code=self.lineEdit_code.text()
        roll=self.lineEdit_roll.text()
        ct=self.lineEdit_ct.text()
        sess=self.lineEdit_sess.text()
        tut=self.lineEdit_tut.text()
        lpw=self.lineEdit_lpw.text()
        see=self.lineEdit_see.text()
        
        
        ######################################################
        query_string = "SELECT ct_per FROM course WHERE code = '{code}'".format(code=code)  
        cur.execute(query_string)
        ct_perct = cur.fetchone()[0]
            
        query_string1 = "SELECT ses_per FROM course WHERE code = '{code}'".format(code=code)  
        cur.execute(query_string1)
        ses_perct = cur.fetchone()[0]
        
        query_string2 = "SELECT tut_inn_per FROM course WHERE code = '{code}'".format(code=code)  
        cur.execute(query_string2)
        tut_perct = cur.fetchone()[0]
        
        query_string3 = "SELECT con_per FROM course WHERE code = '{code}'".format(code=code)  
        cur.execute(query_string3)
        con_perct = cur.fetchone()[0]
        
      
        
        
        con_add = float(ct) + float(sess) + float(tut)
        con_marks = float(con_add) * float(con_perct)
        con_tot = float(con_marks / 100)
        
        
        query_string4 = "SELECT lpw_per FROM course WHERE code = '{code}'".format(code=code)  
        cur.execute(query_string4)
        lpw_perct = cur.fetchone()[0]
        
        query_string5 = "SELECT see_per FROM course WHERE code = '{code}'".format(code=code)  
        cur.execute(query_string5)
        see_perct = cur.fetchone()[0]
        
        if (lpw_perct == 0):
            see_add= float(see) * float(see_perct)
            see_marks = float(see_add / 100)
            
            con_tot_perc = float((float(con_tot) * 60) / 100)
            
            total= see_marks + con_tot_perc
                                
        else:
            see_add= float(see) * float(see_perct)
            see_marks = float(see_add / 100)
            
            lpw_add= float(lpw) * float(lpw_perct)
            lpw_marks = float(lpw_add / 100)
            
            con_tot_perc = float((float(con_tot) * 40) / 100)
            
            total= see_marks + con_tot_perc + lpw_marks
            
            
        if( total < 40 ):
            grade="FF"
        elif (total < 50):
            grade="C"
        elif (total < 60):
            grade="C+"
        elif (total < 70):
            grade="B"
        elif (total < 80):
            grade="B+"
        elif (total < 90):
            grade="A"
        elif (total < 100):
            grade="A+"
        
        
        
        if (code!="" and roll!="" and ct!="" and sess!="" and tut!="" and lpw!="" and see!=""):
            cur.execute("""INSERT INTO marks (code,roll,ct,sess,tut,lpw,see,con,total,grade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(code,roll,ct,sess,tut,lpw,see,con_tot,total,grade))
            tkinter.messagebox.showinfo("Successful","Marks Added Successful")
            self.lineEdit_ct.setText("")
            self.lineEdit_lpw.setText("")
            self.lineEdit_roll.setText("")
            self.lineEdit_see.setText("")
            self.lineEdit_sess.setText("")
            self.lineEdit_tut.setText("")
            
            con.commit()
            con.close()
        else:
            tkinter.messagebox.showinfo("Invalid","All Fields are required")
            
            

    def retranslateUi(self, SignUpScreenNew):
        _translate = QtCore.QCoreApplication.translate
        SignUpScreenNew.setWindowTitle(_translate("SignUpScreenNew", "Add Marks"))
        SignUpScreenNew.setWindowIcon(QtGui.QIcon('C:/Users/Afreen/Desktop/Canteen App Photos/logo.png'))
        self.label_3.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Student Evaluation System</span></p></body></html>"))
        self.label_2.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-weight:600; color:#005500;width:1200;height:500;\">vdsvas</span></p></body></html>"))
        self.label_17.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Course Code</span></p></body></html>"))
        self.label_18.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">CT Marks</span></p></body></html>"))
        self.label_19.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sess Marks</span></p></body></html>"))
        self.label_20.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Tut/Innov</span></p></body></html>"))
        self.label_21.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">LPW</span></p></body></html>"))
        self.label_22.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">SEE</span></p></body></html>"))
        self.label_23.setText(_translate("SignUpScreenNew", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Roll No</span></p></body></html>"))
        self.pushButton_add.setText(_translate("SignUpScreenNew", "NEXT"))

import resource

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpScreenNew = QtWidgets.QDialog()
    ui = Ui_SignUpScreenNew()
    ui.setupUi(SignUpScreenNew)
    SignUpScreenNew.show()
    sys.exit(app.exec_())

