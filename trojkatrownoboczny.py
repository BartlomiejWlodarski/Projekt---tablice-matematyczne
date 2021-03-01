# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trojkatrownoboczny.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_TrojkatRownobocznyWindow(object):
    def b1Clicked(self):
        a1 = float(self.a.text())
        h1 = round(0.5 * round(math.sqrt(3), 4) * a1, 4)
        self.h.setText(str(h1))
        self.pole.setText(str(0.25 * round(math.sqrt(3), 4) * (a1**2)))
        self.r.setText(str(round(h1 / 3, 4)))
        self.R.setText(str(round(2 * h1 / 3, 4)))

    def setupUi(self, TrojkatRownobocznyWindow):
        TrojkatRownobocznyWindow.setObjectName("TrojkatRownobocznyWindow")
        TrojkatRownobocznyWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TrojkatRownobocznyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.a = QtWidgets.QLineEdit(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(180, 70, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.a.setFont(font)
        self.a.setText("")
        self.a.setObjectName("a")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(540, 50, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.b1Clicked)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 240, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 240, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 380, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 380, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.h = QtWidgets.QLabel(self.centralwidget)
        self.h.setGeometry(QtCore.QRect(90, 280, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.h.setFont(font)
        self.h.setObjectName("h")
        self.pole = QtWidgets.QLabel(self.centralwidget)
        self.pole.setGeometry(QtCore.QRect(440, 280, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pole.setFont(font)
        self.pole.setObjectName("pole")
        self.r = QtWidgets.QLabel(self.centralwidget)
        self.r.setGeometry(QtCore.QRect(90, 430, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.r.setFont(font)
        self.r.setObjectName("r")
        self.R = QtWidgets.QLabel(self.centralwidget)
        self.R.setGeometry(QtCore.QRect(440, 430, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.R.setFont(font)
        self.R.setObjectName("R")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 180, 801, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        TrojkatRownobocznyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TrojkatRownobocznyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        TrojkatRownobocznyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TrojkatRownobocznyWindow)
        self.statusbar.setObjectName("statusbar")
        TrojkatRownobocznyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TrojkatRownobocznyWindow)
        QtCore.QMetaObject.connectSlotsByName(TrojkatRownobocznyWindow)

    def retranslateUi(self, TrojkatRownobocznyWindow):
        _translate = QtCore.QCoreApplication.translate
        TrojkatRownobocznyWindow.setWindowTitle(_translate("TrojkatRownobocznyWindow", "MainWindow"))
        self.label.setText(_translate("TrojkatRownobocznyWindow", "Podaj długość boku trójkąta równobocznego"))
        self.b1.setText(_translate("TrojkatRownobocznyWindow", "Oblicz"))
        self.label_2.setText(_translate("TrojkatRownobocznyWindow", "Wysokość trójkąta"))
        self.label_3.setText(_translate("TrojkatRownobocznyWindow", "Pole"))
        self.label_4.setText(_translate("TrojkatRownobocznyWindow", "Promień okręgu wpisangeo"))
        self.label_5.setText(_translate("TrojkatRownobocznyWindow", "Promień okręgu opisanego"))
        self.h.setText(_translate("TrojkatRownobocznyWindow", "(wynik)"))
        self.pole.setText(_translate("TrojkatRownobocznyWindow", "(wynik)"))
        self.r.setText(_translate("TrojkatRownobocznyWindow", "(wynik)"))
        self.R.setText(_translate("TrojkatRownobocznyWindow", "(wynik)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrojkatRownobocznyWindow = QtWidgets.QMainWindow()
    ui = Ui_TrojkatRownobocznyWindow()
    ui.setupUi(TrojkatRownobocznyWindow)
    TrojkatRownobocznyWindow.show()
    sys.exit(app.exec_())
