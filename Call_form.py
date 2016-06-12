# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Call_form.ui'
#
# Created: Sat Jun 11 17:36:38 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(329, 147)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/background/Icons/AIbEiAIAAABECP2Iptyl4PzmnAEiC3ZjYXJkX3Bob3RvKihiMjczYWVlNWQ1ZWVlNjYyY2U2NzA5YWUwNzgzMjE2MmZkMGYxN2Q5MAFyoVXTDsx0nC3OGfmWE7vsTYpe9Q.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("QDialog{background-image: url(:/background/Icons/background.jpg);background-repeat: repeat;}\n"
"\n"
"QToolBar{background:blue;}\n"
"\n"
"QWidget#scrollArea{background-color: blue;}\n"
"QTabBar::tab { background: darkblue; color: white; padding: 10px; border: 2px solid blue;}\n"
"QTabBar::tab:selected {background: rgb(217, 217, 0);  color: black; }\n"
"QTabBar::tab:!selected {background:darkblue;  color: white;}\n"
"/*QTabBar {background-color: blue;} */\n"
"QTabBar::tab:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"\n"
"QPushButton{border-style:solid;background-color:darkblue;color:white;border-radius:3px;font: 12pt \"MS Shell Dlg 2\";}\n"
"QPushButton:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"QPushButton:pressed{background-color: lightblue;}\n"
"QPushButton:disabled{background-color: rgb(176, 176, 176);}\n"
"\n"
"QPushButton#connectButton{ background-color: darkred;}\n"
"QPushButton#connectButton:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"QPushButton#connectButton:pressed{background-color: lightblue;}\n"
"QPushButton#connectButton:disabled{background-color: rgb(176, 176, 176);}\n"
"\n"
"QComboBox{border-style:solid;background-color:darkblue;color:white;border-radius:3px;font: 12pt \"MS Shell Dlg 2\"; padding: 10px}\n"
"QComboBox:hover{color:#ccc;    background-color: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.517, y2:1, stop:0 rgba(45, 45, 45, 255), stop:0.505682 rgba(45, 45, 45, 255), stop:1 rgba(29, 29, 29, 255));    border-color:#2d89ef;border-width:2px;}\n"
"QComboBox:pressed{background-color: lightblue;}\n"
"\n"
"QLineEdit {border:4px outset; border-radius: 8px; border-color: blue; color:rgb(0, 0, 0);  background-color: rgb(235, 235, 235); padding:10px;font: 75 12pt \"MS Shell Dlg 2\";}\n"
"/*QLineEdit { border-radius: 8px;  color:black;background-color: white; } */\n"
"QLineEdit:focus {  border:4px outset; border-radius: 8px; border-color: rgb(41, 237, 215); color:rgb(0, 0, 0);  background-color: rgb(240, 204, 204); }\n"
"\n"
"QLabel {border:4px outset; border-radius: 0px; border-color: blue; color:white;  background-color: darkblue; padding:5px;font: 75 12pt \"MS Shell Dlg 2\";}\n"
"QPlainTextEdit {border:4px outset; border-radius: 0px; border-color: blue; color:black;  background-color: rgb(235, 235, 235);; padding:5px;font: 75 12pt \"MS Shell Dlg 2\";}"))
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 131, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 0);"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Icons/MB_0008_phone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 0, 131, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Icons/2fUZnI4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 10, 71, 41))
        self.label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.numberLineedit = QtGui.QLineEdit(self.frame_2)
        self.numberLineedit.setGeometry(QtCore.QRect(60, 9, 241, 51))
        self.numberLineedit.setObjectName(_fromUtf8("numberLineedit"))
        self.verticalLayout_2.addWidget(self.frame_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Elementz_GSM_Utility", None))
        self.pushButton.setText(_translate("Dialog", "Accept", None))
        self.pushButton_2.setText(_translate("Dialog", "Decline", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; color:#ff0000;\">Calling....</span></p></body></html>", None))

import background_rc
