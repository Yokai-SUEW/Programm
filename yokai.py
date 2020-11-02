from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(720, 480)
        dialog.setStyleSheet("background-color: #201f1f;")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(300, 0, 200, 100))
        self.label.setStyleSheet("color: white;\n"
"font-family: bahnschrift;\n"
"font-size: 60px;\n"
"")
        self.label.setObjectName("label")
        self.pushButtonE = QtWidgets.QPushButton(dialog)
        self.pushButtonE.setGeometry(QtCore.QRect(345, 410, 50, 50))
        self.pushButtonE.setStyleSheet("border: 2px solid white;\n"
"border-radius: 25px;\n"
"font-family: Arial;\n"
"color: white;"
"\n"
"}")

        def abbrechen():
            sys.exit()

        self.pushButtonE.clicked.connect(abbrechen)
        

        self.pushButtonE.setObjectName("pushButton")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog) 

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Yokai - Serverüberwachung"))
        self.label.setText(_translate("dialog", "Yokai"))
        self.pushButtonE.setText(_translate("dialog", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
