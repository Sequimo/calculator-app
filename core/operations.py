# -----------------------Functions operation buttons------------------------

from core.input_processing import addtext

# Function to push the number or operation buttons to the label panel and clear the "Error" text if it is present
# -Number buttons and operations buttons functions

def pushButtonDefault(panel, text):
    if panel.text() == "Error":
        panel.setText("")
    addtext(panel, text)
    

        
# Fuction to parentesis operation     
def parentesisOperation(panel):
    texto = panel.text()

    abierto = texto.count("(")
    cerrado = texto.count(")")

    if abierto == cerrado:
        addtext(panel, "(")
    else:
        addtext(panel, ")")

            
# Function to porcentage operation
def porcentageOperation(panel):
    addtext(panel, "%")
    
    

# Function to calculate the result of the operation
def calculate(panel):
    try:
        varText = panel.text()
            
        for i in varText:
            if i == "%":
                varText = varText.replace("%", "/100*")
            elif i == "x":
                varText = varText.replace("x", "*")
            elif i == "÷":
                varText = varText.replace("÷", "/")
                    
        result = eval(varText)
        panel.setText(str(result))
            
    except:
        panel.setText("Error ")
        
        

# Function to delete the last character of the label panel  
def delete(panel):
    if panel.text() == "Error":
        panel.setText("")
    else: panel.setText(panel.text()[:-1])



# Function to clear the label panel
def clear(panel):
    panel.setText("")