# --------------------layouts configuration------------------

# Importaciones
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout

# layout_buttons configuration

class layout_buttons(QGridLayout):   
    
    def __init__(self, limit_columns = 4):
        super().__init__()
        self.setSpacing(5)
        self.setContentsMargins(10, 0, 10, 10)
        self.limit_columns = limit_columns
    
    def organizeButtons(self, *buttons):
        row = 0
        col = 0
        for button in buttons:
            self.addWidget(button, row, col)
            col += 1
            if col >= self.limit_columns:
                col = 0
                row += 1
                


# layout_panel configuration    
        
class layout_panel(QGridLayout):

    def __init__(self, panel):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.addWidget(panel, 0, 0)
        
        
        
# parent_layout configuration
        
class parent_layout(QVBoxLayout):
    def __init__(self, *layouts):
        super().__init__()
        
        for layout in layouts:
            self.addLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)