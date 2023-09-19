"""Task 5: Triangle Type Checker"""

import sys

from PyQt6.QtWidgets import QApplication

from Abstract_Window import AbstractMainWindow


class Task5Window(AbstractMainWindow):
    def __init__(self):
        self.set_title("Triangle Type Checker")
        self.set_input_label_title("Input 3 angles of a triangle seperated with a comma to check the type of it")
        self.set_button_title("Check Type")
        self.set_error_message_var("The 3 input values should be a number and >= 0")
        super().__init__()

    def calculate_result(self):
        try:
            angle_sum = 0
            # Converting by commas seperated input to an array
            angle_array = self.input.split(", ")

            # Validation
            if len(angle_array) != 3:
                raise Exception
            for _angle in angle_array:
                angle = float(_angle)
                if angle < 0 or angle == 180:
                    raise Exception
                angle_sum += angle
            if angle_sum != 180:
                raise Exception

            # Assigning values to the variable via index
            a1 = float(angle_array[0])
            a2 = float(angle_array[1])
            a3 = float(angle_array[2])

            # Checking for matches
            matches = 0
            if a1 == a2:
                matches += 1
            if a1 == a3:
                matches += 1
            if a2 == a3:
                matches += 1

            if matches == 1:
                category = "Isosceles: At least two angles are equal"
            elif matches > 1:
                category = "Equilateral: All three angles are equal"
            else:
                category = "Scalene: No angles are equal"

            self.set_result(f"The category for the triangle is {category}")
            self.show_result()
        except:
            self.show_error()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Task5Window()
    window.show()

    app.exec()
