import time
import random

import field
import render
import two_in_one

background_color = (0, 0, 0)
snake_color = (7, 0, 7)

xy = [[0, 0], [1, 0], [0, 1], [1, 1]] 

game_field = field.get_field(background_color, snake_color, xy)
render.show(two_in_one.convert(game_field))

while True:
    d = input()
    if d == 'w':
        for i in xy:
            i[0] += 1
    if d == 's':
        for i in xy:
            i[0] -= 1
    if d == 'd':
        for i in xy:
            i[1] += 1
    if d == 'a':
        for i in xy:
            i[1] -= 1
    game_field = field.get_field(background_color, snake_color, xy)
    render.show(two_in_one.convert(game_field))
"""
d = input()
    if d == 'w':
        for i in xy:
            i[0] += 1
        game_field = field.get_field(background_color, snake_color, xy)
        render.show(two_in_one.convert(game_field))

"""
