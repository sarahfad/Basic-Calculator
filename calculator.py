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
        self.just_calculated = False

        # Light pink window background
        self.configure(bg="#FFEFF5")

        self.create_display()
        self.create_buttons()
    
    def create_display(self):
        """Create the actual part where the expression is shown"""
        self.display_var = tk.StringVar()
        entry = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Segoe UI", 20),
            justify="right",
            bg="white",
            fg="#4A2C3A",
            bd=2
        )
        entry.grid(
            row=0, 
            column=0, 
            columnspan=4, 
            padx=5, 
            pady=5, 
            sticky="nsew"
            )
    
    def create_buttons(self):
        """Put the buttons on the GUI"""
       
        # Pink color calc
        btn_color = "#F6C7D9" 
        operator_color = "#E5A4C3"
        clear_color = "#FF9AB9"
        equals_color = "#FF6FAF"

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("←", 5, 0), ("=", 5, 1, 3),
        ]

        for button in buttons:
            if len(button) == 3:
                text, row, col = button
                colspan = 1
            else:
                text, row, col, colspan = button

            # Based on button type - change the colors
            if text in "+-*/":
                color = operator_color
            elif text == "C":
                color = clear_color
            elif text == "=":
                color = equals_color
            else:
                color = btn_color
            
            tk_button = tk.Button(
                self,
                text=text,
                font=("Segoe UI", 16),
                width=4,
                height=2,
                bg=color,
                fg="#4A2C3A",
                activebackground=color,
                relief="flat",
                command=lambda t=text: self.handle_buttons(t)
            )

            tk_button.grid(
                row=row,
                column=col,
                columnspan=colspan,
                padx=3,
                pady=3,
                sticky="nsew",
            )
        
    def handle_buttons(self, label):
        """Handle the button clicks"""
        if self.just_calculated and label not in ["=", "C", "←"]:
            self.logic.clear()
            self.display_var.set("")
            self.just_calculated = False
        if label == "C":
            self.logic.clear()
            self.display_var.set("")
            return
        elif label == "←":
            self.logic.backspace()
            self.display_var.set(self.logic.expression)
            return
        elif label == "=":
            try:
                result = self.logic.calculate()
                self.display_var.set(result)
                self.just_calculated = True
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self.logic.clear()
                self.display_var.set("")
            return
        else:
            self.logic.add(label)
            self.display_var.set(self.logic.expression)
            
if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
