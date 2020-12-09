import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

class Worker(QThread):
    def run(self):
        while True:
            print('hi')
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()


app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()


