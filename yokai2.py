# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\celil\Documents\GitHub\Programm\yokai.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1001, 569)
        dialog.setStyleSheet("background-color: #201f1f;")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(410, 10, 171, 111))
        self.label.setStyleSheet("color: white;\n"
"font-family: bahnschrift;\n"
"font-size: 60px;\n"
"padding-right: 20px;\n"
"padding-left: 20px;\n"
"")
   
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 500, 71, 41))
        self.pushButton.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"font-family: Arial;\n"
"\n"
"QPushButton {\n"
"    background-color: black;\n"
"    margin-bottom: 3px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Yokai - Serverüberwachung"))
        self.label.setText(_translate("dialog", "Yokai"))
        self.pushButton.setText(_translate("dialog", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())