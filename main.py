from tkinter import *
from turtle import width
import setting
import utils
from cells import Cell
root = Tk()

# Title

#change the window
root.configure(bg="blue")
root.geometry(f'{setting.widht}x{setting.height}')
root.title("Minesweeper Game")
root.resizable(False, False)

#layouting the window
top_frame = Frame(root, bg= "yellow", width = utils.percentage_widht(100), height = utils.percentage_height(25))
top_frame.place(x = 0, y = 0)


left_frame = Frame(root, bg = "white", width = utils.percentage_widht(25), height = utils.percentage_height(75))
left_frame.place(x = 0, y = utils.percentage_height(25))

center_frame = Frame(root, bg = "violet", width = utils.percentage_widht(75), height = utils.percentage_height(75))
center_frame.place(x = utils.percentage_widht(25), y = utils.percentage_height(25))

for x in range(8):
    for y in range(8):
        c = Cell(x, y)
        c.create_button(center_frame)
        c.cell_button_object.grid(column = x, row = y)

Cell.create_cell_title_label(top_frame)
Cell.cell_title.place(x = utils.percentage_widht(25), y = 0)
Cell.create_cell_counter_label(left_frame)
Cell.cell_label.place(x = 0, y = 0)
Cell.random_mines()

#debug line to make sure to make the mines
# for c in Cell.all: 
#     print(c.mine)


#run window
root.mainloop()