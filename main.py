import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        uic.loadUi('design.ui', self)
        self.pages.setCurrentWidget(self.main_page)
        self.back_button.clicked.connect(lambda: self.pages.setCurrentWidget(self.main_page))

    def on_choose_button_clicked(self):
        shape_name = self.shape_group.checkedButton().objectName().split('_')[0]
        self.pages.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main_page)
        )

    def on_circle_calculate_button_clicked(self):
        radius = self.circle_radius_input.value()
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius

        self.circle_area_display.display(area)
        self.circle_circumference_display.display(circumference)

    def on_triangle_calculate_button_clicked(self):
        a = self.triangle_side1_input.value()
        b = self.triangle_side2_input.value()
        c = self.triangle_side3_input.value()
        s = (a + b + c) / 2  # Semi perimeter

        try:
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        except Exception as e:
            print("Error: Invalid triangle, the sum of two side lengths has to exceed the length of the third side.", e)
            return
        perimeter = a + b + c

        self.triangle_area_display.display(area)
        self.triangle_perimeter_display.display(perimeter)

    def on_square_calculate_button_clicked(self):
        a = self.square_side_input.value()

        area = a ** 2
        perimeter = a * 4

        self.square_area_display.display(area)
        self.square_perimeter_display.display(perimeter)

    def on_trapezoid_calculate_button_clicked(self):
        a = self.trapezoid_side1_input.value()
        b = self.trapezoid_side2_input.value()
        c = self.trapezoid_side3_input.value()
        d = self.trapezoid_side4_input.value()
        height = self.trapezoid_height_input.value()

        area = (c + d) / 2 * height
        perimeter = a + b + c + d

        self.trapezoid_area_display.display(area)
        self.trapezoid_perimeter_display.display(perimeter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWidget()
    win.show()
    app.exec_()
