from _ast import Lambda
from tkinter import *

root = Tk()
root.title('calculator')

#  Takes input
entry = Entry(root, width=45, borderwidth=3)
entry.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def button_click_1():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(1))
def button_click_2():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(2))
def button_click_3():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(3))
def button_click_4():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(4))
def button_click_5():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(5))
def button_click_6():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(6))
def button_click_7():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(7))
def button_click_8():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(8))
def button_click_9():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(9))
def button_click_0():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(0))
def button_click_add():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)
def button_click_equal():
    second_number = entry.get()
    entry.delete(0, END)
    entry.insert(0, int(f_num) + int(second_number))
def button_click_clear():
    entry.delete(0, END)
def button_click_subtract():
    entry.delete(0, END)
def button_click_multiply():
    entry.delete(0, END)
def button_click_divide():
    entry.delete(0, END)


# Makes the button
button_1 = Button(root, text="1", height=3, width=11, bg="black", fg="white", command=button_click_1)
button_2 = Button(root, text="2", height=3, width=14, bg="black", fg="white", command=button_click_2)
button_3 = Button(root, text="3", height=3, width=11, bg="black", fg="white", command=button_click_3)

button_4 = Button(root, text="4", height=3, width=11, bg="black", fg="white", command=button_click_4)
button_5 = Button(root, text="5", height=3, width=14, bg="black", fg="white", command=button_click_5)
button_6 = Button(root, text="6", height=3, width=11, bg="black", fg="white", command=button_click_6)

button_7 = Button(root, text="7", height=3, width=11, bg="black", fg="white", command=button_click_7)
button_8 = Button(root, text="8", height=3, width=14, bg="black", fg="white", command=button_click_8)
button_9 = Button(root, text="9", height=3, width=11, bg="black", fg="white", command=button_click_9)

button_0 = Button(root, text="0", height=3, width=11, bg="black", fg="white", command=button_click_0)
button_add = Button(root, text="+", height=3, width=14, bg="black", fg="white", command=button_click_add)
button_subtract = Button(root, text="-", height=3, width=11, bg="black", fg="white", command=button_click_subtract)

button_multipy = Button(root, text="x", height=3, width=11, bg="black", fg="white", command=button_click_multiply)
button_divide = Button(root, text="÷", height=3, width=14, bg="black", fg="white", command=button_click_divide)
button_equal = Button(root, text="=", height=3, width=11, bg="black", fg="white", command=button_click_equal)

button_clear = Button(root, text="clear", height=3, width=39, bg="black", fg="white", command=button_click_clear)

# Places the button on the screen
button_1.grid(row=3, column=0, pady=0, padx=0)
button_2.grid(row=3, column=1, pady=0, padx=0)
button_3.grid(row=3, column=2, pady=0, padx=0)

button_4.grid(row=2, column=0, pady=0, padx=0)
button_5.grid(row=2, column=1, pady=0, padx=0)
button_6.grid(row=2, column=2, pady=0, padx=0)

button_7.grid(row=1, column=0, pady=0, padx=0)
button_8.grid(row=1, column=1, pady=0, padx=0)
button_9.grid(row=1, column=2, pady=0, padx=0)

button_0.grid(row=4, column=0, pady=0)
button_add.grid(row=4, column=1, pady=0)
button_subtract.grid(row=4, column=2, pady=0)

button_multipy.grid(row=5, column=0, pady=0)
button_divide.grid(row=5, column=1, pady=0)
button_equal.grid(row=5, column=2, pady=0)

button_clear.grid(row=6, column=0, pady=0, padx=0, columnspan=3)

root.mainloop()
