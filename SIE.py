# This is just a Simple Image Editor, for that reason the edition funtions may not be too complicated
#
# Program made by @FunkyoEnma
# https://linktr.ee/FunkyoEnma

import sys

from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


from CheckArgs import CheckArgsv
import Ui

args = CheckArgsv(sys.argv)


class MainUi(QMainWindow):

    def __init__(self, image: str):
        super(MainUi, self).__init__()
        self.resize(400, 500)

        self.move(QPoint(app.primaryScreen().geometry().center().x() - int(self.width() / 2),
                         app.primaryScreen().geometry().center().y() - 40 - int(self.height() / 2)))

        self.type_selector = Ui.ImageTypeSel(self)
        self.imageTypes = list()
        self.type_selector.accept.clicked.connect(lambda:  self.close_selector())

    def close_selector(self):
        self.imageTypes = self.type_selector.getTypes(True)
        self.load_editor()

    def load_editor(self):
        print(self.imageTypes)

        self.__selector = Ui.Selector(self)
        self.__selector.move((int(self.size().width() / 2)) - self.__selector.geometry().center().x(), 20)
        self.__selector.loadTypes(self.imageTypes)
        self.__selector.show()


app = QApplication(args.args)
_ventana = MainUi(args.ImageInput)
_ventana.show()
app.exec()
