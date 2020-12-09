import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__'

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 400)
        self.setWindowTitle('TICKER')
        self.setWindowIcon(QIcon('iconfinder_coin-9_3338901.png'))

        btn = QPushButton('버튼1', self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

        btn2 = QPushButton('버튼2', self)
        btn2.move(10, 40)
        btn2.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼클릭!")

app = QApplication(sys.argv)

window = MyWindow()
window.show()



# label = QLabel('hello')
# label.show()
# btn = QPushButton('hello')
# btn.show()


app.exec_()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
