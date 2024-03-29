# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dzial2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import math
from kwadratowa import kwadratowa
class Ui_Dzial2Window(object):
    def b1Clicked(self):
        f1 = kwadratowa(float(self.parametr_a.text()), float(self.parametr_b.text()), float(self.parametr_c.text()))
        self.delta.setText(str(f1.get_delta()))

        if float(self.delta.text()) < 0.0:
            self.x1.setText("Brak x1")
            self.x2.setText("Brak x2")
        else:
            self.x1.setText(str(f1.get_x1()))
            self.x2.setText(str(f1.get_x2()))

        
        self.p.setText(str(f1.get_p()))
        self.q.setText(str(f1.get_q()))
        f1.rysuj_wykres()
        
    def setupUi(self, Dzial2Window):
        Dzial2Window.setObjectName("Dzial2Window")
        Dzial2Window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Dzial2Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.parametr_a = QtWidgets.QLineEdit(self.centralwidget)
        self.parametr_a.setGeometry(QtCore.QRect(80, 110, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parametr_a.setFont(font)
        self.parametr_a.setObjectName("parametr_a")
        self.parametr_b = QtWidgets.QLineEdit(self.centralwidget)
        self.parametr_b.setGeometry(QtCore.QRect(330, 110, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parametr_b.setFont(font)
        self.parametr_b.setObjectName("parametr_b")
        self.parametr_c = QtWidgets.QLineEdit(self.centralwidget)
        self.parametr_c.setGeometry(QtCore.QRect(590, 110, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parametr_c.setFont(font)
        self.parametr_c.setObjectName("parametr_c")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(80, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1Clicked)
        self.delta = QtWidgets.QLabel(self.centralwidget)
        self.delta.setGeometry(QtCore.QRect(350, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delta.setFont(font)
        self.delta.setObjectName("delta")
        self.x1 = QtWidgets.QLabel(self.centralwidget)
        self.x1.setGeometry(QtCore.QRect(480, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x1.setFont(font)
        self.x1.setObjectName("x1")
        self.x2 = QtWidgets.QLabel(self.centralwidget)
        self.x2.setGeometry(QtCore.QRect(610, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x2.setFont(font)
        self.x2.setObjectName("x2")
        self.p = QtWidgets.QLabel(self.centralwidget)
        self.p.setGeometry(QtCore.QRect(320, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p.setFont(font)
        self.p.setObjectName("p")
        self.q = QtWidgets.QLabel(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(530, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q.setFont(font)
        self.q.setObjectName("q")
        Dzial2Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dzial2Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Dzial2Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dzial2Window)
        self.statusbar.setObjectName("statusbar")
        Dzial2Window.setStatusBar(self.statusbar)

        self.retranslateUi(Dzial2Window)
        QtCore.QMetaObject.connectSlotsByName(Dzial2Window)

    def retranslateUi(self, Dzial2Window):
        _translate = QtCore.QCoreApplication.translate
        Dzial2Window.setWindowTitle(_translate("Dzial2Window", "MainWindow"))
        self.label.setText(_translate("Dzial2Window", "Funkcja kwadratowa"))
        self.parametr_a.setText(_translate("Dzial2Window", "a"))
        self.parametr_b.setText(_translate("Dzial2Window", "b"))
        self.parametr_c.setText(_translate("Dzial2Window", "c"))
        self.b1.setText(_translate("Dzial2Window", "Oblicz"))
        self.delta.setText(_translate("Dzial2Window", "Delta"))
        self.x1.setText(_translate("Dzial2Window", "x1"))
        self.x2.setText(_translate("Dzial2Window", "x2"))
        self.p.setText(_translate("Dzial2Window", "współrzędna x paraboli"))
        self.q.setText(_translate("Dzial2Window", "współrzędna y paraboli"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dzial2Window = QtWidgets.QMainWindow()
    ui = Ui_Dzial2Window()
    ui.setupUi(Dzial2Window)
    Dzial2Window.show()
    sys.exit(app.exec_())
