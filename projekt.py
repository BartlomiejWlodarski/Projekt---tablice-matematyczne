# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projekt.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Dzial1 import Ui_Dzial1Window
from Dzial2 import Ui_Dzial2Window
from Dzial3 import Ui_Dzial3Window
from Dzial4 import Ui_Dzial4Window
from Dzial5 import Ui_Dzial5Window
from Dzial6 import Ui_Dzial6Window

class Ui_ProjektWindow(object):
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dzial1Window()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dzial2Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dzial3Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dzial4Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dzial5Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow6(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dzial6Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def bKoniecClicked(self):
        ProjektWindow.close()

    def setupUi(self, ProjektWindow):
        ProjektWindow.setObjectName("ProjektWindow")
        ProjektWindow.resize(800, 669)
        self.centralwidget = QtWidgets.QWidget(ProjektWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(120, 110, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.openWindow1)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(120, 220, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.openWindow2)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(120, 330, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.openWindow3)
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(120, 430, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.openWindow4)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(500, 110, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.openWindow5)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(500, 220, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b6.setFont(font)
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.openWindow6)
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(500, 330, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b7.setFont(font)
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(500, 430, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.b8.setFont(font)
        self.b8.setObjectName("b8")
        self.bKoniec = QtWidgets.QPushButton(self.centralwidget)
        self.bKoniec.setGeometry(QtCore.QRect(310, 530, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bKoniec.setFont(font)
        self.bKoniec.setObjectName("bKoniec")
        self.bKoniec.clicked.connect(self.bKoniecClicked)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        ProjektWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProjektWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ProjektWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProjektWindow)
        self.statusbar.setObjectName("statusbar")
        ProjektWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProjektWindow)
        QtCore.QMetaObject.connectSlotsByName(ProjektWindow)

    def retranslateUi(self, ProjektWindow):
        _translate = QtCore.QCoreApplication.translate
        ProjektWindow.setWindowTitle(_translate("ProjektWindow", "MainWindow"))
        self.b1.setText(_translate("ProjektWindow", "Ciągi"))
        self.b2.setText(_translate("ProjektWindow", "Funkcja kwadratowa"))
        self.b3.setText(_translate("ProjektWindow", "Geometria analityczna"))
        self.b4.setText(_translate("ProjektWindow", "Trygonometria"))
        self.b5.setText(_translate("ProjektWindow", "Logarytmy"))
        self.b6.setText(_translate("ProjektWindow", "Planimetria"))
        self.b7.setText(_translate("ProjektWindow", "Dział 7"))
        self.b8.setText(_translate("ProjektWindow", "Dział 8"))
        self.bKoniec.setText(_translate("ProjektWindow", "Zakończ program"))
        self.label.setText(_translate("ProjektWindow", "Wybierz dział"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjektWindow = QtWidgets.QMainWindow()
    ui = Ui_ProjektWindow()
    ui.setupUi(ProjektWindow)
    ProjektWindow.show()
    sys.exit(app.exec_())