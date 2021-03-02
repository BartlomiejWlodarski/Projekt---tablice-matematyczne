# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dzial8.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import math
import statistics
tablica = []
iloczyn = 1

class Ui_Dzial8Window(object):
    def b1Clicked(self):
        tablica.append(float(self.element.text()))
        global iloczyn
        iloczyn *= float(self.element.text())

    def b2Clicked(self):
        suma = sum(tablica)
        self.arytmetyczna.setText(str(round((suma / len(tablica)), 4)))
        print(iloczyn)
        self.geometryczna.setText(str(round(iloczyn**(1/len(tablica)), 4)))
        self.mediana.setText(str(statistics.median(tablica)))

    def b3Clicked(self):
        tablica.clear()
        global iloczyn
        iloczyn = 1

    def setupUi(self, Dzial8Window):
        Dzial8Window.setObjectName("Dzial8Window")
        Dzial8Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dzial8Window)
        self.centralwidget.setObjectName("centralwidget")
        self.element = QtWidgets.QLineEdit(self.centralwidget)
        self.element.setGeometry(QtCore.QRect(190, 40, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.element.setFont(font)
        self.element.setObjectName("element")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(380, 40, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1Clicked)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 300, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 300, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 300, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 140, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(200, 180, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.b2Clicked)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(400, 180, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.b3Clicked)
        self.arytmetyczna = QtWidgets.QLabel(self.centralwidget)
        self.arytmetyczna.setGeometry(QtCore.QRect(30, 340, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.arytmetyczna.setFont(font)
        self.arytmetyczna.setObjectName("arytmetyczna")
        self.geometryczna = QtWidgets.QLabel(self.centralwidget)
        self.geometryczna.setGeometry(QtCore.QRect(280, 340, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.geometryczna.setFont(font)
        self.geometryczna.setObjectName("geometryczna")
        self.mediana = QtWidgets.QLabel(self.centralwidget)
        self.mediana.setGeometry(QtCore.QRect(530, 340, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mediana.setFont(font)
        self.mediana.setObjectName("mediana")
        Dzial8Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dzial8Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Dzial8Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dzial8Window)
        self.statusbar.setObjectName("statusbar")
        Dzial8Window.setStatusBar(self.statusbar)

        self.retranslateUi(Dzial8Window)
        QtCore.QMetaObject.connectSlotsByName(Dzial8Window)

    def retranslateUi(self, Dzial8Window):
        _translate = QtCore.QCoreApplication.translate
        Dzial8Window.setWindowTitle(_translate("Dzial8Window", "MainWindow"))
        self.b1.setText(_translate("Dzial8Window", "Dodaj element"))
        self.label.setText(_translate("Dzial8Window", "Średnia arytmetyczna"))
        self.label_2.setText(_translate("Dzial8Window", "Średnia geometryczna"))
        self.label_3.setText(_translate("Dzial8Window", "Mediana"))
        self.b2.setText(_translate("Dzial8Window", "Oblicz dane "))
        self.b3.setText(_translate("Dzial8Window", "Usuń dane "))
        self.arytmetyczna.setText(_translate("Dzial8Window", "(wynik)"))
        self.geometryczna.setText(_translate("Dzial8Window", "(wynik)"))
        self.mediana.setText(_translate("Dzial8Window", "(wynik)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dzial8Window = QtWidgets.QMainWindow()
    ui = Ui_Dzial8Window()
    ui.setupUi(Dzial8Window)
    Dzial8Window.show()
    sys.exit(app.exec_())