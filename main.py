import sys
from random import randint

from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_file import Ui_MainWindow


class DrawEllipse(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.setupUi(self)
        self.btn_draw.clicked.connect(self.drawed)

    def paintEvent(self, event):
        if not self.flag:
            return
        qp = QPainter(self)
        qp.begin(self)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setPen(color)
        qp.setBrush(color)
        r = randint(0, 200)
        qp.drawEllipse(randint(0, 500 - r), randint(0, 500 - r), r, r)
        qp.end()
        self.flag = False

    def drawed(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawEllipse()
    ex.show()
    sys.exit(app.exec())
