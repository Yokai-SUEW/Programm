from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication , QMainWindow , QPushButton , QWidget, QFrame, QHBoxLayout
import mysql.connector
from mysql.connector import Error

#############################################################
#MySQL - Connector

mydb = mysql.connector.connect(
    host="192.168.0.45",
    user="halil",
    passwd="root",
    database="yokai",
    )

"""
class Ui_MainWindow(object):
    def loadData(self):

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
"""

#############################################################
#StyleSheet

StyleSheet = '''
QPushButton {
    background-color: grey;
    border: 2px solid grey;
    border-radius: 25px;
    font-family: Arial;
    color: white;
    font-size: 25px;
    text-align: center;
}

QPushButton::hover {
    background-color: darkred;
    border: 2px solid darkred;
    border-radius: 12px;
    font-family: Arial;
    color: white;
    font-size: 27px;
}

QPushButton::pressed {
    background-color: #201f1f;
    border: 2px solid darkred;
    color: white;
}
'''

StyleSheetTable = '''
QTableWidget {
        color: white;
        background-color: #201f1f;
        width: 70%;
        height: 60%;
        font-family: bahnschrift;
        font-size: 20px;
        text-align: center;
        border-collapse: collapse;
}

::section {
    Background-color: green;
    color: white;
    text-align: center;
    font-size: 15px;
    font-weight: bold;
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
        self.tableWidget = QTableWidget(MainWindow)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Temperatur"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Luftfeuchtigkeit"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Datum & Uhrzeit"))
        self.tableWidget.setGeometry(QtCore.QRect(30,95,740,291))
        self.tableWidget.setStyleSheet(StyleSheetTable)
        self.tableWidget.horizontalHeader().setStyleSheet(StyleSheetTable)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionsClickable(False)

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM sensor_status ORDER BY ID DESC, Temperatur DESC, Luftfeuchtigkeit DESC, Datum DESC")
        myresult = mycursor.fetchall()
        self.tableWidget.setRowCount(len(myresult))
        self.tableWidget.setColumnCount(4)

        row = 0
        while True:
            sqlRow = mycursor.fetchone()
            if sqlRow == None:
                break
            for col in range(0, 8):
                self.tableWidget.setItem(row, col, QtGui.QTableWidgetItem(sqlRow[col]))
            row += 1

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
        self.pushButtonE.setMouseTracking(False)
        self.pushButtonE.setAutoFillBackground(False)
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