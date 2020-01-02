import tkinter as tk
root = tk.Tk()
top_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM)
top_frame.pack(side=tk.TOP)
lab = tk.Label(top_frame, bg='black', fg='green', width=20)
entry1 = tk.Entry(top_frame)
entry2 = tk.Entry(top_frame)


def div(event):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        lab['text'] = num1 / num2
    except ZeroDivisionError:
        lab['text'] = 'Ошибка'
    except ValueError:
        lab['text'] = 'Ошибка'


def mult(event):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        lab['text'] = num1 * num2

    except ValueError:
        lab['text'] = 'Ошибка'


def degree(event):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        lab['text'] = num1 ** num2

    except ValueError:
        lab['text'] = 'Ошибка'


def sum(event):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        lab['text'] = num1 + num2

    except ValueError:
        lab['text'] = 'Ошибка'


button_sum = tk.Button(bottom_frame, text='+')
button_sum.bind('<Button-1>' or '<+>', sum)
button_degree = tk.Button(bottom_frame, text='**')
button_degree.bind('<Button-1>', degree)
button_mult = tk.Button(bottom_frame, text="*")
button_mult.bind('<Button-1>', mult)
button_div = tk.Button(bottom_frame, text="/")
button_div.bind('<Button-1>', div)
button_degree.pack(side=tk.RIGHT)
button_div.pack(side=tk.RIGHT)
button_sum.pack(side=tk.LEFT)
button_mult.pack(side=tk.LEFT)

lab.pack()
entry1.pack()
entry2.pack()

root.mainloop()