from tkinter import *

root = Tk()
root.title("Old Plain Calculator")
input_field = Entry(root, width=50, borderwidth=7)
input_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


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


key_1 = Button(root, text="1", padx=40, pady=20, command=lambda: key_pressed_nums(1))
key_2 = Button(root, text="2", padx=40, pady=20, command=lambda: key_pressed_nums(2))
key_3 = Button(root, text="3", padx=40, pady=20, command=lambda: key_pressed_nums(3))
key_4 = Button(root, text="4", padx=40, pady=20, command=lambda: key_pressed_nums(4))
key_5 = Button(root, text="5", padx=40, pady=20, command=lambda: key_pressed_nums(5))
key_6 = Button(root, text="6", padx=40, pady=20, command=lambda: key_pressed_nums(6))
key_7 = Button(root, text="7", padx=40, pady=20, command=lambda: key_pressed_nums(7))
key_8 = Button(root, text="8", padx=40, pady=20, command=lambda: key_pressed_nums(8))
key_9 = Button(root, text="9", padx=40, pady=20, command=lambda: key_pressed_nums(9))
key_0 = Button(root, text="0", padx=40, pady=20, command=lambda: key_pressed_nums(0))
key_add = Button(root, text="+", padx=39, pady=20, command=lambda: key_pressed_add())
key_sub = Button(root, text="-", padx=41, pady=20, command=lambda: key_pressed_sub())
key_mul = Button(root, text="x", padx=40, pady=20, command=lambda: key_pressed_mul())
key_div = Button(root, text="/", padx=40, pady=20, command=lambda: key_pressed_div())
key_equal = Button(root, text="=", padx=40, pady=20, command=key_pressed_equal)
key_clear = Button(root, text="Clear", padx=30, pady=20, command=key_pressed_clear)
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
