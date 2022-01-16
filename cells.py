from cgitb import text
from re import T
from tkinter import N, Button, Label
import random
import setting
import ctypes
import sys
class Cell:
    all = []
    cell_label = None
    title = None
    cell_count = setting.cell_count
    def __init__(self, x, y, mine = False):
        self.mine = mine
        self.candidate_mine = False
        self.opened = False
        self.cell_button_object = None
        self.x = x
        self.y = y
    
    #append object to all
        Cell.all.append(self)

    def create_button(self, position):
        btn = Button(
            position,
            width = 12,
            height = 4
        )
        btn.bind('<Button-1>', self.left_click )
        btn.bind('<Button-3>', self.right_click )
        self.cell_button_object = btn

    @staticmethod
    def create_cell_counter_label(position):
        lbl = Label(
            position,
            bg= "black",
            fg = "white",
            text=f"Cells left : {Cell.cell_count}",
            font = ("Comic Sans", 30)
        )
        Cell.cell_label = lbl

    def left_click(self, event):
        if self.mine:
            self.showMine()
        else:
            if self.cells_arround_mines == 0:
                for x in self.cells_around:
                    x.showCell()
            self.showCell()
            if Cell.cell_count == setting.mine_count:
                 ctypes.windll.user32.MessageBoxW(0, 'YESSSS you won this time, another try ?', 'game over', 0)
        self.cell_button_object.unbind('<Button-1>')
        self.cell_button_object.unbind('<Button-3>')
   
    def cell_by_axis (self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def cells_around(self):
        surround = [
            self.cell_by_axis(self.x - 1, self.y - 1),
            self.cell_by_axis(self.x - 1, self.y),
            self.cell_by_axis(self.x - 1, self.y + 1),
            self.cell_by_axis(self.x, self.y -1),
            self.cell_by_axis(self.x + 1, self.y - 1),
            self.cell_by_axis(self.x + 1, self.y),
            self.cell_by_axis(self.x + 1, self.y + 1),
            self.cell_by_axis(self.x , self.y + 1)
        ]
        
        surround = [cell for cell in surround if cell is not None]
        return surround

    @property
    def cells_arround_mines(self):
        counter = 0
        for cell in self.cells_around:
            if cell.mine:
                counter += 1
        return counter

    def showCell(self):
        if not self.opened:
            Cell.cell_count -= 1
            self.cell_button_object.configure(text=self.cells_arround_mines)
           
            if Cell.cell_label:
                Cell.cell_label.configure(text =f"Cells left : {Cell.cell_count}")

            self.cell_button_object.configure(
                bg = 'SystemButtonFace'
            )
        self.opened = True

    def showMine(self):
        self.cell_button_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, 'OOOPSSSS it is a mine', 'game over', 0)
        sys.exit()
        

    def right_click(self, event):
        if not self.candidate_mine:
            self.cell_button_object.configure(bg = 'orange')
            self.candidate_mine = True
        else:
            self.cell_button_object.configure( bg = 'SystemButtonFace')
            self.random_mines = False
    
    @staticmethod
    def create_cell_title_label(position):
        title = Label(
            position,
            bg= "black",
            fg = "red",
            text=f"Welcome To Minesweeper",
            font = ("Comic Sans", 30)
        )
        Cell.cell_title = title

    @staticmethod
    def random_mines():
        selected_cells = random.sample(Cell.all, setting.mine_count)
        for selected_cell in selected_cells:
            selected_cell.mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
    