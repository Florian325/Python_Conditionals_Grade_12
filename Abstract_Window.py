"""Abstract base class for the main window"""
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QFont


class AbstractMainWindow(QMainWindow):
    """Handles base functionalities"""

    # private class variables
    _title: str = ""
    _error_message: str = "Input value should be an integer or a float"
    _button_title: str = ""
    _input_label_title: str = ""

    def __init__(self):
        # initialise super class
        super().__init__()
        self.setWindowTitle(self.title)

        # input section
        self._input_label = QLabel(self.input_label_title)
        self._input = QLineEdit()

        # button section
        button = QPushButton(self.button_title)
        button.clicked.connect(self.calculate_result)

        # result label section
        self._result_label = QLabel("")
        self._result_label.setFont(QFont("Arial", 15))
        self._result_label.hide()

        # error label section
        self._error_label = QLabel(self.error_message)
        self._error_label.setStyleSheet("color: red")
        self._error_label.hide()

        # initialise vertical layout
        self.layout = QVBoxLayout()

        # add elements to layout
        self.layout.addWidget(self._input_label)
        self.layout.addWidget(self._input)
        self.layout.addWidget(button)
        self.layout.addWidget(self._result_label)
        self.layout.addWidget(self._error_label)

        # initialise Widget
        self.widget = QWidget()
        # adds previous created layout to widget
        self.widget.setLayout(self.layout)

        # add widget to the main window
        self.setCentralWidget(self.widget)

    # Getter and Setter
    # Getter returns private variable as a variable (@property) and setter edits variables and ui elements
    @property
    def title(self) -> str:
        return self._title

    def set_title(self, value: str):
        self._title = value

    @property
    def error_message(self) -> str:
        return self._error_message

    def set_error_message_var(self, value: str):
        self._error_message = value

    def set_error_message(self, value: str):
        self._error_label.setText(value)

    @property
    def button_title(self) -> str:
        return self._button_title

    def set_button_title(self, value: str):
        self._button_title = value

    @property
    def input_label_title(self) -> str:
        return self._input_label_title

    def set_input_label_title(self, value: str):
        self._input_label_title = value

    @property
    def input(self) -> str:
        """Returns input as a string"""
        return self._input.text()

    @property
    def integer_input(self) -> int:
        """Returns input as an integer"""
        return int(self.input)

    @property
    def float_input(self) -> float:
        """Returns input as a float"""
        return float(self.input)

    def set_result(self, val: str):
        self._result_label.setText(val)

    # Visibility controls
    def show_result(self):
        self.hide_error()
        self._result_label.show()

    def hide_result(self):
        self._result_label.hide()

    def show_error(self):
        self._result_label.hide()
        self._error_label.show()

    def hide_error(self):
        self.hide_result()
        self._error_label.hide()

    def calculate_result(self):
        """Gets executed if button gets clicked"""
        pass
