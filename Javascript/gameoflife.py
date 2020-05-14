from tkinter import *
from random import *
import time
import numpy as np

PIXEL_SIZE = 10
ROW = 910
COLUMN = 700
grid = []
updated_grid = [[]]

def create_grid():
    for row in range(0, ROW):
        grid2 = []
        for column in range(0, COLUMN):
            grid2.append(randint(0, 1))
        grid.append(grid2)


def draw_grid():
    for row in range(0, ROW):
        for column in range(0, COLUMN):
            if grid[row][column] == 1:
                x0 = row*PIXEL_SIZE
                y0 = column*PIXEL_SIZE
                x1 = x0+PIXEL_SIZE
                y1 = y0+PIXEL_SIZE
                canvas.create_rectangle(x0, y0, x1, y1, fill='red')


def apply_rules():
    for row in range(1, ROW - 1):
        for column in range(1, COLUMN - 1):
            neighbours_count = 0
            # will count the neighbours for each cell
            neighbours_count += grid[row-1][column-1] # top left
            neighbours_count += grid[row][column-1] # top center
            neighbours_count += grid[row+1][column-1] # top right

            neighbours_count += grid[row-1][column] # middle left
            neighbours_count += grid[row+1][column] # middle right

            neighbours_count += grid[row-1][column+1] # bottom left
            neighbours_count += grid[row][column+1] # bottom center
            neighbours_count += grid[row+1][column+1] # bottom right

            # Game Of Life rules:

            # alive cell rules
            if grid[row][column] == 1:
                if neighbours_count < 2: # rule 1 any live cell with fewer than two live neighbours dies, as if by underpopulation
                    updated_grid[row][column] = 0
                elif neighbours_count == 2 | neighbours_count == 3: # rule 2 any live cell with two or three live neighbours lives on to the next generation
                    updated_grid[row][column] = 1
                elif neighbours_count > 3 & neighbours_count <= 8: # rule 3 any live cell with more than three live neighbours dies, as if by overpopulation
                    updated_grid[row][column] = 0
                else:
                    updated_grid[row][column] = 0
            elif grid[row][column] == 0: # dead cells rule 4 any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
                if neighbours_count == 3:
                    updated_grid[row][column] = 1
                else:
                    updated_grid[row][column] = 0
    for row in range(0, ROW):
        for column in range(0, COLUMN):
            grid[row][column] = updated_grid[row][column]


def one_cycle():
    apply_rules()
    draw_grid()
    window.after(1, one_cycle)


window = Tk() # creates the window for the game
window.title('Game Of Life Python') # is the game title written on the window
canvas_frame = Frame(window) # creates a frame on the window to hold the canvas
game_title = Frame(window) # creates a frame on the window to display the game title (which will be a label)
start_button = Button(window, text='Start Game', command=one_cycle) # creates a button which will be used to start the game
canvas = Canvas(canvas_frame, width=ROW, height=COLUMN, background='black') # creates the canvas used to the draw the game of life
game_title_label = Label(game_title, text='Game Of Life', font='Helvetica 20 bold', fg='grey') # creates the label for the game title which will be placed in a frame

canvas.grid(row=0, column=0) # places the canvas onto the canvas_frame
canvas_frame.grid(row=1, column=1) # places the canvas_frame onto the window
game_title_label.grid(rowspan=2, column=0) # places the title of the game onto the game_title frame
game_title.grid(row=0, columnspan=2) # places the frame for the game title onto the window
start_button.grid(rowspan=2, column=1) # places the start onto the window


create_grid()
window.mainloop()
