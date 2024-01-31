import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QWidget


def isInsideCadenas(pos) -> bool:
    x, y = pos.x(), pos.y()
    return (x - 75) ** 2 + (y - 75) ** 2 <= 625


class Cadenas(QWidget):
    lockStateChanged = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.locked = True
        self.lockStateChanged.connect(self.slot)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Cadenas')

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if isInsideCadenas(event.pos()):
                self.lockStateChanged.emit(self.locked)

    def slot(self, value: bool):
        self.locked = not value
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCadenas(qp)
        qp.end()

    def drawCadenas(self, qp):
        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        if self.locked:
            qp.setBrush(QBrush(QColor(255, 0, 0)))
        else:
            qp.setBrush(QBrush(QColor(0, 255, 0)))

        qp.drawEllipse(50, 50, 50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cadenas()
    ex.show()
    sys.exit(app.exec())
