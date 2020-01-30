import pygame
import time
import random

import field
import render
import two_in_one


def main():



    pygame.init()
    controller = pygame.joystick.Joystick(0)
    controller.init()
    pygame.display.set_mode((1, 1))
    axis = {}
    button = {}
    AXIS_X = 3
    AXIS_Y = 4
    rot_x = 0.0
    rot_y = 0.0


    background_color = (0, 0, 0)
    snake_color = (55, 55, 0)

    xy = [[0, 0], ] 
    direction = 'right'
    game_field = field.get_field(background_color, snake_color, xy)
    render.show(two_in_one.convert(game_field))

    while True:
        if pygame.mixer.get_busy() != None:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        direction = 'up'
                        xy = change_coord_list(xy, direction)
                        game_field = field.get_field(background_color, snake_color, xy)
                        render.show(two_in_one.convert(game_field))
                    if event.button == 2:
                        direction = 'down'
                        xy = change_coord_list(xy, direction)
                        game_field = field.get_field(background_color, snake_color, xy)
                        render.show(two_in_one.convert(game_field))
                    if event.button == 1:
                        direction = 'right'
                        xy = change_coord_list(xy, direction)
                        game_field = field.get_field(background_color, snake_color, xy)
                        render.show(two_in_one.convert(game_field))
                    if event.button == 3:
                        direction = 'left'
                        xy = change_coord_list(xy, direction)
                        game_field = field.get_field(background_color, snake_color, xy)
                        render.show(two_in_one.convert(game_field))
                    if event.button == 12:
                        xy = change_coord_list(xy, direction, True)
                        game_field = field.get_field(background_color, snake_color, xy)
                        render.show(two_in_one.convert(game_field))
                        print(xy)
        time.sleep(0.1)


def change_coord(coord, direction):
    if direction == 'up':
        coord[1] += 1
        if coord[1] > 15:
             coord[1] = 0
        if coord[1] < 0:
             coord[1] = 15
    elif direction == 'down':
        coord[1] -= 1
        if coord[1] > 15:
            coord[1] = 0
        if coord[1] < 0:
            coord[1] = 15
    elif direction == 'right':
        coord[0] += 1
        if coord[0] > 15:
             coord[0] = 0
        if coord[0] < 0:
            coord[0] = 15
    elif direction == 'left':
        coord[0] -= 1
        if coord[0] > 15:
            coord[0] = 0
        if coord[0] < 0:
            coord[0] = 15
    else:
        print('Something wrong!!! Connect to the admin')
    return coord[:]


def change_coord_list(coord_list, direction, new = False):
    if new:
        coord_list.append(change_coord(coord_list[-1], direction))
    else:
        coord_list_temp = []
        for i in range(1, len(coord_list)):
            coord_list_temp.append(coord_list[i])
        coord_list_temp.append(change_coord(coord_list[-1], direction))
        coord_list = coord_list_temp[:]
    return coord_list[:]



if __name__ == '__main__':
    main()
