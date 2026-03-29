#--------------------label_Panel configuration------------------   

from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtGui import QFont, QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression
from core.input_processing import delimiterSignalOperation

font_panel = QFont("Arial", 50, QFont.Weight.Bold)    
            
class CalculatorDisplay(QLineEdit):
    def __init__(self, text = ""):
        super().__init__()
        self.setText(text)
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: #1C1C1C; border: none; color: #FFFFFF;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setFont(font_panel)
        self.setMaxLength(12)
        self.s = False
        self.textChanged.connect(lambda: delimiterSignalOperation(self))
        
        regulator = QRegularExpression(r"^[0-9+()%-*/.]+$")
        validator = QRegularExpressionValidator(regulator)
        self.setValidator(validator)
        
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)