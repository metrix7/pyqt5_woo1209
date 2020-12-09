import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit
import pybithumb


tickers = ['BTC', 'ETH', 'XRP', 'BCH']
form_class = uic.loadUiType('MyWindow02.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.tick)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
        # self.timer.timeout.connect(self.btn_clicked)
        # self.timer.timeout.connect(self.tick)

    def timeout(self):
        # print('1sec!!!!!!!!!!!!!!!')
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWoo.setItem(i, 0, item)

            price, last_ma5, state = self.get_market_infos(ticker)
            self.tableWoo.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWoo.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tableWoo.setItem(i, 3, QTableWidgetItem(state))

    def btn_clicked(self):
        print("버튼클릭!")

    def tick(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString('hh:mm:ss')
        self.statusBar().showMessage(str_time)

        # price = pykorbit.get_current_price('BTC')
        # print(price)
        # self.lineEdit.setText(str(price))

    def get_market_infos(self, ticker):
        df = pybithumb.get_candlestick(ticker)
        ma5 = df['close'].rolling(window=5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)

        state = None
        if price > last_ma5:
            state = '상승장'
        else:
            state = '하락장'
        return price, last_ma5, state


app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec_()

'''
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
'''
