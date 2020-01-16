from tkinter import *

root = Tk()


def open_():
    try:
        for i in open(file_field.get(), encoding='UTF-8'):
            text_field.insert(END, i)
    except FileNotFoundError:
        text_field.delete(0.0, END)
        text_field.insert(1.0, "File not found")


def save_():
    f = open(file_field.get(), encoding='UTF-8', mode='w')
    f.write(text_field.get(1.0, END))
    f.close()


f_entry_open_save = Frame(root)
text_field = Text(width=50, height=30)
file_field = Entry(f_entry_open_save, width=30)
open_button = Button(f_entry_open_save, text="Open", width=10, height=1, command=open_)
save_button = Button(f_entry_open_save, text="Save", width=10, height=1, command=save_)
f_entry_open_save.pack()
scroll_x = Scrollbar(orient=HORIZONTAL, command=text_field.xview)
scroll_y = Scrollbar(command=text_field.yview)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
file_field.pack(side=LEFT)
save_button.pack(side=RIGHT)
open_button.pack(side=RIGHT)

text_field.pack()
root.mainloop()
