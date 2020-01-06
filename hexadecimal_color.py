from tkinter import *

colors = {'красный': '#ff0000',
          'оранжевый': '#ff7d00',
          'желтый': '#ffff00',
          'зеленый': '#00ff00',
          'голубой': '#007dff',
          'синий': '#0000ff',
          'фиолетовый': '#7d00ff'
          }


class But:
    def __init__(self, master, color, color_code):
        self.color = color
        self.color_code = color_code
        self.but = Button(master, width=15, bg=self.color_code, command=self.set_color)
        self.but.pack()

    def set_color(self):
        l1.config(text=self.color)
        e1.delete(0, END)
        e1.insert(0, self.color_code)


root = Tk()
l1 = Label()
e1 = Entry(bd=3)
l1.pack()
e1.pack()

for c in colors.keys():
    But(root, c, colors[c])

root.mainloop()
#ff0000 – красный, #ff7d00 – оранжевый, #ffff00 – желтый,
# #00ff00 – зеленый, #007dff – голубой,
# #0000ff – синий, #7d00ff – фиолетовый