class CalculatorLogic:
    """Core logic for the calculator which calculates math expressions
        """
    allowed_chars = "0123456789+-*/.()"
    
    def __init__(self):
        self.expression = "" # Initialize empty expression 


    def calculate(self):
        """Calculates the math expression. Returns the result or raises an error if the expression is invalid"""
        if not all(c in self.allowed_chars for c in self.expression):
            raise ValueError("Invaild characters in the expression")
        
        try:
            result = eval(self.expression) = str(result)
            return result
        except Exception:
            raise ValueError("Invalid math expression")
    
    
    def add(self, char):
        """Add a character to the expression"""
        self.expression += str(char)
    
    def backspace(self):
        """Remove the last character from the expression"""
        self.expression = self.expression[:-1]
    
    def clear(self):
        """Removes the entire expression from the calculator"""
        self.expression = ""
    