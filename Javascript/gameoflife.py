from tkinter import *
from random import *
import time
import numpy as np

PIXEL_SIZE = 10
ROW = 910
COLUMN = 700

window = Tk() # creates the window for the game
window.title('Game Of Life Python') # is the game title written on the window

canvas_frame = Frame(window) # creates a frame on the window to hold the canvas
game_title = Frame(window) # creates a frame on the window to display the game title (which will be a label)
start_button = Button(window, text='Start Game') # creates a button which will be used to start the game
canvas = Canvas(canvas_frame, width=ROW, height=COLUMN, background='black') # creates the canvas used to the draw the game of life
game_title_label = Label(game_title, text='Game Of Life', font='Helvetica 20 bold', fg='grey') # creates the label for the game title which will be placed in a frame

canvas.grid(row=0, column=0) # places the canvas onto the canvas_frame
canvas_frame.grid(row=1, column=1) # places the canvas_frame onto the window
game_title_label.grid(rowspan=2, column=0) # places the title of the game onto the game_title frame
game_title.grid(row=0, columnspan=2) # places the frame for the game title onto the window
start_button.grid(rowspan=2, column=1) # places the start onto the window



def create_grid():
    grid = []
    for row in range(0, ROW):
        grid2 = []
        for column in range(0, COLUMN):
            grid2.append(randint(0, 1))
        grid.append(grid2)
    return grid


def draw_grid(game_grid):
        for row in range(0, ROW):
            for column in range(0, COLUMN):
                if game_grid[row][column] == 1:
                    x0 = row*PIXEL_SIZE
                    y0 = column*PIXEL_SIZE
                    x1 = x0+PIXEL_SIZE
                    y1 = y0+PIXEL_SIZE
                    canvas.create_rectangle(x0, y0, x1, y1, fill='red')


def apply_rules():
    pass

draw_grid(create_grid())
window.mainloop()
