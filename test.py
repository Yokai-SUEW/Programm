import sys 
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWidgets import QVBoxLayout, QLabel 
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import QTimer, QTime, Qt 
  
  
class Window(QWidget): 
  
    def __init__(self): 
        super().__init__() 
  
        # setting geometry of main window 
        self.setGeometry(100, 100, 800, 400) 
  
        # creating a vertical layout 
        layout = QVBoxLayout() 
  
        # creating font object 
        font = QFont('Arial', 120, QFont.Bold) 
  
        # creating a label object 
        self.label = QLabel() 
  
        # setting centre alignment to the label 
        self.label.setAlignment(Qt.AlignCenter) 
  
        # setting font to the label 
        self.label.setFont(font) 
  
        # adding label to the layout 
        layout.addWidget(self.label) 
  
        # setting the layout to main window 
        self.setLayout(layout) 
  
        # creating a timer object 
        timer = QTimer(self) 
  
        # adding action to timer 
        timer.timeout.connect(self.showTime) 
  
        # update the timer every second 
        timer.start(1000) 
  
    # method called by timer 
    def showTime(self): 
  
        # getting current time 
        current_time = QTime.currentTime() 
  
        # converting QTime object to string 
        label_time = current_time.toString('hh:mm:ss') 
  
        # showing it to the label 
        self.label.setText(label_time) 
  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# showing all the widgets 
window.show() 
  
# start the app 
App.exit(App.exec_()) 