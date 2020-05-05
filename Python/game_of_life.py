from tkinter import *
from random import *
import time

PIXEL_SIZE = 10
ROW = 910
COLUMN = 700
data = {}

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


def initialize():
    for width in range(0, ROW):
        for height in range(0, COLUMN):
            data[(width, height)] = randint(0,1)

def populate():
    for row, column in data.keys():
        tag = f"{row}x{column}"
        x0 = column*PIXEL_SIZE
        y0 = row*PIXEL_SIZE
        x1 = x0+PIXEL_SIZE
        y1 = y0+PIXEL_SIZE
        color = "red" if data[(row,column)] == 1 else "green"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags=(tag,))

def get_value(w, h):
    for key, value in data.items():
        if data[(w, h)] == data[key]:
            return value
    return "value does not exist"


def rules():
    neighbours_count = 0
    for row in data.keys():
        for column in data.keys():
            neighbours_count += data[row-1][column-1] # top left
            neighbours_count += data[row-1][column] # top center
            neighbours_count += data[row+1][column-1] # top right

            neighbours_count += data[row][column-1] # middle left
            neighbours_count += data[row][column+1] # middle right

            neighbours_count += data[row-1][column+1] # bottom left
            neighbours_count += data[row][column+1] # bottom center
            neighbours_count += data[row+1][column+1] # bottom right

            # Game Of Life rules

            # alive cell rules
            if data[(row, column)] == 1:
                # rule 1 any live cell with fewer than two live neighbours dies, as if by underpopulation
                if neighbours_count < 2:
                    data[(row, column)] = 0
                # rule 2 any live cell with two or three live neighbours lives on to the next generation
                elif neighbours_count == 2 | neighbours_count == 3:
                    data[(row, column)] = 1
                # rule 3 any live cell with more than three live neighbours dies, as if by overpopulation
                elif neighbours_count > 3 & neighbours_count <= 8:
                    data[(row, column)] = 0
                else:
                    data[(row, column)] = 0
            # dead cells rules
            # rule 4 any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
            elif data[(row, column)] == 0:
                if neighbours_count == 3:
                    data[(row, column)] = 1
                else:
                    data[(row, column)] = 0 





initialize()
populate()
window.mainloop()
