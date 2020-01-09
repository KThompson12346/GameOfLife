from tkinter import *
import random
import time


class game_window:

    def __init__(self, master):
        canvas_frame = Frame(master)
        game_title = Frame(master)
        start_button = Button(master, text='Start Game')
        canvas = Canvas(canvas_frame, width=910, height=700, background='black')
        game_title_label = Label(game_title, text='Game Of Life', font='Helvetica 20 bold', fg='grey')
        canvas.grid(row=0, column=0)
        canvas_frame.grid(row=1, column=1)
        game_title_label.grid(rowspan=2, column=0)
        game_title.grid(row=0, columnspan=2)
        start_button.grid(rowspan=2, column=1)


window = Tk()
window.title('Game Of Life Python')
gameoflife = game_window(window)
window.mainloop()
