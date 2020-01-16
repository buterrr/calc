from tkinter import *


def transfer_to_selected():
    """
    The function takes the selected value from the general list or several selected
    values and transfers to the selected
    list and removes the transferred values from the general list.
    :return: none
    """
    selected = list(general_box.curselection())
    for i in selected:
        selected_box.insert(END, general_box.get(i))
    selected.reverse()
    for select in selected:
        general_box.delete(select)


def general_list_transfer():
    """
    Opposite  transfer_to_selected function.
    :return: none
    """
    selected = list(selected_box.curselection())
    for i in selected:
        general_box.insert(END, selected_box.get(i))
    selected.reverse()
    for select in selected:
        selected_box.delete(select)


general_list = ['carrot', 'pineapple', 'apple', 'potato', 'garlic',
                'orange', 'onion', 'butter', 'whiskey', 'coffee', 'milk']

root = Tk()

general_box = Listbox(selectmode=EXTENDED)
general_box.pack(side=LEFT, fill=Y)
scroll = Scrollbar(command=general_box.yview)
scroll.pack(side=LEFT, fill=Y)
general_box.config(yscrollcommand=scroll.set)

for i in general_list:
    general_box.insert(END, i)

my_frame = Frame()
my_frame.pack(side=LEFT, expand=1)
gen_box_but = Button(my_frame, text="<<<", command=general_list_transfer)
gen_box_but.pack(expand=1, fill=X)
sel_box_but = Button(my_frame, text=">>>", command=transfer_to_selected)
sel_box_but.pack(expand=1, fill=X)

selected_box = Listbox(selectmode=EXTENDED)
selected_box.pack(side=RIGHT, fill=Y)
scroll = Scrollbar(command=selected_box.yview)
scroll.pack(side=LEFT, fill=Y)
selected_box.config(yscrollcommand=scroll.set)

root.mainloop()
