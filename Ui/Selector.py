from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QToolButton
from plate import Plate

import App

_ = Plate(locale="es_CO")


class Selector(QLabel):

    def __init__(self, parent):
        super(Selector, self).__init__(parent)

        self.left = QToolButton(self)
        font = QFont("Tahoma")
        font.setPixelSize(20)
        self.__loadedTypes = list()
        self.__currentType = None
        self.left.setFont(font)
        self.left.setText("◄")
        self.left.resize(25, 25)
        self.left.setDisabled(True)
        self.left.clicked.connect(lambda: self.__change(-1))
        self.__types = QLabel(self)
        self.__setText(SelectorTexts.load)
        self.__types.setContentsMargins(20, 0, 20, 0)
        self.__types.move(self.left.geometry().topRight())
        self.__types.resize(200, 25)
        self.__types.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right = QToolButton(self)
        self.right.setFont(font)
        self.right.setText("►")
        self.right.resize(25, 25)
        self.right.move(self.__types.geometry().topRight())
        self.right.setDisabled(True)
        self.right.clicked.connect(lambda: self.__change(1))

        self.resize(self.right.geometry().right() + 2, self.right.geometry().bottom() + 2)
        self.setStyleSheet("border: 1px groove gray;")

    def setTypes(self, types: list[str]):
        pass

    def __setText(self, text):

        text = _(text.__str__())

        if len(text) > 26:
            text = text[:24] + "..."

        self.__types.setText(text)

    def loadTypes(self, i0: list[App.ImageTypes]):

        self.__loadedTypes = i0
        self.__currentType = self.__loadedTypes[0]
        self.__setText(self.__loadedTypes[0])

        if len(i0) > 1:
            self.left.setEnabled(True)
            self.right.setEnabled(True)

    def __change(self, move: int):
        if move < 0:
            if self.__getCurentIndex == 0:
                self.__currentType = self.__loadedTypes[len(self.__loadedTypes) - 1]

            else:
                self.__currentType = self.__loadedTypes[self.__getCurentIndex - 1]

            self.__setText(self.__currentType)

        elif move > 0:
            if self.__getCurentIndex == len(self.__loadedTypes) - 1:
                self.__currentType = self.__loadedTypes[0]

            else:
                self.__currentType = self.__loadedTypes[self.__getCurentIndex + 1]

            self.__setText(self.__currentType)

        print(self.__getCurentIndex)

    @property
    def __getCurentIndex(self):
        return self.__loadedTypes.index(self.__currentType)


class SelectorTexts(Enum):

    load = 0
