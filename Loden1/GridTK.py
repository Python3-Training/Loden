#!/usr/bin/env python3
'''
A Tkinter realization for the grid abstration.

Whimsical demonstration "makes faces, in time."

'''
from AbsGrid import aGrid
import tkinter as tk
from tkinter import font

class GridT(aGrid):

    def __init__(self, cells_wide, cells_high, cell_wide, cell_high, font_size=16):
        self._color_back = '#00ff00'
        self._color_fore = '#0000ff'
        self._color_border = '#000000'
        self._cells_wide = cells_wide
        self._cells_high = cells_high
        self._cell_wide = cell_wide
        self._cell_high = cell_high
        self._win = None
        self._cells = []
        self._fntsize = font_size
        self._time_lapse = 1000 # milisecond default
        self._times = 0
    
    def _init_win(self):
        self.close()
        self._win = tk.Tk()
        self._win.title("Loden")
        zpane = tk.Frame(self._win)
        zfont = font.nametofont('TkFixedFont')
        zfont.configure(size=self._fntsize)
        zfont.configure(weight=font.BOLD)
        self._win.geometry(f"+{50}+{50}")
        self._win['bg'] =self._color_border
        self._win['borderwidth'] = 2 # margin nsew
        for yhigh in range(self._cells_wide):
            for xwide in range(self._cells_high):
                a_wgt = tk.Button(
                    zpane,
                    font=zfont,
                    bg=self._color_back,
                    fg=self._color_fore,
                    width=self._cell_wide, # font
                    height=self._cell_high,# font
                    relief=tk.SOLID
                    )
                a_wgt.grid(row=xwide,column=yhigh)
                self._cells.append(a_wgt)
        zpane.pack(expand=True)
        self.zpane = zpane

    def ticker(self, mili_sec=None):
        '''
        Beschedule the very NEXT callback to .tick()
        '''
        if not mili_sec:
            mili_sec = self._time_lapse
        self.zpane.after(mili_sec, self.tick)
        self._time_lapse = mili_sec
        self._times += 1

    def tick(self):
        '''
        To activate one must first call .ticker().
        One must also re-sechedule using the same,
        as demonstrated herein.
        '''
        import random
        r = hex(random.randrange(0, 255))[2:]
        g = hex(random.randrange(0, 255))[2:]
        b = hex(random.randrange(0, 255))[2:]
        acolor = f'#{r:<02}{g:<02}{b:<02}'
        x = random.randrange(0, self._cells_wide)
        y = random.randrange(0, self._cells_high)
        if self._times % (len(self._cells)/2) == 0:
            self.cls(acolor)
        else:
            face = random.randrange(0x1f600, 0x1f619)
            self.set_char(x, y, chr(face))
            self.set_color(x, y, acolor)
        self.ticker()

    def get_cell(self, xloc, yloc):
        '''
        Handy way to get the representational widget.
        Returns None if none found.
        '''
        max_ = (yloc * self._cells_wide) + xloc
        if len(self._cells) > max_:
            a_wgt = self._cells[max_]
            return self._win.nametowidget(a_wgt)

    def back(self, color):
        '''
        Update & distribute a default cell color
        over the entire grid, preserving previous
        contents, if any.
        '''
        for cell in self._cells:
            a_wgt = self._win.nametowidget(cell)
            a_wgt.config(bg=color)
        self._color_back = color    

    def fore(self, color):
        '''
        Update & distribute a default foreground color
        over the entire grid, preserving previous
        contents, if any.
        '''
        for cell in self._cells:
            a_wgt = self._win.nametowidget(cell)
            a_wgt.config(fg=color)
        self._color_fore = color    

    def set_color(self, cellx, celly, color) -> bool:
        '''
        Set the color of the 0's based cell location.
        Colors to be a stringified color as per Tkinter.
        '''
        a_wgt = self.get_cell(cellx, celly)
        if a_wgt:
            a_wgt.config(bg=color)
            return True
        return False

    def cls(self, color=None):
        '''
        Clear the screen to the desired color.
        Resets the default text content to empty.
        Default color to be platform defined.
        '''
        if not color:
            color = self._color_back
        for cell in self._cells:
            a_wgt = self._win.nametowidget(cell)
            a_wgt['text'] = ' '
            a_wgt.config(bg=color)

    def set_char(self, cellx, celly, a_char) -> bool:
        '''
        Set the content of a cell to the string.
        String size to be a multiple of font_wide.
        '''
        a_wgt = self.get_cell(cellx, celly)
        if a_wgt:
            a_wgt['text'] = a_char
            return True
        return False
    
    def close(self):
        '''
        Close the window and / exit the program.
        '''
        if self._win:
            try:
                self._win.destroy()
            except:
                pass
            finally:
                self._win = None

    @staticmethod
    def Create(cells_wide, cells_high, cell_wide, cell_high):
        '''Factory. 
        Regions to be based upon cells, never pixels.
        Font width is number of characters each cell can hold.
        '''
        result = GridT(cells_wide, cells_high,
                       cell_wide, cell_high)
        result._init_win()
        return result


if __name__ == '__main__':
    w = GridT.Create(20,10,3,1)
    w.set_color(0, 0, 'red')
    w.set_char(0, 0, '#')
    w.set_color(4, 4, '#ee00ee')
    w.set_char(4, 4, '!')
    w.ticker(150)
    print("You can now use 'w.' (e.g. w.close()), as well.")

