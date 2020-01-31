def get_field(background_color, snake_color, food_color, xy, food = None):
    game_field = [
        [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

        [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],

     [background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color, background_color],
            ]
    
    for i in xy:
        game_field[i[0]][i[1]] = snake_color
    if food != None:
        game_field[food[0]][food[1]] = food_color

    return game_field
