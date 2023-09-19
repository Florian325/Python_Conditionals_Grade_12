"""Task 6: Largest of Three Numbers"""

import sys

from PyQt6.QtWidgets import QApplication

from Abstract_Window import AbstractMainWindow


class Task6Window(AbstractMainWindow):
    def __init__(self):
        self.set_title("Largest of Three Numbers")
        self.set_input_label_title("Input 3 numbers seperated with a comma to check which is the largest one")
        self.set_button_title("Check")
        self.set_error_message_var("The 3 input values should be a number")
        super().__init__()

    def calculate_result(self):
        try:
            numbers = self.input.split(", ")

            # Validation
            if len(numbers) != 3:
                raise Exception

            largest_number = 0

            for _number in numbers:
                number = float(_number)
                # Checks if the current number is greater than the to know largest number
                if number > largest_number or numbers.index(_number) == 0:
                    # If it is grater or the first number current number get assigned to the largest_number
                    largest_number = number

            self.set_result(f"The largest number is {largest_number}")
            self.show_result()
        except:
            self.show_error()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Task6Window()
    window.show()

    app.exec()
