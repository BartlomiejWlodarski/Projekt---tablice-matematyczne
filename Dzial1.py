# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dzial1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ciagA import ciagA
from ciagG import ciagG
from ciagZ import ciagZ
import math

class Ui_Dzial1Window(object):
    def b1Clicked(self):
        c1 = ciagA(int(self.a1_a.text()), int(self.r_a.text()), int(self.n_a.text()))
        self.wynik_a.setText(str(c1.get_wynik()))
    
    def b2Clicked(self):
        c2 = ciagG(int(self.a1_g.text()), int(self.q_g.text()), int(self.n_g.text()))
        self.wynik_g.setText(str(c2.get_wynik()))

    def b3Clicked(self):
        if math.fabs(float(self.q_z.text()))>1:
            self.wynik_z.setText("wpisano błędny iloraz, |q| musi być < 1")
        else:
            c3 = ciagZ(float(self.a1_z.text()), float(self.q_z.text()))
            self.wynik_z.setText(str(c3.get_wynik()))

    def bKoniecClicked(self):
        print("")

    def setupUi(self, Dzial1Window):
        Dzial1Window.setObjectName("Dzial1Window")
        Dzial1Window.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(Dzial1Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 40, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.a1_a = QtWidgets.QLineEdit(self.centralwidget)
        self.a1_a.setGeometry(QtCore.QRect(300, 120, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a1_a.setFont(font)
        self.a1_a.setObjectName("a1_a")

        self.labela1 = QtWidgets.QLabel(self.centralwidget)
        self.labela1.setGeometry(QtCore.QRect(300, 161, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labela1.setFont(font)
        self.label.setObjectName("labela1")

        self.r_a = QtWidgets.QLineEdit(self.centralwidget)
        self.r_a.setGeometry(QtCore.QRect(400, 120, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.r_a.setFont(font)
        self.r_a.setObjectName("r_a")

        self.labelr_a = QtWidgets.QLabel(self.centralwidget)
        self.labelr_a.setGeometry(QtCore.QRect(400, 161, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelr_a.setFont(font)
        self.labelr_a.setObjectName("labelr_a")

        self.n_a = QtWidgets.QLineEdit(self.centralwidget)
        self.n_a.setGeometry(QtCore.QRect(500, 120, 140, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_a.setFont(font)
        self.n_a.setObjectName("n_a")

        self.labeln_a = QtWidgets.QLabel(self.centralwidget)
        self.labeln_a.setGeometry(QtCore.QRect(500, 161, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeln_a.setFont(font)
        self.labeln_a.setObjectName("labelr_n")

        self.wynik_a = QtWidgets.QLabel(self.centralwidget)
        self.wynik_a.setGeometry(QtCore.QRect(650, 120, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wynik_a.setFont(font)
        self.wynik_a.setObjectName("wynik_a")

        self.labelw_a = QtWidgets.QLabel(self.centralwidget)
        self.labelw_a.setGeometry(QtCore.QRect(650, 161, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelw_a.setFont(font)
        self.labelw_a.setObjectName("labelw_a")

        self.a1_g = QtWidgets.QLineEdit(self.centralwidget)
        self.a1_g.setGeometry(QtCore.QRect(300, 230, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a1_g.setFont(font)
        self.a1_g.setObjectName("a1_g")

        self.labela1_g = QtWidgets.QLabel(self.centralwidget)
        self.labela1_g.setGeometry(QtCore.QRect(300, 271, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labela1_g.setFont(font)
        self.labela1_g.setObjectName("labela1_g")

        self.q_g = QtWidgets.QLineEdit(self.centralwidget)
        self.q_g.setGeometry(QtCore.QRect(400, 230, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q_g.setFont(font)
        self.q_g.setObjectName("q_g")

        self.labelq_g = QtWidgets.QLabel(self.centralwidget)
        self.labelq_g.setGeometry(QtCore.QRect(400, 271, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelq_g.setFont(font)
        self.labelq_g.setObjectName("labelq_g")

        self.n_g = QtWidgets.QLineEdit(self.centralwidget)
        self.n_g.setGeometry(QtCore.QRect(500, 230, 140, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.n_g.setFont(font)
        self.n_g.setObjectName("n_g")

        self.labeln_g = QtWidgets.QLabel(self.centralwidget)
        self.labeln_g.setGeometry(QtCore.QRect(500, 271, 140, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeln_g.setFont(font)
        self.labeln_g.setObjectName("labeln_g")

        self.wynik_g = QtWidgets.QLabel(self.centralwidget)
        self.wynik_g.setGeometry(QtCore.QRect(650, 230, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wynik_g.setFont(font)
        self.wynik_g.setObjectName("wynik_g")

        self.labelw_g = QtWidgets.QLabel(self.centralwidget)
        self.labelw_g.setGeometry(QtCore.QRect(650, 271, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelw_g.setFont(font)
        self.labelw_g.setObjectName("labelw_g")

        self.a1_z = QtWidgets.QLineEdit(self.centralwidget)
        self.a1_z.setGeometry(QtCore.QRect(300, 340, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a1_z.setFont(font)
        self.a1_z.setObjectName("a1_z")

        self.labela1_z = QtWidgets.QLabel(self.centralwidget)
        self.labela1_z.setGeometry(QtCore.QRect(300, 381, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labela1_z.setFont(font)
        self.labela1_z.setObjectName("labela1_z")

        self.q_z = QtWidgets.QLineEdit(self.centralwidget)
        self.q_z.setGeometry(QtCore.QRect(400, 340, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q_z.setFont(font)
        self.q_z.setObjectName("q_z")

        self.labelq_z = QtWidgets.QLabel(self.centralwidget)
        self.labelq_z.setGeometry(QtCore.QRect(400, 381, 90, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelq_z.setFont(font)
        self.labelq_z.setObjectName("labelq_z")

        self.wynik_z = QtWidgets.QLabel(self.centralwidget)
        self.wynik_z.setGeometry(QtCore.QRect(650, 340, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wynik_z.setFont(font)
        self.wynik_z.setObjectName("wynik_z")

        self.labelw_z = QtWidgets.QLabel(self.centralwidget)
        self.labelw_z.setGeometry(QtCore.QRect(650, 381, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelw_z.setFont(font)
        self.labelw_z.setObjectName("labelw_z")

        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(90, 120, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1Clicked)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(90, 230, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.b2Clicked)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(90, 340, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.b3Clicked)
        self.bKoniec = QtWidgets.QPushButton(self.centralwidget)
        self.bKoniec.setGeometry(QtCore.QRect(300, 450, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bKoniec.setFont(font)
        self.bKoniec.setObjectName("bKoniec")
        self.bKoniec.clicked.connect(self.bKoniecClicked)
        Dzial1Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dzial1Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Dzial1Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dzial1Window)
        self.statusbar.setObjectName("statusbar")
        Dzial1Window.setStatusBar(self.statusbar)

        self.retranslateUi(Dzial1Window)
        QtCore.QMetaObject.connectSlotsByName(Dzial1Window)

    def retranslateUi(self, Dzial1Window):
        _translate = QtCore.QCoreApplication.translate
        Dzial1Window.setWindowTitle(_translate("Dzial1Window", "MainWindow"))
        self.label.setText(_translate("Dzial1Window", "Ciągi"))
        self.labela1.setText(_translate("Dzial1Window", "wartość a1"))
        self.labelr_a.setText(_translate("Dzial1Window", "wartość r"))
        self.labeln_a.setText(_translate("Dzial1Window", "liczba wyrazów"))
        self.wynik_a.setText(_translate("Dzial1Window", "                       (wynik)"))
        self.labelw_a.setText(_translate("Dzial1Window", "suma wyrazów ciągu arytmetycznego"))
        self.labela1_g.setText(_translate("Dzial1Window", "wartość a1"))
        self.labelq_g.setText(_translate("Dzial1Window", "wartość q"))
        self.labeln_g.setText(_translate("Dzial1Window", "liczba wyrazów"))
        self.wynik_g.setText(_translate("Dzial1Window", "                       (wynik)"))
        self.labelw_g.setText(_translate("Dzial1Window", "suma wyrazów ciągu geometrycznego"))
        self.labela1_z.setText(_translate("Dzial1Window", "wartość a1"))
        self.labelq_z.setText(_translate("Dzial1Window", "wartość q"))
        self.wynik_z.setText(_translate("Dzial1Window", "                       (wynik)"))
        self.labelw_z.setText(_translate("Dzial1Window", "suma wyrazów ciągu zbieżnego"))
        self.b1.setText(_translate("Dzial1Window", "Oblicz"))
        self.b2.setText(_translate("Dzial1Window", "Oblicz"))
        self.b3.setText(_translate("Dzial1Window", "Oblicz"))
        self.bKoniec.setText(_translate("Dzial1Window", "Wyjdź"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dzial1Window = QtWidgets.QMainWindow()
    ui = Ui_Dzial1Window()
    ui.setupUi(Dzial1Window)
    Dzial1Window.show()
    sys.exit(app.exec_())
