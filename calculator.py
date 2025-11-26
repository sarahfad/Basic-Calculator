import tkinter as tk
from tkinter import messagebox

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
            result = eval(self.expression) 
            self.expression = str(result)
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

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.logic = CalculatorLogic()
        self.create_display()
    
    def create_display(self):
        self.display_var = tk.StringVar()
        entry = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Segoe UI", 20),
            justify="right"
        )
        entry.grid(
            row=0, 
            column=0, 
            columnspan=4, 
            padx=5, 
            pady=5, 
            sticky="nsew"
            )
        
if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
