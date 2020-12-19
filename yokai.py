from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication , QMainWindow , QPushButton , QWidget, QFrame, QHBoxLayout
import mysql.connector
from mysql.connector import Error

################################################################
#MySQL - Connector
'''
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
'''
for row in myresult:
    print(row)
'''
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
    border: 2px solid #201f1f;
    color: #201f1f;
}

'''

StyleSheetTable = '''
QTableWidget {
        color: white;
        background-color: grey;
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
}
'''

StyleSheetTable2 = """
::section {
    background-color: red;
    color: white;
}
"""

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
        self.tableWidget.setGeometry(QtCore.QRect(175,95,457,291))
        self.tableWidget.setStyleSheet(StyleSheetTable)
        self.tableWidget.horizontalHeader().setStyleSheet(StyleSheetTable)
        self.tableWidget.verticalHeader().setStyleSheet(StyleSheetTable2)

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