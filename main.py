from tkinter import *
from shapes.shapes import *

tk = Tk()

window_width = 800
window_height = 600

win = Canvas(tk, width=window_width, height=window_height)
win.pack()

r = Rectangle(win, 100, 100, 50, 100, False, "#476042")
r.draw()
s = Square(win, 200, 200, 50, False, "#476042")
s.draw()
o = Oval(win, 300, 300, 50, 100, False, "#476042")
o.draw()
c = Circle(win, 400, 400, 50, False, "#476042")
c.draw()

win.mainloop()
