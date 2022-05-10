#!/usr/bin/env python3
# Mission: Provide a reusable set of grid-management operations.

__all__ = ["CmdHelp","CmdValues","CmdOpen","CmdClose",
           "CmdEvents","CmdEvent",]

from AbsGrid import aGrid
from AbsCommand import aCommand, NoCommand, BadParam


class Validate:
    @staticmethod
    def validate(a_cmd, a_grid, full_command):
        if not isinstance(a_cmd, aCommand):
            raise NoCommand("Error: AbsCommand child required.")
        Validate.check_prefix(a_cmd.key, full_command)
        Validate.check_instance(a_grid)
    
    ''' Common parameter validations. '''
    @staticmethod
    def check_instance(a_grid):
        ''' Verif a_grid existance & type. '''
        if not a_grid:
            raise NoCommand("Error: No grid provided.")
        if not isinstance(a_grid, aGrid):
            raise BadParam("Error: Unsupported Object.")

    @staticmethod
    def check_prefix(dot_name, full_command):
        ''' Full commands must begin with the dot_name. '''
        if not full_command.lower().startswith(dot_name.lower()):
            raise NoCommand("Error: Command mismatch.")


class CmdHelp(aCommand):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        Validate.validate(self, a_grid, full_command)
        return self.key    

class CmdValues(aCommand):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        Validate.validate(self, a_grid, full_command)
        return self.key    

class CmdOpen(aCommand):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        Validate.validate(self, a_grid, full_command)
        return self.key    

class CmdClose(aCommand):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        Validate.validate(self, a_grid, full_command)
        return self.key    

class CmdEvents(aCommand):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        Validate.validate(self, a_grid, full_command)
        return self.key    

class CmdEvent(aCommand):
    def __init__(self, key):
        self.key = key
    
    def execute(self, a_grid, full_command) -> str():
        Validate.validate(self, a_grid, full_command)
        return self.key

