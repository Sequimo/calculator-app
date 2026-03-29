from PyQt6.QtWidgets import QApplication
import sys
from ui.main_window import MyWindow
from ui.central_widget import MainWindow
from ui.display import CalculatorDisplay
from ui.buttons import NumberButton, OperationButton
from ui.layouts import layout_buttons, layout_panel, parent_layout


app = QApplication(sys.argv)

# --------------------Window configuration------------------

window = MyWindow()

# --------------------Widget configuration------------------


#-Panel configuration

panel = CalculatorDisplay()

#-Buttons nums configuration

b7 = NumberButton("7", panel)
b8 = NumberButton("8", panel)
b9 = NumberButton("9", panel)
b4 = NumberButton("4", panel)
b5 = NumberButton("5", panel)
b6 = NumberButton("6", panel)
b1 = NumberButton("1", panel)
b2 = NumberButton("2", panel)
b3 = NumberButton("3", panel)
b0 = NumberButton("0", panel)

#-Buttons operations configuration

suma = OperationButton("+", panel)
resta = OperationButton("-", panel)
multiplicacion = OperationButton("x", panel)
division = OperationButton("÷", panel)
igual = OperationButton("=", panel)
delete = OperationButton("⌫", panel)
clear = OperationButton("C", panel)
parentesis = OperationButton("()", panel)
porcentaje = OperationButton("%", panel)
punto = OperationButton(".", panel)

#-Layout configuration

layoutPanel = layout_panel(panel)#Panel layout 

layoutButtons = layout_buttons()#Buttons layout
layoutButtons.organizeButtons(clear, delete, division, multiplicacion,
                              b7, b8, b9, resta,
                              b4, b5, b6, suma,
                              b1, b2, b3, punto,
                              porcentaje, parentesis, b0, igual)

parent_layout = parent_layout(layoutPanel, layoutButtons)#Parent layout

center_widget = MainWindow(parent_layout, panel)#Parent layout
window.setCentralWidget(center_widget)

window.show()
app.exec() 

