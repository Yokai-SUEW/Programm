from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication , QMainWindow , QPushButton , QWidget
import mysql.connector
from mysql.connector import Error

################################################################
#MySQL - Connector

mydb = mysql.connector.connect(
    host="192.168.0.45",
    user="halil",
    passwd="root",
    database="yokai",
    )

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sensor_status")
myresult = mycursor.fetchall()

'''
for row in myresult:
    print(row)
'''
#############################################################
#StyleSheet

StyleSheet = '''
QPushButton {
    background-color: #201f1f;
    border: 2px solid white;
    border-radius: 25px;
    font-family: Arial;
    color: white;
    font-size: 25px;
}

QPushButton::hover {
    background-color: #201f1f;
    border: 2px solid #201f1f;
    border-radius: 25px;
    font-family: Arial;
    color: grey;
    font-size: 30px;
}

QPushButton::pressed {
    background-color: #201f1f;
    border: 2px solid #201f1f;
    color: #201f1f;
}
'''

##############################################################
#Bildschirm

class UIWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setGeometry(600, 350, 800, 480)
        MainWindow.setFixedSize(800, 480)
        MainWindow.setStyleSheet("background-color: #201f1f;")
        MainWindow.setWindowTitle("Yokai-Serverüberwachung")
        MainWindow.setWindowIcon(QtGui.QIcon('../favicon.png'))
        self.tableWidget = QTableWidget(MainWindow)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setGeometry(QtCore.QRect(30,90,500,300))
        self.tableWidget.setStyleSheet(
            "color: white;\n"
            "background-color: black;\n"
            "width: 70%;\n"
            "height: 60%;\n"
            "font-family: bahnschrift;\n"
            "font-size: 20px;\n"
        )

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setAlignment(QtCore.Qt.AlignCenter) 
        self.label.setGeometry(QtCore.QRect(10, 0, 780, 80))
        self.label.setStyleSheet(
            "font-family: bahnschrift;\n"
            "font-size: 60px;\n"
            "color: white;\n"
        )


#####################################################################
#Buttons

        self.label.setObjectName("X")
        self.pushButtonE = QtWidgets.QPushButton(MainWindow)
        self.pushButtonE.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.pushButtonE.setGeometry(QtCore.QRect(375, 410, 50, 50))
        self.pushButtonE.setStyleSheet(StyleSheet)
    
#####################################################################
#Funktionen

        def abbrechen():
            sys.exit()

        self.pushButtonE.clicked.connect(abbrechen)

        self.pushButtonE.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
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