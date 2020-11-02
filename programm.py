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
