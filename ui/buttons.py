# ----------------------------Buttons configuration----------------------------

# importataciones
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from core.operations import pushButtonDefault, parentesisOperation, porcentageOperation, calculate, delete, clear

# Variables
font_button = QFont("Arial", 30, QFont.Weight.Bold, Qt.AlignmentFlag.AlignCenter) 
font_ops = QFont("Arial", 30, QFont.Weight.Bold)     

class NumberButton(QPushButton):
    def __init__(self, text, label_panel_instance):
        super().__init__(text)  
        self.label_panel = label_panel_instance
        
        self.setFont(font_button)
        self.setFixedSize(90, 90)
        self.setStyleSheet("background-color: #363636; border: 1px solid #1C1C1C; border-radius: 45px; color: #FFFFFF;")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clicked.connect(lambda: pushButtonDefault(self.label_panel, self.text()))   
        


class OperationButton(NumberButton):
    def __init__(self, text, label_panel_instance):
        super().__init__(text, label_panel_instance)

        self.setStyleSheet("background-color: #FF9500; border: 1px solid #1C1C1C; border-radius: 45px; color: #FFFFFF;")
        self.setFont(font_ops)
        self.clicked.disconnect()
        
        if text == "⌫":    
            self.clicked.connect(lambda: delete(self.label_panel))
        elif text == "=":
            self.clicked.connect(lambda: calculate(self.label_panel))
        elif text == "C":
            self.clicked.connect(lambda: clear(self.label_panel))
        elif text == "%":
            self.clicked.connect(lambda: porcentageOperation(self.label_panel))
        elif text == "()":
            self.clicked.connect(lambda: parentesisOperation(self.label_panel))
        else:
            self.clicked.connect(lambda: pushButtonDefault(self.label_panel, self.text()))
        