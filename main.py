import sys
import random

from UI import UI_MyWidget

from PyQt6.QtCore import QPointF 
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


def generate_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


class MyWidget(UI_MyWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.setup_drawing_and_draw(self.draw_circle))
        self.current_draw_func = None

    def paintEvent(self, event):
        if self.current_draw_func:
            qp = QPainter()
            qp.begin(self)
            self.current_draw_func(qp)
            qp.end()

    def setup_drawing_and_draw(self, func=None):
        self.current_draw_func = func
        self.update()

    def draw_circle(self, qp: QPainter):
        r = random.randint(20, 100)
        x, y = random.randint(0, self.rect().right()), random.randint(0, self.rect().bottom())
        qp.setBrush(QColor(255, 255, 0, 255))
        qp.drawEllipse(QPointF(x, y), r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())