# --------------------------Functions label panel-------------------

# Delimiter to label panel
def delimiterSignalOperation(self):
        
    var = self.text()
        
    if not var:
        return
        
    if not var[0] in "1234567890": #The first character must be a number, if it is not, it will be deleted.
        self.blockSignals(True)
        self.setText(var[1:]) 
        self.blockSignals(False)
       
    if self.s == False and var[-1] in "+-x/.%÷": #Characters that cannot be repeated one after another, if they are repeated, the last one will be deleted.           
        self.s = True
    else: 
        if var[-1] in "1234567890()": #Characters that can be repeated.
            self.s = False
        else: 
            self.blockSignals(True)
            self.setText(var[:-1]) 
            self.blockSignals(False)



# Function to add text to the label panel
def addtext(panel, text):
    panel.setText(panel.text() + text)


