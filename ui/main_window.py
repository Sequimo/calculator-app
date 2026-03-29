#--------------------Window configuration------------------

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("assets\icono_calculator.jpeg"))
        self.setWindowTitle("Calculadora")
        self.setFixedSize(405, 690)
        self.setStyleSheet("background-color: #1C1C1C;")