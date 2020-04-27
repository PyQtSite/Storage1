from UI_demo.Q111 import Ui_Form
from UI_demo.Q111sub import Ui_Q1111
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time


class Mywindow1(QWidget,Ui_Form):
    def __init__(self):
        super(Mywindow1,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hidepushbutton)

        self.label=QLineEdit(self)
        self.label.setText("what")
        self.label.setGeometry(QRect(690, 150, 75, 23))

        self.label.returnPressed.connect(self.returnPress)

        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)

    def returnPress(self):
        print(self.sender())
        self.hide()
        time.sleep(5)
        self.show()



    def hidepushbutton(self):
        print(self.sender())
        self.hide()
        time.sleep(5)
        self.show()

    def hideEvent(self,event):
        super(Mywindow1,self).hideEvent(event)
        print("112121212121",self.sender())

    def showEvent(self,event):
        super(Mywindow1,self).showEvent(event)
        print("11221",self.sender())

    def paintEvent(self,event):
        super(Mywindow1, self).paintEvent(event)
        print("paintEvent",self.sender())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Mywindow()
    myWin.show()
    sys.exit(app.exec_())

