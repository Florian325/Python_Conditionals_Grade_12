"""Task 4: Age Classifier"""

import sys

from PyQt6.QtWidgets import QApplication

from Abstract_Window import AbstractMainWindow


class Task4Window(AbstractMainWindow):
    def __init__(self):
        self.set_title("Age Classifier")
        self.set_input_label_title("Qualifies age into categories")
        self.set_button_title("Check")
        self.set_error_message_var("Input value should be an integer and >= 0")
        super().__init__()

    def calculate_result(self):
        try:
            # Validation
            if self.integer_input < 0:
                raise Exception

            if self.integer_input <= 2:
                category = "Infant"
            elif self.integer_input <= 5:
                category = "Toddler"
            elif self.integer_input <= 12:
                category = "Child"
            elif self.integer_input <= 19:
                category = "Teenager"
            else:
                category = "Adult"
            self.set_result(f"The category for the age {self.integer_input} is {category}")
            self.show_result()
        except:
            self.show_error()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Task4Window()
    window.show()

    app.exec()
