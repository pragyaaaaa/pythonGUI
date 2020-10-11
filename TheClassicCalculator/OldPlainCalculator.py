from tkinter import *
from tkinter.ttk import Style
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

root = ThemedTk(theme="breeze")
s = Style()
root.title("Old Plain Calculator")
input_field = Entry(root, width=40, borderwidth=2, bg='#daecff')
input_field.grid(row=0, column=0, columnspan=3)


def key_pressed_nums(num):
    current_val = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current_val) + str(num))
    return


def key_pressed_clear():
    input_field.delete(0, END)
    return


def key_pressed_add():
    global first_num
    global operation
    operation = "add"
    first_num = int(input_field.get())
    input_field.delete(0, END)
    return


def key_pressed_sub():
    global first_num
    global operation
    operation = "sub"
    first_num = int(input_field.get())
    input_field.delete(0, END)
    return


def key_pressed_mul():
    global first_num
    global operation
    operation = "mul"
    first_num = int(input_field.get())
    input_field.delete(0, END)
    return


def key_pressed_div():
    global first_num
    global operation
    operation = "div"
    first_num = int(input_field.get())
    input_field.delete(0, END)
    return


def key_pressed_equal():
    second_num = int(input_field.get())
    input_field.delete(0, END)
    if operation == "add":
        input_field.insert(0, first_num + second_num)
    elif operation == "sub":
        input_field.insert(0, first_num - second_num)
    elif operation == "mul":
        input_field.insert(0, first_num * second_num)
    else:
        input_field.insert(0, first_num / second_num)
    return


key_1 = ttk.Button(root, text="1", command=lambda: key_pressed_nums(1))
key_2 = ttk.Button(root, text="2", command=lambda: key_pressed_nums(2))
key_3 = ttk.Button(root, text="3", command=lambda: key_pressed_nums(3))
key_4 = ttk.Button(root, text="4", command=lambda: key_pressed_nums(4))
key_5 = ttk.Button(root, text="5", command=lambda: key_pressed_nums(5))
key_6 = ttk.Button(root, text="6", command=lambda: key_pressed_nums(6))
key_7 = ttk.Button(root, text="7", command=lambda: key_pressed_nums(7))
key_8 = ttk.Button(root, text="8", command=lambda: key_pressed_nums(8))
key_9 = ttk.Button(root, text="9", command=lambda: key_pressed_nums(9))
key_0 = ttk.Button(root, text="0", command=lambda: key_pressed_nums(0))
key_add = ttk.Button(root, text="+", command=lambda: key_pressed_add())
key_sub = ttk.Button(root, text="-", command=lambda: key_pressed_sub())
key_mul = ttk.Button(root, text="x", command=lambda: key_pressed_mul())
key_div = ttk.Button(root, text="/", command=lambda: key_pressed_div())
key_equal = ttk.Button(root, text="=", command=key_pressed_equal)
key_clear = ttk.Button(root, text="Clear", command=key_pressed_clear)
# placing buttons on screen
key_1.grid(row=3, column=0)
key_2.grid(row=3, column=1)
key_3.grid(row=3, column=2)

key_4.grid(row=2, column=0)
key_5.grid(row=2, column=1)
key_6.grid(row=2, column=2)

key_7.grid(row=1, column=0)
key_8.grid(row=1, column=1)
key_9.grid(row=1, column=2)

key_0.grid(row=4, column=0)
key_clear.grid(row=5, column=1)
key_equal.grid(row=5, column=2)
key_add.grid(row=5, column=0)
key_sub.grid(row=4, column=1)
key_mul.grid(row=4, column=2)
key_div.grid(row=4, column=0)
root.mainloop()
