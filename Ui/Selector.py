from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QPushButton


class Selector(QLabel):

    def __init__(self, parent):
        super(Selector, self).__init__(parent)

        self.left = QPushButton(self)
        font = QFont("Tahoma")
        font.setPixelSize(20)
        self.left.setFont(font)
        self.left.setText("◄")
        self.left.resize(25, 25)
        self.left.setDisabled(True)
        self.__types = QLabel(self)
        self.__setText("Cargar tipos de imagen")
        print(self.__types.font().pointSize())
        self.__types.setContentsMargins(20, 0, 20, 0)
        self.__types.move(self.left.geometry().topRight())
        self.__types.resize(200, 25)
        self.__types.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right = QPushButton(self)
        self.right.setFont(font)
        self.right.setText("►")
        self.right.resize(25, 25)
        self.right.move(self.__types.geometry().topRight())
        self.right.setDisabled(True)

        self.resize(self.right.geometry().right() + 2, self.right.geometry().bottom() + 2)
        self.setStyleSheet("border: 1px groove gray;")

    def setTypes(self, types: list[str]):
        pass

    def __setText(self, text):
        print(len(text))

        if len(text) > 26:
            text = text[:24] + "..."

        self.__types.setText(text)
