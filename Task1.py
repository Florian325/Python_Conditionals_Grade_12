"""Task 1: Odd or Even?"""

import sys

from PyQt6.QtWidgets import QApplication

from Abstract_Window import AbstractMainWindow


class Task1Window(AbstractMainWindow):
    def __init__(self):
        self.set_title("Odd or Even?")
        self.set_input_label_title("Input Number to check if it is even or odd")
        self.set_button_title("Check")
        super().__init__()

    def calculate_result(self):
        # If there is an error program will execute the except statement instead of crashing
        try:
            # Checks if there is a remaining amount
            if self.integer_input % 2 == 0:
                result = "even"
            else:
                result = "odd"
            self.set_result(f"The value: {self.integer_input} is {result}")
            self.show_result()

        except:
            self.show_error()


if __name__ == '__main__':
    # initialise App
    app = QApplication(sys.argv)

    # initialise Window
    window = Task1Window()
    window.show()

    # execute app
    app.exec()
