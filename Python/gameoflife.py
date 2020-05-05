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
    for cell in range(1, 501): # for loop that runs 500 times
        rectangle = canvas.create_rectangle(cell_positions(), fill='grey', outline='blue', tags='rectangle{}'.format(cell)) # on each iteration of the for loop 'rectangle' variable is updated with coordinates for a single cell
        cells_dict['rectangle{}'.format(cell)] = tuple(canvas.coords(rectangle)) # on each iteration the 'cells_dict' is updated with an entry of coordinates corresponding to the 'rectangle' variable on each iteration

        #canvas.create_rectangle(cell_positions(), fill='grey')
        #cells_dict = canvas.find_all()
    return cells_dict


# get_key() method will return the key given a value in the cells_dict dictionary
def get_key(*val):
    for key, value in cells_dict.items():
        if val == value:
            return key
    return "Key does not exist"


# get_value() method will return the value given a key in the cells_dict dictionary
def get_value(dict_key):
    for key, value in cells_dict.items():
        if dict_key == key:
            return value
    return "value does not exist"


# A method that will check/count each neighbour a cell has using
# the saved dictionary of coordinates 'cells_dict'. It will
# iterate through the dictionary and count each neighbour and
# return a dictionary that holds all cells with a neighbour
# neighbours_dict.
def check_neighbours(all_cells):
    neighbours_dict = {} # A dictionary that will hold all the neighbour cells and is returned at the end of the method
    for cell in all_cells.values(): # Loops through dictionary values i.e. coordinates
        x1, y1, x2, y2 = cell # each coordinate/cell is then split into separate variables
        cell_key = get_key(x1, y1, x2, y2) # Variable cell_key is created to so that i have the key of each value
        num_of_neighbours = canvas.find_overlapping(x1, y1, x2, y2) # num_of_neighbours holds the number of neighbours each coordinate/cell has, one means that the cell has no neighbours
        print('---------------')
        print('{} is at points {} and, has the neighbours {}.'.format(cell_key, get_value(cell_key), num_of_neighbours))
        print('---------------')
        for neighbour_cell in num_of_neighbours: # will loop the set of neighbours each cell has
            if len(num_of_neighbours) > 1: # if the length of the number of neighbours is greater than 1 it means that cell has a neighbour
                print('rectangle{} is at points {}'.format(neighbour_cell, canvas.coords(neighbour_cell)))
                neighbours_dict[cell_key] = num_of_neighbours # associates cell with their neighbours in the form of a dictionary
    return (neighbours_dict) # returns the dictionary that holds all the neighbour cells


create_multiple_cells()
rules(check_neighbours(cells_dict))

window.mainloop()
