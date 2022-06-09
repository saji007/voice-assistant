# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'victorui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_victorGUI(object):
    def setupUi(self, victorGUI):
        victorGUI.setObjectName("victorGUI")
        victorGUI.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(victorGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -190, 1941, 1371))
        self.label.setStyleSheet("background:transparent;\n"
"border-radius:none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("GIF/tuse.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1000, 130, 361, 331))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("GIF/round_orig.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 401, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("GIF/Jarvis_Loading_Screen.gif"))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 350, 351, 71))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 540, 351, 71))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1620, 570, 191, 61))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 52);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1620, 260, 181, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 52);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(850, 490, 611, 181))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("GIF/78_04_article.gif"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 750, 401, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("GIF/J4o.gif"))
        self.label_5.setObjectName("label_5")
        victorGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(victorGUI)
        self.statusbar.setObjectName("statusbar")
        victorGUI.setStatusBar(self.statusbar)

        self.retranslateUi(victorGUI)
        QtCore.QMetaObject.connectSlotsByName(victorGUI)

    def retranslateUi(self, victorGUI):
        _translate = QtCore.QCoreApplication.translate
        victorGUI.setWindowTitle(_translate("victorGUI", "MainWindow"))
        self.pushButton.setText(_translate("victorGUI", "RUN"))
        self.pushButton_2.setText(_translate("victorGUI", "TERMINATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    victorGUI = QtWidgets.QMainWindow()
    ui = Ui_victorGUI()
    ui.setupUi(victorGUI)
    victorGUI.show()
    sys.exit(app.exec_())