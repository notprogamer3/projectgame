import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a = random.randrange(50, 200)
        qp.drawEllipse(40, 40, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(400, 40, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(700, 40, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(40, 350, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(40, 600, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(700, 600, a, a)
        a = random.randrange(50, 200)
        qp.drawEllipse(400, 600, a, a)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())