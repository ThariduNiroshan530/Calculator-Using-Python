import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_sqrt():
    try:
        expression = entry.get()
        result = math.sqrt(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_sin():
    try:
        expression = entry.get()
        result = math.sin(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_cos():
    try:
        expression = entry.get()
        result = math.cos(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_tan():
    try:
        expression = entry.get()
        result = math.tan(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Advanced Calculator")

# Create the entry field
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
buttons = [
    ("1", 1), ("2", 2), ("3", 3),
    ("4", 4), ("5", 5), ("6", 6),
    ("7", 7), ("8", 8), ("9", 9),
    ("0", 0)
]

row = 1
col = 0
for button_text, button_value in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=10,
                       command=lambda value=button_value: button_click(value))
    button.grid(row=row, column=col)
    col += 1
    if col == 3:
        col = 0
        row += 1

# Create the operator buttons
operators = [
    ("+", "+"), ("-", "-"), ("*", "*"),
    ("/", "/"), ("^", "**"), ("sqrt", "sqrt"),
    ("sin", "sin"), ("cos", "cos"), ("tan", "tan")
]

row = 1
col = 3
for button_text, operator in operators:
    button = tk.Button(window, text=button_text, padx=20, pady=10,
                       command=lambda op=operator: button_click(op))
    button.grid(row=row, column=col)
    row += 1

# Create the clear and equal buttons
button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)
button_clear.grid(row=0, column=3)

button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
button_equal.grid(row=row, column=col)

# Run the main loop
window.mainloop()
