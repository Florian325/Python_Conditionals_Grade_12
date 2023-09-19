"""Task 2: Grade Calculator"""

import sys

from PyQt6.QtWidgets import QApplication

from Abstract_Window import AbstractMainWindow


class Task2Window(AbstractMainWindow):
    def __init__(self):
        self.set_title("Grade Calculator?")
        self.set_input_label_title("Input percentage of right answers")
        self.set_button_title("Calculate Grade")
        self.set_error_message_var("Input value should be an integers or a float and between 0 and 100")
        super().__init__()

    def calculate_result(self):
        try:
            # Validation
            if self.float_input < 0 or self.float_input > 100:
                raise Exception

            if self.float_input < 60:
                result = "F"
            elif self.float_input < 70:
                result = "D"
            elif self.float_input < 80:
                result = "C"
            elif self.float_input < 90:
                result = "B"
            else:
                result = "A"
            self.set_result(f"The Grade is {result}")
            self.show_result()

        except:
            self.show_error()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Task2Window()
    window.show()

    app.exec()
