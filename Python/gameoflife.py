from tkinter import *
import random
import time

window = Tk()
window.title('Game Of Life Python')
game_title = Frame(window) # frame for the game of life title

canvas_frame = Frame(window) # frame for the canvas
canvas = Canvas(canvas_frame, width=910, height=700, background='black') # creates the canvas size

game_title_label = Label(game_title, text='Game Of Life', font='Helvetica 20 bold', fg='grey') # creates the label for the game title

canvas.grid(row=0, column=0) # puts canvas onto the canvas_frame
canvas_frame.grid(row=1, column=1) # puts canvas_frame onto the window
game_title_label.grid(rowspan=2, column=0) # puts the game_title_label onto the game_title frame
game_title.grid(row=0, columnspan=2)



window.mainloop()
