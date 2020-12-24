from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mc


#############################################################
#StyleSheet

StyleSheet = '''
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
    background-color: rgb(65, 65, 65);
    border: 2px solid rgb(65, 65, 65);
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
    Background-color: rgb(65, 65, 65);
    color: white;
    text-align: center;
    font-size: 15px;
    font-weight: bold;
    padding-top: -4px;
}
'''
StyleSheetT = """
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
    Background-color: darkred;
    color: white;
    text-align: center;
    font-size: 15px;
    font-weight: bold;
}
"""

##############################################################
#Bildschirm
class UIWindow(object):
    def setupUi(self, MainWindow):
        timer = QTimer(MainWindow)
        timer.timeout.connect(self.showTime)
        timer.start(1000)   
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
        self.labelTime.setGeometry(QtCore.QRect(465, 43, 300, 30))
        self.labelTime.setAlignment(QtCore.Qt.AlignRight)
        self.labelTime.setStyleSheet(
            "font-family: Arial;\n"
            "font-size: 25px;\n"
            "color: white;\n"
        )

        self.labelDate = QtWidgets.QLabel(MainWindow)
        self.labelDate.setGeometry(QtCore.QRect(358, 43, 300, 30))
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

        self.labelC = QtWidgets.QLabel(MainWindow)
        self.labelC.setGeometry(QtCore.QRect(464, 18, 300, 25))
        self.labelC.setAlignment(QtCore.Qt.AlignRight)
        self.labelC.setStyleSheet(
            "font-family: bahnschrift;\n"
            "font-size: 20px;\n"
            "color: grey;\n"
        )
#####################################################################
#Buttons

        self.label.setObjectName("X")
        self.pushButtonE = QtWidgets.QPushButton(MainWindow)
        self.pushButtonE.setMouseTracking(False)
        self.pushButtonE.setAutoFillBackground(False)
        self.pushButtonE.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.pushButtonE.setGeometry(QtCore.QRect(372, 410, 50, 50))
        self.pushButtonE.setStyleSheet(StyleSheet)

        self.label.setObjectName("LoadData")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.pushButton.setGeometry(QtCore.QRect(28, 410, 225, 50))
        self.pushButton.setStyleSheet(StyleSheet)
    
#####################################################################
#Funktionen
        def abbrechen():
            sys.exit()

        self.pushButton.clicked.connect(self.select_data)

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
            mycursor.execute("SELECT * FROM sensor_status ORDER BY ID DESC ")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
 
            if row_data > 30:
                self.tableWidget.horizontalHeader().setStyleSheet(StyleSheetT)
    
            else: 
                None

        except mc.Error as e:
            print("Error")

##############################################################################
#Datum & Uhrzeit

    def retranslateUi(self, MainWindow):
        date = QDate.currentDate()
        datestr = date.toString()

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "YOKAI"))
        self.pushButtonE.setText(_translate("MainWindow", "X"))
        self.pushButton.setText(_translate("MainWindow", "Daten anzeigen:"))
        self.labelC.setText(_translate("MainWindow", "©Made by Celil TAN"))
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