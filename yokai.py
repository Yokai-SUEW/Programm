# -*- coding: utf-8 -*-
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mc

#############################################################
#StyleSheet

StyleSheetE = '''
QPushButton {
    background-color: rgb(44, 44, 44);
    border: 2px solid rgb(44, 44, 44);
    border-radius: 12px;
    font-family: Arial;
    color: white;
    font-size: 25px;
    text-align: center;
}
QPushButton::hover {
    background-color: darkred;
    border: 2px solid darkred;
    border-radius: 10px;
    font-family: Arial;
    color: white;
    font-size: 25px;
    padding-left: 2px;
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
}
::section {
    background-color: rgb(65, 65, 65);
    color: white;
    text-align: center;
    font-size: 15px;
    font-weight: bold;
    padding-top: -4px;
}
'''
StyleSheetTableM = '''
QTableWidget {
        color: white;
        background-color: #201f1f;
        width: 40%;
        height: 30%;
        font-family: bahnschrift;
        font-size: 15px;
        text-align: center;
}
::section {
    background-color: rgb(50, 0, 0);
    color: white;
    text-align: center;
    font-size: 12px;
    font-weight: bold;
    padding-top: -4px;
}
'''
##############################################################
#Bildschirm

class UIWindow(QMainWindow):
    def setupUi(self, MainWindow):
        timer = QTimer(MainWindow)
        timer2 = QTimer(MainWindow)
        timer.timeout.connect(self.showTime)
        timer.start(30)
        timer2.timeout.connect(self.select_data)
        timer2.start(10000)
        MainWindow.setGeometry(600, 350, 800, 480)
        MainWindow.setFixedSize(800, 480)
        MainWindow.setStyleSheet("background-color: #201f1f;")
        MainWindow.setWindowTitle("Yokai - Überwachung eines Serverschrankes")
        self.tableWidget = QTableWidget(MainWindow)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Temperatur"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Luftfeuchtigkeit"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Datum & Uhrzeit"))
        self.tableWidget.setGeometry(QtCore.QRect(30,95,740,291))
        self.tableWidget.setStyleSheet(StyleSheetTable)
        self.tableWidget.horizontalHeader().setStyleSheet(StyleSheetTable)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setSelectionBehavior(False)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionsClickable(False)

        header2 = self.tableWidget.verticalHeader()
        header2.setSectionsClickable(False)

        self.labelTime = QtWidgets.QLabel(MainWindow)
        self.labelTime.setGeometry(QtCore.QRect(465, 44, 300, 30))
        self.labelTime.setAlignment(QtCore.Qt.AlignRight)
        self.labelTime.setStyleSheet(
            "font-family: Arial;\n"
            "font-size: 25px;\n"
            "color: white;\n"
        )

        self.labelDate = QtWidgets.QLabel(MainWindow)
        self.labelDate.setGeometry(QtCore.QRect(358, 44, 300, 30))
        self.labelDate.setAlignment(QtCore.Qt.AlignRight)
        self.labelDate.setStyleSheet(
            "font-family: Arial;\n"
            "font-size: 25px;\n"
            "color: grey;\n"
        )

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setGeometry(QtCore.QRect(31, 10, 350, 80))
        self.label.setStyleSheet(
            "font-family: bahnschrift;\n"
            "font-size: 60px;\n"
            "color: white;\n"
        )

        self.labelV = QtWidgets.QLabel(MainWindow)
        self.labelV.setGeometry(QtCore.QRect(464, 18, 300, 25))
        self.labelV.setAlignment(QtCore.Qt.AlignRight)
        self.labelV.setStyleSheet(
            "font-family: bahnschrift;\n"
            "font-size: 20px;\n"
            "color: grey;\n"
        )

        self.tableWidgetM = QTableWidget(MainWindow)
        self.tableWidgetM.setColumnCount(3)
        self.tableWidgetM.setGeometry(QtCore.QRect(470, 398, 300, 70))
        self.tableWidgetM.setStyleSheet(StyleSheetTableM)
        self.tableWidgetM.horizontalHeader().setStyleSheet(StyleSheetTableM)
        self.tableWidgetM.verticalHeader().setVisible(False)
        self.tableWidgetM.horizontalHeader().setVisible(True)
        self.tableWidgetM.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetM.setAutoFillBackground(True)
        self.tableWidgetM.setSelectionBehavior(False)
        self.tableWidgetM.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.tableWidgetM.setHorizontalHeaderItem(1, QTableWidgetItem("Temperatur"))
        self.tableWidgetM.setHorizontalHeaderItem(2, QTableWidgetItem("Datum & Uhrzeit"))

        headerM = self.tableWidgetM.horizontalHeader()
        headerM.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        headerM.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        headerM.setSectionsClickable(False)

        header2M = self.tableWidgetM.verticalHeader()
        header2M.setSectionsClickable(False)
#####################################################################
#Buttons

        self.label.setObjectName("X")
        self.pushButtonE = QtWidgets.QPushButton(MainWindow)
        self.pushButtonE.setMouseTracking(False)
        self.pushButtonE.setAutoFillBackground(False)
        self.pushButtonE.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.pushButtonE.setGeometry(QtCore.QRect(372, 410, 50, 50))
        self.pushButtonE.setStyleSheet(StyleSheetE)
    
#####################################################################
#Funktionen
        def abbrechen():
            sys.exit()


        self.pushButtonE.clicked.connect(abbrechen)

        self.pushButtonE.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#####################################################################
#Daten ablesen / Datenbank Verbindung

    def select_data(self):
        try:
            mydb = mc.connect(
                host="192.168.0.45",
                user="halil",
                password="root",
                database="yokai"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT id, Temperatur, Luftfeuchtigkeit, datum, active FROM sensor_status ORDER BY ID DESC")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.tableWidget.setItem(row_number, column_number, item)

            active = mydb.cursor()
            active.execute("SELECT id, Temperatur, datum FROM sensor_status WHERE active = 1; ")
            ergebnis = active.fetchall()

            self.tableWidgetM.setRowCount(0)
            for row_numberM, row_dataM in enumerate(ergebnis):
                self.tableWidgetM.insertRow(row_numberM)
                for column_numberM, dataM in enumerate(row_dataM):
                    itemM = QTableWidgetItem(str(dataM))
                    itemM.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.tableWidgetM.setItem(row_numberM, column_numberM, itemM)

        except mc.Error as e:
            print("Es konnte keine Verbindung zur Datenbank hergestellt werden!")
            print("Bitte versuchen Sie es später noch einmal.")

##############################################################################
#Datum & Uhrzeit

    def retranslateUi(self, MainWindow):
        date = QDate.currentDate()
        datestr = date.toString()

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "YOKAI"))
        self.pushButtonE.setText(_translate("MainWindow", "X"))
        self.labelV.setText(_translate("MainWindow", "version 1.2"))
        self.labelDate.setText(_translate("MainWindow", datestr + " /"))
        

    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString("hh:mm:ss")
        self.labelTime.setText(label_time)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())