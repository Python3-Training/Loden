#!/usr/bin/env python3

from AbsGrid import aGrid
import tkinter as tk
from tkinter import font

class GridT(aGrid):

    def __init__(self, cells_wide, cells_high, cell_wide, cell_high, font_size=16):
        self.color_fore = '#00ff00'
        self.color_back = '#0000ff'
        self.color_border = '#000000'
        self.cells_wide = cells_wide
        self.cells_high = cells_high
        self.cell_wide = cell_wide
        self.cell_high = cell_high
        self._win = None
        self._cells = []
        self._fntsize = font_size
    
    def _init_win(self):
        self.close()
        self._win = tk.Tk()
        self._win.title("Loden")
        zpane = tk.Frame(self._win)
        zfont = font.nametofont('TkFixedFont')
        zfont.configure(size=self._fntsize)
        self._win.geometry(f"+{50}+{50}")
        self._win['bg'] =self.color_back
        self._win['borderwidth'] = 2 # margin nsew
        for yhigh in range(self.cells_high):
            for xwide in range(self.cells_wide):
                a_wgt = tk.Button(
                    zpane,
                    font=zfont,
                    bg=self.color_fore,
                    width=self.cell_wide,
                    height=self.cell_high,
                    relief=tk.SOLID
                    )
                a_wgt.grid(row=xwide,column=yhigh)
                self._cells.append(a_wgt)
        zpane.pack(expand=True)
        self.zpane = zpane

    def get_cell(self, xloc, yloc):
        max_ = xloc * self.cells_wide + yloc
        if len(self._cells) > max_:
            a_wgt = self._cells[max_]
            return self._win.nametowidget(a_wgt)

    @staticmethod
    def Create(cells_wide, cells_high, cell_wide, cell_high):
        result = GridT(cells_wide, cells_high,
                       cell_wide, cell_high)
        result._init_win()
        return result

    def pour(self, color):
        for cell in self._cells:
            a_wgt = self._win.nametowidget(cell)
            a_wgt.config(bg=color)
        self.color_fore = color    

    def set_color(self, cellx, celly, color) -> bool:
        a_wgt = self.get_cell(cellx, celly)
        if a_wgt:
            a_wgt.config(bg=color)
            return True
        return False

    def cls(self, color=None):
        if not color:
            color = self.color_fore
        for cell in self._cells:
            a_wgt = self._win.nametowidget(cell)
            a_wgt['text'] = ' '
            a_wgt.config(bg=color)

    def set_char(self, cellx, celly, a_char) -> bool:
        a_wgt = self.get_cell(cellx, celly)
        if a_wgt:
            a_wgt['text'] = a_char
            return True
        return False
    
    def close(self):
        if self._win:
            try:
                self._win.destroy()
            except:
                pass
            finally:
                self._win = None


if __name__ == '__main__':
    w = GridT.Create(10,10,2,2)
    w.set_color(0, 0, 'red')
    w.set_char(0, 0, '#')
    w.set_color(4, 4, '#ee00ee')
    w.set_char(4, 4, '!')

