#!/usr/bin/env python3
# Mission: Create a command-line interface (CLI)

from GridTK import GridT
from GridGrammer import Grmr01
from AbsCommand import NoCommand, BadParam

app = Grmr01()
a_grid = GridT(10, 8, 3, 3)
while(True):
    try:
        cmd = input(": ")
        a_cmd = app.get_command(cmd)
        response = a_cmd.execute(a_grid, cmd)
        print(response)
    except Exception as ex:
        print(ex)
        break
          
