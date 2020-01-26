def get_field(background_color, snake_color, xy):
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
    return game_field
