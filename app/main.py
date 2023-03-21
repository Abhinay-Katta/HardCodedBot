from chadBot import chad_noob_bot
from PyQt6 import QtCore

from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie, QIcon, QPixmap, QFont
import sys
sys.path.append('../')
sys.path.append('./')


class App(QWidget):

    def __init__(self):
        super().__init__()
        bot = chad_noob_bot()

        # Set window properties
        self.setWindowTitle('noobBot')
        self.setWindowIcon(QIcon('../src/noobBot_window_icon.png'))
        self.set_taskbar_icon('../src/noobBot_window_icon.png')
        self.setMinimumSize(340, 300)
        self.setMaximumSize(360, 320)
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(QtCore.Qt.AlignmentFlag(5))
        # Create a button to trigger the animation
        self.button = QPushButton('Speak', self)
        self.button.setFont(QFont('Berlin Sans FB', 13))
        self.button.clicked.connect(self.play_gif)

        # self.button.clicked.connect(bot.take_command)
        # print console output
        self.console_output_text = QLabel(self)
        self.console_output_text.setText("console output text")
        self.console_output_text.setAlignment(QtCore.Qt.AlignmentFlag(10))
        # # self.console_output_text_button

        # # print Statement
        self.statement_text = QLabel(self)
        self.statement_text.setText("statement text")

        # Create a vertical layout and add the button and label to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.gif_label)
        layout.addWidget(self.statement_text)
        layout.addWidget(self.console_output_text)

        # bot.wish_me()

    def update_text(self):
        self.textbox

    def set_taskbar_icon(self, icon_path):
        # Load the icon from file
        icon = QIcon(QPixmap(icon_path))

        # Set the icon for the taskbar
        try:
            if sys.platform == 'win32':
                import ctypes
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                    'myappid')
                self.setWindowIcon(icon)
        except:
            pass

        # Create a label to display the GIF animation

    def play_gif(self):
        # Load the GIF animation from file
        self.button.setText("Listening")
        gif = QMovie('D:\Projects\python\HardCodedBot\src\giphy.gif')

        gif.setSpeed(100)

        # Set the GIF animation to the label and start playing
        self.gif_label.setMovie(gif)
        gif.start()

    def closeEvent(self, event):
        # Clean up the GIF animation when closing the app
        try:
            self.gif_label.movie().stop()
            self.gif_label.clear()
        except:
            self.gif_label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
