from tkinter import *
from random import *

window = Tk()
window.title("John Conway's Game Of Life")
canvas = Canvas(window, background='white', width=800, height=600)


def create_grid(canvas):
    width = 800 # specifies width of the canvas
    height = 600 # specifies height of the canvas

    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')


create_grid(canvas)
canvas.grid(row=0, column=0)
window.mainloop()
