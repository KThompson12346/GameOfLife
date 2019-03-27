from tkinter import *
from random import *

window = Tk()
window.title("John Conway's Game Of Life")
canvas = Canvas(window, background='white', width=500, height=500)


def x_value(): # this function will create a random x_value that is between 0 and 500 and is a multiple of 10
    return choice(range(0, 500, 10))
def y_value(): # this function will create a random y_value that is between 0 and 500 and is a multiple of 10
    return choice(range(0, 500, 10))


def rectangle_points(): # This function creates four points used to create the rectangles on the grid, all of which are multiples of 10
    x1 = x_value()
    y1 = y_value()
    x2 = x1 + 10
    y2 = y1 + 10
    return x1, y1, x2, y2

def create_grid(canvas): # This function creates the grid lines on the canvas which are spaced out by 10 in both the x and y directions
    width = 500 # specifies width of the canvas
    height = 500 # specifies height of the canvas

    for line in range(0, width, 10): # range(start, stop, step), creates lines along the x direction that is 10 spaces apart and goes up to the width of the window
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10): # creates lines along the y directiion that is 10 spaces apart and goes up to the height of the window
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

def draw(canvas): # This methed draws the initial start of the game of life grid
    counter = 0
    while counter < 131:
        canvas.create_rectangle(rectangle_points(), fill='red')
        canvas.update()
        counter += 1

def update_grid(canvas):
    pass

create_grid(canvas)
draw(canvas)
canvas.grid(row=0, column=0)
window.mainloop()
