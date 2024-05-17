import tkinter as tk
from tkinter import messagebox


def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        messagebox.showerror("Error", "You can not division by zero bro")
        return None


def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operator.get()

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = substract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        messagebox.showerror("Error", "Invalid Operation")
        return

    result_label.config(text=f"Result: {result}")


root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First Number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operation:").grid(row=2, column=0)
operator = tk.StringVar()
operator.set("+")  # Default value
tk.OptionMenu(root, operator, "+", "-", "*", "/").grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2)

root.mainloop()
