from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QCheckBox, QWidget, QPushButton
from plate import Plate

import App
import IMG

_ = Plate(locale="es_CO")


class ImageTypeSel(QLabel):

    def __init__(self, parent):
        super(ImageTypeSel, self).__init__(parent)

        self.resize(self.parent().size())

        self.__center = QLabel(self)

        self.__square = SelectorWithImage(self.__center, App.ImageTypes.Squared)

        self.__round = SelectorWithImage(self.__center, App.ImageTypes.Rounded)
        self.__round.move(self.__square.geometry().topRight())

        self.__port = SelectorWithImage(self.__center, App.ImageTypes.Portrait)
        self.__port.move(self.__round.geometry().topRight())

        self.__land = SelectorWithImage(self.__center, App.ImageTypes.Landscape)
        self.__land.move(self.__port.geometry().topRight())

        self.accept = QPushButton(self.__center)
        self.accept.setText("Siguiente ->")
        self.accept.adjustSize()
        self.accept.move(self.__land.geometry().right() - self.accept.width() - 10,
                         self.__land.geometry().bottom())
        self.accept.setDisabled(True)

        self.__center.resize(self.childMaxSize(self.__center))

        self.__checkBoxes(self.__center)
        self.__loadCheckBoxes(self.__center)

        self.__center.move(self.geometry().center() - self.__center.geometry().center())
        self.__center.setObjectName("myParentWidget")
        self.__center.setStyleSheet("QWidget#myParentWidget {border: 1px groove gray;}")


    def childMaxSize(self, parent: QWidget):

        childs = parent.children()

        x = 0
        y = 0

        for i in range(len(childs)):

            if childs[i].geometry().bottom() > y:
                y = childs[i].geometry().bottom()
            if childs[i].geometry().right() > x:
                x = childs[i].geometry().right()

        return QSize(x, y + 10)

    def __checkBoxes(self, parent: QWidget):

        childs = parent.children()

        checked = list()

        for i in childs:
            if i.__class__.__name__ == "SelectorWithImage":
                if i.check.isChecked(): checked.append(i.imageType)

        return checked

    def __loadCheckBoxes(self, parent: QWidget):

        childs = parent.children()

        for i in childs:
            if i.__class__.__name__ == "SelectorWithImage":
                i.check.clicked.connect(lambda: self.__nexButtonStat())

    def __nexButtonStat(self):
        btt = self.__checkBoxes(self.__center)
        self.accept.setEnabled(True) if len(btt) > 0 else self.accept.setDisabled(True)

    def getTypes(self, close=False):
        if close:
            self.hide()
            self.destroy()
        return self.__checkBoxes(self.__center)


class SelectorWithImage(QLabel):

    def __init__(self, parent, imageType: App.ImageTypes):
        super(SelectorWithImage, self).__init__(parent)

        self.check = QCheckBox(self)
        self.check.adjustSize()
        self.__text = QLabel(self)
        self.__imageType = imageType
        self.__text.setText(_(self.__imageType.name))
        self.__text.setContentsMargins(10, -10, 10, 10)
        self.__text.adjustSize()
        self.__text.move(self.check.geometry().bottomLeft().x(), 33)
        self.check.move(self.__text.geometry().center().x() - self.check.geometry().center().x(), 15)
        self.__img = QLabel(self)
        self.__img.move(self.__text.geometry().bottomLeft())
        image = QPixmap(IMG.Images[imageType])
        self.__img.setPixmap(image.scaledToWidth(self.__text.geometry().bottomRight().x() - 20))
        self.__img.setContentsMargins(10, 0, 10, 10)
        self.__img.adjustSize()
        self.resize(self.__text.geometry().bottomRight().x(), self.__img.geometry().bottomRight().y())

    @property
    def imageType(self):
        return self.__imageType
