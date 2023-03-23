from chadBot import chad_noob_bot
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie, QIcon, QPixmap, QFont
import sys
import threading
sys.path.append('../')
sys.path.append('./')


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.bot = chad_noob_bot()
        # Set window properties
        self.window_title = 'noobBot'
        self.setWindowTitle(self.window_title)
        self.setWindowIcon(QIcon('../assets/noobBot_window_icon.png'))
        self.set_taskbar_icon('../assets/noobBot_window_icon.png')
        self.setMinimumSize(380, 360)
        self.setMaximumSize(380, 360)

        # gif style properties
        self.gif_label = QLabel(self)
        self.gif_label.setAlignment(Qt.AlignmentFlag(5))

        # Start button for listening gif
        self.start_gif_button = QPushButton('Speak', self)
        self.start_gif_button.setFont(QFont('Montserrat', 10))
        self.start_gif_button.clicked.connect(self.play_gif)

        # Stop button for listening gif
        self.stop_gif_button = QPushButton('Stop', self)
        self.stop_gif_button.clicked.connect(self.stop_gif)
        self.stop_gif_button.setFont(QFont('Montserrat', 10))

        # print console output
        self.console_output_text = QLabel(self)

        # print Statement
        self.statement_text = QLabel(self)
        self.statement_text.setText("statement text")

        # Create a vertical layout and add the button and label to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.start_gif_button)
        layout.addWidget(self.stop_gif_button)
        layout.addWidget(self.gif_label)
        layout.addWidget(self.statement_text)
        layout.addWidget(self.console_output_text)

        # self.bot.wish_me()

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

        self.start_gif_button.setText("Listening")
        self.gif = QMovie('../assets/giphy.gif')
        self.gif.setSpeed(100)

        # Set the GIF animation to the label and start playing
        self.gif_label.setMovie(self.gif)
        self.gif.start()
        wish_thread = threading.Thread(target=self.bot.wish_me)
        wish_thread.start()

    def stop_gif(self):
        self.gif.stop()
        self.start_gif_button.setText("Speak")
        self.gif_label.clear()
        self.console_output_text.clear()

    def closeEvent(self):
        #     # Clean up the GIF animation when closing the app
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
