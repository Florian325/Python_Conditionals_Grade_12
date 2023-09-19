"""Task 3: Leap Year Checker"""

import sys

from PyQt6.QtWidgets import QApplication

from Abstract_Window import AbstractMainWindow


class Task3Window(AbstractMainWindow):
    def __init__(self):
        self.set_title("Leap Year Checker")
        self.set_input_label_title("Enter Year to check if it is a leap year")
        self.set_button_title("Check")
        self.set_error_message_var("Input value should be an integer")
        super().__init__()

    def calculate_result(self):
        try:
            # Checks if there is a remaining amount
            if self.integer_input % 4 == 0:
                leap = "is"
            else:
                leap = "is not"
            self.set_result(f"{self.integer_input} {leap} a leap year")
            self.show_result()
        except:
            self.show_error()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Task3Window()
    window.show()

    app.exec()
