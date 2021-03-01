# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dzial4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_Dzial4Window(object):
    def b1clicked(self):
        a = math.radians(float(self.stopnie.text()))
        self.sinus.setText(str(round(math.sin(a), 4)))
        self.cosinus.setText(str(round(math.cos(a), 4)))
        self.tangens.setText(str(round(math.tan(a), 4)))
        self.radiany.setText(str(round(a, 4)))
        if math.fabs(a)>1:
            self.arkussinus.setText("poza dziedziną")
            self.arkuscosinus.setText("poza dziedziną")
            self.arkustangens.setText("poza dziedziną")
        else:
            self.arkussinus.setText(str(round(math.asin(a), 4)))
            self.arkuscosinus.setText(str(round(math.acos(a), 4)))
            self.arkustangens.setText(str(round(math.atan(a), 4)))
        
    def b2clicked(self):
        self.sinus.setText(str(round(math.sin(float(self.radiany.text())), 4)))
        self.cosinus.setText(str(round(math.cos(float(self.radiany.text())), 4)))
        self.tangens.setText(str(round(math.tan(float(self.radiany.text())), 4)))
        self.stopnie.setText(str(round(math.degrees(float(self.radiany.text())), 4)))
        if math.fabs(float(self.radiany.text()))>1:
            self.arkussinus.setText("poza dziedziną")
            self.arkuscosinus.setText("poza dziedziną")
            self.arkustangens.setText("poza dziedziną")
        else:
            self.arkussinus.setText(str(round(math.asin(float(self.radiany.text())), 4)))
            self.arkuscosinus.setText(str(round(math.acos(float(self.radiany.text())), 4)))
            self.arkustangens.setText(str(round(math.atan(float(self.radiany.text())), 4)))
            
    def setupUi(self, Dzial4Window):
        Dzial4Window.setObjectName("Dzial4Window")
        Dzial4Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dzial4Window)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(30, 50, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1clicked)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stopnie = QtWidgets.QLineEdit(self.centralwidget)
        self.stopnie.setGeometry(QtCore.QRect(210, 80, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stopnie.setFont(font)
        self.stopnie.setObjectName("stopnie")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sinus = QtWidgets.QLabel(self.centralwidget)
        self.sinus.setGeometry(QtCore.QRect(100, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sinus.setFont(font)
        self.sinus.setText("")
        self.sinus.setObjectName("sinus")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cosinus = QtWidgets.QLabel(self.centralwidget)
        self.cosinus.setGeometry(QtCore.QRect(320, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cosinus.setFont(font)
        self.cosinus.setText("")
        self.cosinus.setObjectName("cosinus")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tangens = QtWidgets.QLabel(self.centralwidget)
        self.tangens.setGeometry(QtCore.QRect(570, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tangens.setFont(font)
        self.tangens.setText("")
        self.tangens.setObjectName("tangens")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.radiany = QtWidgets.QLineEdit(self.centralwidget)
        self.radiany.setGeometry(QtCore.QRect(420, 80, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.radiany.setFont(font)
        self.radiany.setObjectName("radiany")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(610, 50, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.b2clicked)
        self.arkussinus = QtWidgets.QLabel(self.centralwidget)
        self.arkussinus.setGeometry(QtCore.QRect(100, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.arkussinus.setFont(font)
        self.arkussinus.setText("")
        self.arkussinus.setObjectName("arkussinus")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 360, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.arkuscosinus = QtWidgets.QLabel(self.centralwidget)
        self.arkuscosinus.setGeometry(QtCore.QRect(320, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.arkuscosinus.setFont(font)
        self.arkuscosinus.setText("")
        self.arkuscosinus.setObjectName("arkuscosinus")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(320, 360, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(570, 360, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.arkustangens = QtWidgets.QLabel(self.centralwidget)
        self.arkustangens.setGeometry(QtCore.QRect(570, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.arkustangens.setFont(font)
        self.arkustangens.setText("")
        self.arkustangens.setObjectName("arkustangens")
        Dzial4Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dzial4Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Dzial4Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dzial4Window)
        self.statusbar.setObjectName("statusbar")
        Dzial4Window.setStatusBar(self.statusbar)

        self.retranslateUi(Dzial4Window)
        QtCore.QMetaObject.connectSlotsByName(Dzial4Window)

    def retranslateUi(self, Dzial4Window):
        _translate = QtCore.QCoreApplication.translate
        Dzial4Window.setWindowTitle(_translate("Dzial4Window", "MainWindow"))
        self.b1.setText(_translate("Dzial4Window", "Przelicz ze stopni"))
        self.label.setText(_translate("Dzial4Window", "Wartość kąta w stopniach"))
        self.label_2.setText(_translate("Dzial4Window", "Sinus"))
        self.label_4.setText(_translate("Dzial4Window", "Cosinus"))
        self.label_6.setText(_translate("Dzial4Window", "Tangens"))
        self.label_10.setText(_translate("Dzial4Window", "Wartość kąta w radianach"))
        self.b2.setText(_translate("Dzial4Window", "Przelicz z radianów"))
        self.label_9.setText(_translate("Dzial4Window", "Arkus sinus"))
        self.label_12.setText(_translate("Dzial4Window", "Arkus cosinus"))
        self.label_13.setText(_translate("Dzial4Window", "Arkus tangens"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dzial4Window = QtWidgets.QMainWindow()
    ui = Ui_Dzial4Window()
    ui.setupUi(Dzial4Window)
    Dzial4Window.show()
    sys.exit(app.exec_())
