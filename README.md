# basic-calculator

A simple, pastel-themed calculator built with Python and Tkinter.  
This project was created as a course assignment to demonstrate GUI development and object-oriented programming pythonic principles.

---

## Features

- Graphical user interface using Tkinter  
- Supports basic arithmetic operations:  
  - Addition  
  - Subtraction  
  - Multiplication  
  - Division  
- Decimal input  
- Backspace functionality  
- Clear button  
- Basic error handling for invalid expressions  
- Organized using separate logic and UI classes  

---

## Project Structure

The project contains two main components:

### CalculatorLogic
Handles the internal functionality of the calculator:
- Stores and updates the math expression
- Ensures only valid characters are accepted
- Evaluates the expression using Python's `eval()` function
- Clears or deletes characters from the expression

### CalculatorApp
- Inherits from `tk.Tk`
- Creates and arranges all buttons and the display entry field
- Applies simple color styling for a light pink theme
- Connects UI button actions to the logic class
- Updates the display based on user interactions

Separating the logic from the interface improves readability and maintainability.

---

## Styling

The calculator uses a color scheme to create a soft pink appearance.  
Examples of the style values used:

```python
self.configure(bg="#FFEFF5")

btn_color = "#F6C7D9"
operator_color = "#E5A4C3"
clear_color = "#FF9AB9"
equals_color = "#FF6FAF"
```

These values are applied directly to the Tkinter Buttons and Entry widgets.

---

## Running the program

### Requirements

- Python 3.x
- Tkinter (included with most python installations)

### Instructions

Run the calculator with:
```bash
  python calculator.py
```

A window will appear where you can interact with the calculator.

---

## Example Usage

- Click number and operator buttons to build an expression  
- Use the decimal point as needed  
- Use the backspace button to remove the last character  
- Use the Clear button to reset the expression  
- Press `=` to evaluate the current expression  

---

## Learning Resources for Tkinter

The following sources were used to learn Tkinter during development:

- Python Official Documentation (Tkinter)  
  https://docs.python.org/3/library/tkinter.html  

- TkDocs Tutorial  
  https://tkdocs.com/tutorial/  

- Real Python: Tkinter Guide  
  https://realpython.com/python-gui-tkinter/  

---

## Author

Sarah Fadenrecht  
University of Colorado Colorado Springs  

---

## Course Notes

This project demonstrates:

- Basic GUI programming in Python  
- Object-oriented design  
- Inheritance (CalculatorApp inherits from `tk.Tk`)  
- Event-driven programming  
- Simple widget styling  
- Error handling for user input  


