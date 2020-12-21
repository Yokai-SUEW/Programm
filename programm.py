from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def Fenster():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(550, 350, 720, 480)
    win.setWindowTitle("Yokai - Serverüberwachung")


    win.show()
    sys.exit(app.exec_())

Fenster()


class Ui_MainWindow(object):
    def loadData(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))



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