import sys
from functools import partial
from PyQt5.QtCore import (QFile, QFileInfo, QSettings, QSignalMapper,
        QTimer,Qt,QByteArray)
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog,
        QMainWindow, QMessageBox, QTextEdit,QMdiArea,QWidget)
from PyQt5.QtGui import QIcon,QKeySequence

from ui_Qtest import Ui_QTaskConfigWindow
#import qrc_resources
import objgraph
import psutil
import gc
from os import getpid
from traceback import print_exc
#from memory_profiler import profile
__version__ = "1.0.0"
from time import sleep

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        fileNewAction = self.createAction("&New", self.fileNew,
                QKeySequence.New, "filenew", "Create a text file")
        fileOpenAction = self.createAction("&Open...", self.fileOpen,
                QKeySequence.Open, "fileopen",
                "Open an existing text file")

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolbar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction))



    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{0}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action


    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    #@profile
    def fileNew(self):
        try:
            print(u'openSystemConfig内存使用：', round(psutil.Process(getpid()).memory_info().rss / 1024 / 1024, 4))
            objgraph.show_growth(shortnames=False)
            self.taskConfigWindow = Ui_QTaskConfigWindow()
            self.mdi.addSubWindow(self.taskConfigWindow).show()
        except Exception as e:
            print(print_exc())

    def fileOpen(self):
        for win_temp in self.mdi.subWindowList():
            win_temp_widget = win_temp.widget()
            if (win_temp_widget is not None) and (isinstance(win_temp_widget, Ui_QTaskConfigWindow)):
                self.mdi.setActiveSubWindow(win_temp)
                self.mdi.closeActiveSubWindow()

        self.taskConfigWindow = None





if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    app.exec_()
