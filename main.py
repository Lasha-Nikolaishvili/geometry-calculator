import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        uic.loadUi('design.ui', self)
        print(dir(self))
        self.pages.setCurrentWidget(self.main_page)
        self.choose_button.clicked.connect(self.select_shape)
        self.back_button.clicked.connect(lambda: self.pages.setCurrentWidget(self.main_page))

    def select_shape(self):
        shape_name = self.shape_group.checkedButton().objectName().split('_')[0]
        print(shape_name)
        self.pages.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main_page)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWidget()
    win.show()
    app.exec_()
