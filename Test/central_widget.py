from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6 import QtCore

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Add a button and a label to the central widget
        button = QPushButton('Click me', central_widget)
        label = QLabel('Hello, world!', central_widget)

        # centering the label:
        label.setAlignment(QtCore.Qt.AlignmentFlag(5))

        layout = QVBoxLayout(central_widget)
        layout.addWidget(button)
        layout.addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
