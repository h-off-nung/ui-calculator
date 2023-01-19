# Import the necessary modules
from tkinter import *

# Create a new Tkinter window
root = Tk()
root.title("Calculator")
# root.geometry("550x400")

# Create a variable to store the user's input
equation = StringVar()

# Create a function to handle button clicks
def button_click(number):
    current = equation.get()
    equation.set(current + str(number))

def clear():
    equation.set("")

def equal():
    current = equation.get()
    equation.set(eval(current))

# Create the input field
entry = Entry(root, textvariable=equation)
entry.grid(row=0, column=0, columnspan=10, padx=100, pady=30)

# Create the button for each number
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create the button for each operator
button_add = Button(root, text="+", padx=30, pady=20, command=lambda: button_click("+"))
button_subtract = Button(root, text="-", padx=30, pady=20, command=lambda: button_click("-"))
button_multiply = Button(root, text="*", padx=30, pady=20, command=lambda: button_click("*"))
button_divide = Button(root, text="/", padx=30, pady=20, command=lambda: button_click("/"))
button_decimal = Button(root, text=".", padx=41, pady=20, command=lambda: button_click("."))
button_index = Button(root, text="Index", padx=29, pady=20, command=lambda: button_click("**"))

button_equal = Button(root, text="=", padx=30, pady=20, bg='green', command=equal)
button_clear = Button(root, text="Clear", padx=30, pady=20, bg='red', command=clear)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=0, column=3)
button_clear.grid(row=0, column=0)
button_decimal.grid(row=4, column=2)
button_index.grid(row=4, column=0)


root.mainloop()

#add button decimal
# Decimal= Button(gui, text='.', fg='black', bg='red',
#                     command=lambda: press('.'), height=1, width=7)