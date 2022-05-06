#!/usr/bin/env python3

from abc import ABC, abstractmethod

class aGrid(ABC):

    @staticmethod
    @abstractmethod
    def Create(cells_wide, cells_high, pix_wide, pix_high):
        pass
    
    @abstractmethod
    def set_color(self, cellx, celly, color) -> bool:
        pass
     
    @abstractmethod
    def cls(self, color=None):
        pass
     
    @abstractmethod
    def set_char(self, cellx, celly, a_char) -> bool:
        pass
    
    @abstractmethod
    def close(self):
        pass
