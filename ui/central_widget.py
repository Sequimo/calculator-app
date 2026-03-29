from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
from core.input_processing import addtext
from core.operations import parentesisOperation, porcentageOperation, calculate, delete, clear

class MainWindow(QWidget):
    def __init__(self, layout, label_panel):
        super().__init__()
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.label_panel = label_panel
        
    #-Keyboard functions
    
    def write(self, text):
        addtext(self.label_panel, text)

    def keyPressEvent(self, event: QKeyEvent):
        
        key_map = {
                    Qt.Key.Key_Slash: "÷",
                    Qt.Key.Key_Asterisk: "x",
                    Qt.Key.Key_Plus: "+",
                    Qt.Key.Key_Minus: "-",
                    Qt.Key.Key_Period: ".",
                }   

        key = event.key()
        if key in (Qt.Key.Key_0, Qt.Key.Key_1, Qt.Key.Key_2, 
                   Qt.Key.Key_3, Qt.Key.Key_4, Qt.Key.Key_5, 
                   Qt.Key.Key_6, Qt.Key.Key_7, Qt.Key.Key_8, Qt.Key.Key_9):
            self.write(event.text())
            
        elif key in key_map:
            self.write(key_map[key])
        
        elif key == Qt.Key.Key_Backspace:
            delete(self.label_panel)
        elif key == Qt.Key.Key_Return or key == Qt.Key.Key_Enter:
            calculate(self.label_panel)
        elif key == Qt.Key.Key_Percent:
            porcentageOperation(self.label_panel)
        elif key == Qt.Key.Key_ParenLeft or key == Qt.Key.Key_ParenRight:
            parentesisOperation(self.label_panel)
        elif key == Qt.Key.Key_C:
            clear(self.label_panel)