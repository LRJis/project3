from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer


class Demo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1300, 850)
        self.bar = QProgressBar(self)
        self.bar.setMinimum(0)
        self.bar.setMaximum(100)

        self.step = 0
        self.timer = QTimer(self)
        self.button = QPushButton('start', self)
        self.button.setGeometry(0, 0, 100, 50)
        self.button_1 = QPushButton('reset', self)
        self.button_1.setGeometry(200, 0, 100, 50)
        self.bar.setGeometry(0, 500, 500, 10)
        self.button.clicked.connect(self.start)
        self.button_1.clicked.connect(self.reset_text)
        self.timer.timeout.connect(self.update_text)

    def start(self):
        if self.button.text() == 'start':
            self.button.setText('stop')
            self.timer.start(100)
        else:
            self.button.setText('start')
            self.timer.stop()

    def update_text(self):
        self.step = self.step + 1
        self.bar.setValue(self.step)

        if self.step >= 100:
            self.button.setText('start')
            self.timer.stop()
            self.step = 0

    def reset_text(self):
        self.bar.reset()
        self.button.setText('start')
        self.timer.stop()
        self.step = 0
