import pygame
import time
import random

import field
import render
import two_in_one


def main():
    background_color = (0, 0, 0)
    snake_color = (10, 0, 0)
    food_color = (0, 15, 0)

    xy = [[0, 0], ]
    direction = 'right'
    game_field = field.get_field(background_color, snake_color, food_color, xy)
    render.show(two_in_one.convert(game_field))
    food = rand_coord_food(xy)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    if not direction == 'up' and not direction == 'down':
                        direction = 'up'
                if event.button == 2:
                    if not direction == 'up' and not direction == 'down':
                        direction = 'down'
                if event.button == 1:
                    if not direction == 'left' and not direction == 'right':
                        direction = 'right'
                if event.button == 3:
                    if not direction == 'ledt' and not direction == 'right':
                        direction = 'left'
                if event.button == 12:
                    xy = change_coord_list(xy, direction, True)
                if event.button == 11:
                    print(xy)
                if event.button == 10:
                    start_and_stop()
                if event.button == 9:
                    pause()

        xy = change_coord_list(xy, direction)
        if xy[-1] == food:
            food = rand_coord_food(xy)
            xy = change_coord_list(xy, direction, True)
        game_field = field.get_field(background_color, snake_color, food_color, xy, food)
        render.show(two_in_one.convert(game_field))
        time.sleep(0.2)


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
        coord_list.append(change_coord(coord_list[-1][:], direction))
    else:
        coord_list_temp = []
        for i in range(1, len(coord_list)):
            coord_list_temp.append(coord_list[i][:])
        coord_new = change_coord(coord_list[-1][:], direction)
        coord_list_temp.append(coord_new[:])
        if coord_new in coord_list:
            print(len(coord_list))
            time.sleep(2)
            start_and_stop()
        coord_list = coord_list_temp[:]
    return coord_list[:]


def rand_coord_food(xy):
    while True:
        food = random.sample(range(0, 16), 2)
        if food not in xy:
            return food


def pause():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 9:
                    return 0 


def start_and_stop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 10:
                    main()


def init():
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


if __name__ == '__main__':
    init()
    start_and_stop()
