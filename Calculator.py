# This script demonstrates a simple calculator with basic arithmetic operations

import tkinter as tk

def calculate():
    """Perform the calculation based on user input."""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Error: Division by zero!"
            else:
                result = num1 / num2
        else:
            result = "Invalid operator!"

        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Python GUI Calculator")
window.configure(bg="#ffc0cb")  # Set window background to pink

# Set a pinkish style for all widgets
label_style = {"bg": "#ffc0cb", "fg": "#d6336c", "font": ("Arial", 12, "bold")}
entry_style = {"bg": "#fff0f5", "fg": "#d6336c", "font": ("Arial", 12)}
button_style = {"bg": "#ff69b4", "fg": "white", "activebackground": "#ffb6c1", "font": ("Arial", 12, "bold")}

# Create and pack the widgets
tk.Label(window, text="First Number:", **label_style).pack()
entry_num1 = tk.Entry(window, **entry_style)
entry_num1.pack()

tk.Label(window, text="Operator (+, -, *, /):", **label_style).pack()
operator_var = tk.StringVar(value="+")
operator_menu = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_menu.config(bg="#ffb6c1", fg="#d6336c", font=("Arial", 12, "bold"), activebackground="#ffc0cb")
operator_menu["menu"].config(bg="#fff0f5", fg="#d6336c", font=("Arial", 12))
operator_menu.pack()

tk.Label(window, text="Second Number:", **label_style).pack()
entry_num2 = tk.Entry(window, **entry_style)
entry_num2.pack()

# Calculate button
btn_calculate = tk.Button(window, text="Calculate", command=calculate, **button_style)
btn_calculate.pack()

# Result display
label_result = tk.Label(window, text="Result: ", **label_style)
label_result.pack()

window.mainloop()