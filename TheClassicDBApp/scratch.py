from tkinter import *

root = Tk()  # the root widget

# define the widget (here, label named my_label), create it
# my_label = Label(root, text="Hey Pragya!")
# my_label_grid = Label(root, text="Hey Pragya. It's grid!")
# put it up on screen
# my_label.pack()
# tkinter grid system
# my_label_grid.grid(row=0, column=0)
# my_label.grid(row=1, column=1)
input_field = Entry(root, width=50)
input_field.pack()
input_field.insert(0, "Enter your name")

# creating buttons
def my_click():
    my_label = Label(root, text="Hey! what's up, " + input_field.get() + "?!?")
    my_label.pack()


button_one = Button(root, text="Feed your name", padx=50, pady=9, command=my_click, fg="white", bg="black")
button_one.pack()
root.mainloop()
