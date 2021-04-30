import os
import calculator_two
import calculator
from tkinter import *

root = Tk()
root.title('App Chooser')


def calculator():
    os.system('calculator.py')


def calculator_2():
    os.system('calculator_two.py')


# Makes the buttons
calculator = Button(root, text="calculator", height=3, width=14, bg="black", fg="white", command=calculator)
calculator_2 = Button(root, text="calculator 2", height=3, width=11, bg="black", fg="white", command=calculator_2)

# Places the buttons
calculator.grid(row=0, column=1, pady=0, padx=0)
calculator_2.grid(row=0, column=2, pady=0, padx=0)


root.mainloop()
