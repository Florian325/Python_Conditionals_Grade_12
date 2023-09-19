"""Runs all tasks at the same time"""

# imports
import sys

from PyQt6.QtWidgets import QApplication

from Tasks import Task1Window, Task2Window, Task3Window, Task4Window, Task5Window, Task6Window, Task7Window

if __name__ == '__main__':
    # initialise app
    app = QApplication(sys.argv)

    # initialise windows
    w1 = Task1Window()
    w1.show()

    w2 = Task2Window()
    w2.show()

    w3 = Task3Window()
    w3.show()

    w4 = Task4Window()
    w4.show()

    w5 = Task5Window()
    w5.show()

    w6 = Task6Window()
    w6.show()

    w7 = Task7Window()
    w7.show()

    # execute application
    app.exec()
