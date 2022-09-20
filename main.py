from tkinter import *

calculation = ""
root = Tk()
input_area = Entry(root, width=16, font=("Arieal", 40))
input_area.grid(row=0, column=0, columnspan=4, padx=15, pady=15)


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    input_area.delete(0, "end")
    input_area.insert(0, calculation)


def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        input_area.delete(0, "end")
        input_area.insert(0, calculation)

    except:
        input_area.delete(0, "end")
        input_area.insert(0, "Error")


def clear():
    global calculation
    calculation = ""
    input_area.delete(0, "end")


button_1 = Button(root, text="1", padx=50, pady=25, command=lambda: add_to_calculation(1))
button_2 = Button(root, text="2", padx=50, pady=25, command=lambda: add_to_calculation(2))
button_3 = Button(root, text="3", padx=50, pady=25, command=lambda: add_to_calculation(3))
button_4 = Button(root, text="4", padx=50, pady=25, command=lambda: add_to_calculation(4))
button_5 = Button(root, text="5", padx=50, pady=25, command=lambda: add_to_calculation(5))
button_6 = Button(root, text="6", padx=50, pady=25, command=lambda: add_to_calculation(6))
button_7 = Button(root, text="7", padx=50, pady=25, command=lambda: add_to_calculation(7))
button_8 = Button(root, text="8", padx=50, pady=25, command=lambda: add_to_calculation(8))
button_9 = Button(root, text="9", padx=50, pady=25, command=lambda: add_to_calculation(9))
button_0 = Button(root, text="0", padx=50, pady=25, command=lambda: add_to_calculation(0))
button_add = Button(root, text="+", padx=50, pady=25, command=lambda: add_to_calculation('+'))
button_sub = Button(root, text="-", padx=50, pady=25, command=lambda: add_to_calculation('-'))
button_mul = Button(root, text="*", padx=50, pady=25, command=lambda: add_to_calculation('*'))
button_div = Button(root, text="/", padx=50, pady=25, command=lambda: add_to_calculation('/'))
button_clear = Button(root, text="AC", padx=50, pady=25, command=clear)
button_equal = Button(root, text="=", padx=50, pady=25, command=evaluate)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_div.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal.grid(row=4, column=3)


root.mainloop()