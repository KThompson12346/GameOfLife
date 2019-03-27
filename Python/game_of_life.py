from tkinter import *
from random import *

window = Tk()
window.title("John Conway's Game Of Life")
canvas = Canvas(window, background='white', width=500, height=500)


def x_value():
    return choice(range(0, 500, 10))
def y_value():
    return choice(range(0, 500, 10))


def create_rect():
    x1 = x_value()
    y1 = y_value()
    x2 = x1 + 10
    y2 = y1 + 10
    return x1, y1, x2, y2

def create_grid(canvas):
    width = 500 # specifies width of the canvas
    height = 500 # specifies height of the canvas

    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

def draw(canvas):
    pass

def update_grid(canvas):
    pass

create_grid(canvas)
draw(canvas)
canvas.grid(row=0, column=0)
window.mainloop()
