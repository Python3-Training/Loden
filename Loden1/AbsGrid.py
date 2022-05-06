#!/usr/bin/env python3

from abc import ABC, abstractmethod

class aGrid(ABC):

    @staticmethod
    @abstractmethod
    def Create(cells_wide, cells_high, font_wide, font_high):
        '''Factory. 
        Regions to be based upon cells, never pixels.
        Font width is number of characters each cell can hold.
        '''
        pass
     
    @abstractmethod
    def pour(self, color):
        '''
        Update & distribute a default cell color
        over the entire grid, preserving previous
        contents, if any.
        '''
        pass

    @abstractmethod
    def set_color(self, cellx, celly, color) -> bool:
        '''
        Set the color of the 0's based cell location.
        Colors to be a stringified color as per Tkinter.
        '''
        pass
     
    @abstractmethod
    def cls(self, color=None):
        '''
        Clear the screen to the desired color.
        Resets the default text content to empty.
        Default color to be platform defined.
        '''
        pass
     
    @abstractmethod
    def set_char(self, cellx, celly, a_char) -> bool:
        '''
        Set the content of a cell to the string.
        String size to be a multiple of font_wide.
        '''
        pass
    
    @abstractmethod
    def close(self):
        '''
        Close the window and / exit the program.
        '''
        pass
