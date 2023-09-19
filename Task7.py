"""Task 7: Positive or Negative?"""

import sys

from PyQt6.QtWidgets import QApplication

from Abstract_Window import AbstractMainWindow


class Task7Window(AbstractMainWindow):
    def __init__(self):
        self.set_title("Positive or Negative?")
        self.set_input_label_title("Check if the number is positive, negative or zero")
        self.set_button_title("Check")
        self.set_error_message_var("The input value should be a number")
        super().__init__()

    def calculate_result(self):
        try:
            if self.float_input > 0:
                result = "positive"
            elif self.float_input < 0:
                result = "negative"
            else:
                result = "zero"

            self.set_result(f"The number is {result}")
            self.show_result()
        except:
            self.show_error()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Task7Window()
    window.show()

    app.exec()
