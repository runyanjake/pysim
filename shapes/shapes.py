from tkinter import *

class Rectangle:
    def __init__(self, win, x, y, width, height, fill, color):
        self.win = win
        self.xpos = x
        self.ypos = y
        self.width = width
        self.height = height
        self.fill = fill
        self.color = color

    def draw(self):
        self.win.create_line(self.xpos, self.ypos, self.xpos + self.width, self.ypos, fill=self.color)
        self.win.create_line(self.xpos + self.width, self.ypos, self.xpos + self.width, self.ypos + self.height, fill=self.color)
        self.win.create_line(self.xpos + self.width, self.ypos + self.height, self.xpos, self.ypos + self.height, fill=self.color)
        self.win.create_line(self.xpos, self.ypos + self.height, self.xpos, self.ypos, fill=self.color)


class Square(Rectangle):
    def __init__(self, win, x, y, width, fill, color):
        super().__init__(win, x, y, width, width, fill, color)

    def draw(self):
        super().draw()


class Oval:
    def __init__(self, win, x, y, width, height, fill, color):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.color = color

    def draw(self):
        self.win.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)


class Circle(Oval):
    def __init__(self, win, x, y, width, fill, color):
        super().__init__(win, x, y, width, width, fill, color)

    def draw(self):
        super().draw()
