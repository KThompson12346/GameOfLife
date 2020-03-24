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

cells_dict = {}


def cell_positions():
    x1 = randrange(0, 910, 10)
    y1 = randrange(0, 700, 10)
    x2 = x1 + 10
    y2 = y1 + 10
    return (x1, y1, x2, y2)


def create_multiple_cells(): # method to create the cells on the canvas
    for cell in range(0, 500): # for loop that runs 500 times
        rectangle = canvas.create_rectangle(cell_positions(), fill='grey') # on each iteration of the for loop 'rectangle' variable is updated with coordinates for a single cell
        cells_dict['rectangle{0}'.format(cell)] = tuple(canvas.coords(rectangle)) # on each iteration the 'cells_dict' is updated with an entry of coordinates corresponding to the 'rectangle' variable on each iteration
    return cells_dict

# A method that will check/count each neighbour a cell has using
# the saved dictionary of coordinates 'cells_dict'. It will
# iterate through the dictionary and count each neighbour
def check_neighbours(all_cells):
    for cell in all_cells.values():
        x1, y1, x2, y2 = cell
        num_of_neighbours = canvas.find_overlapping(x1, y1, x2, y2)
        print('The cell {}, has {} neighbours '.format(cell, num_of_neighbours))


create_multiple_cells()
check_neighbours(cells_dict)
#print(cells_dict)
blue_rectangle = canvas.create_rectangle(455, 350, 465, 360, fill='blue')
red_rectangle = canvas.create_rectangle(465, 350, 475, 360, fill='red')


window.mainloop()
