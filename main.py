from PyQt5.QtWidgets import QWindow, QGroupBox, Qapplication, QGridLayout, QLabel, QPushButton, QSlider, QSpacerItem, QListWidget, QMessageBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon

import os
import sys

class Window(QWindow):
    pass


if __name__ == '__main__':
    app = Qapplication(sys.argv)
    window = Window()
    window.show()
