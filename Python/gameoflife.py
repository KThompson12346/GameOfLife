from tkinter import *
from random import *
import time

window = Tk() # creates the window for the game
window.title('Game Of Life Python') # is the game title written on the window

canvas_frame = Frame(window) # creates a frame on the window to hold the canvas
game_title = Frame(window) # creates a frame on the window to display the game title (which will be a label)
start_button = Button(window, text='Start Game') # creates a button which will be used to start the game
canvas = Canvas(canvas_frame, width=910, height=700, background='black') # creates the canvas used to the draw the game of life
game_title_label = Label(game_title, text='Game Of Life', font='Helvetica 20 bold', fg='grey') # creates the label for the game title which will be placed in a frame

canvas.grid(row=0, column=0) # places the canvas onto the canvas_frame
canvas_frame.grid(row=1, column=1) # places the canvas_frame onto the window
game_title_label.grid(rowspan=2, column=0) # places the title of the game onto the game_title frame
game_title.grid(row=0, columnspan=2) # places the frame for the game title onto the window
start_button.grid(rowspan=2, column=1) # places the start onto the window

def cell_positions():
    x1 = randrange(0, 910, 10)
    y1 = randrange(0, 700, 10)
    x2 = x1 + 10
    y2 = y1 + 10
    return x1, y1, x2, y2

def multiple_cells():
    for cell in range(0, 500):
        canvas.create_rectangle(cell_positions(), fill='grey')

multiple_cells()

window.mainloop()
