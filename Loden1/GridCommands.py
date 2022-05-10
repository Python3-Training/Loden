#!/usr/bin/env python3
# Mission: Provide a reusable set of grid-management operations.

from AbsCommand import Command, NoCommand, BadParam

class CmdHelp(Command):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        return self.key    

class CmdValues(Command):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        return self.key    

class CmdOpen(Command):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        return self.key    

class CmdClose(Command):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        return self.key    

class CmdEvents(Command):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        return self.key    

class CmdEvent(Command):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        return self.key

