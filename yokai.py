from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication , QMainWindow , QPushButton , QWidget
import mysql.connector
from mysql.connector import Error

################################################################
#MySQL - Connector

mydb = mysql.connector.connect(
    host="yokai.ddns.net",
    user="root",
    passwd="292726242528",
    database="yokai"
    )


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sensor_status")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)

###############################################################
#Tabelle



class UIWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setGeometry(600, 350, 800, 480)
        MainWindow.setFixedSize(800, 480)
        MainWindow.setStyleSheet("background-color: #201f1f;")
        MainWindow.setWindowIcon(QtGui.QIcon('hintergrund.png'))
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(325, 0, 200, 100))
        self.label.setStyleSheet(
            "color: white;\n"
            "font-family: bahnschrift;\n"
            "font-size: 60px;\n"
            ""
            )


        self.label.setObjectName("X")
        self.pushButtonE = QtWidgets.QPushButton(MainWindow)
        self.pushButtonE.setGeometry(QtCore.QRect(375, 410, 50, 50))
        self.pushButtonE.setStyleSheet(
            "border: 2px solid white;\n"
            "border-radius: 25px;\n"
            "font-family: Arial;\n"
            "color: white;\n"
            "font-size: 25px;\n"
            "\n"
            ""
            )


######################################################################
#Funktionen

        def abbrechen():
            sys.exit()



        self.pushButtonE.clicked.connect(abbrechen)

        self.pushButtonE.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yokai - Serverüberwachung"))
        self.label.setText(_translate("MainWindow", "YOKAI"))
        self.pushButtonE.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())