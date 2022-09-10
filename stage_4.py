def get_input():
    input_string = input()
    return '| ' + " ".join(input_string[:3]) + ' |', '| ' + " ".join(input_string[3:6]) + ' |', '| ' + " ".join(input_string[6:]) + ' |'
    
def create_field():
    line_1, line_2, line_3 = get_input()
    top_bot_border = '-' * 9
    return top_bot_border + '\n' + line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + top_bot_border

def main():
    global field
    field = create_field()
    print(field)
    user_plays()
    #state_play()

def X_wins():
    hor_1 = field[12] == field[14] == field[16] == 'X' 
    hor_2 = field[22] == field[24] == field[26] == 'X'
    hor_3 = field[32] == field[34] == field[36] == 'X'
    ver_1 = field[12] == field[22] == field[32] == 'X'
    ver_2 = field[14] == field[24] == field[34] == 'X'
    ver_3 = field[16] == field[26] == field[36] == 'X'
    dia_1 = field[12] == field[24] == field[36] == 'X' 
    dia_2 = field[16] == field[24] == field[32] == 'X'
    return any([hor_1, hor_2, hor_3, ver_1, ver_2, ver_3, dia_1, dia_2])    

def O_wins():
    hor_1 = field[12] == field[14] == field[16] == 'O' 
    hor_2 = field[22] == field[24] == field[26] == 'O'
    hor_3 = field[32] == field[34] == field[36] == 'O'
    ver_1 = field[12] == field[22] == field[32] == 'O'
    ver_2 = field[14] == field[24] == field[34] == 'O'
    ver_3 = field[16] == field[26] == field[36] == 'O'
    dia_1 = field[12] == field[24] == field[36] == 'O' 
    dia_2 = field[16] == field[24] == field[32] == 'O'
    return any([hor_1, hor_2, hor_3, ver_1, ver_2, ver_3, dia_1, dia_2])   

def game_not_finish():
    return '_' in field
        

def impossible():
    no_X = field.count('X')
    no_Y = field.count('O')
    return no_X - no_Y > 1 or no_Y - no_X > 1
        

def state_play():
    X_winner = X_wins()
    O_winner = O_wins()
    not_finished = game_not_finish()
    bad_game = impossible()
    if bad_game or X_winner == O_winner == True:
        print('Impossible') 
    elif X_winner and O_winner:
        print('Impossible') 
    elif X_winner:
        print('X wins')
    elif O_winner:
        print('O wins')
    elif not_finished:
        print('Game not finished')
    else:
        print('Draw')
    
def user_plays():
    global field
    can_play = True
    while can_play == True:
        print('input 2 coordinate numbers that represent the cell where you want to place your X, for example, 1 1')
        print('Numbers must be between 1 and 3, inclusive.')
        input_coordinates = input("Please, enter coordinates: ")
        y_coordinate = input_coordinates[0]
        x_coordinate = input_coordinates[2]
    
        try:
            int(x_coordinate)
        except TypeError:
             print('You should enter numbers!')
             continue
        try:
            int(y_coordinate)
        except TypeError:
             print('You should enter numbers!')
             continue
        else:
            if int(x_coordinate) > 3 or int(y_coordinate) > 3:
                print('Coordinates should be from 1 to 3!')
                continue
            x_field_coord = str(int(x_coordinate) * 2)
            y_field_coord = y_coordinate
            xy_field_coord = int(y_field_coord + x_field_coord)
            if field[xy_field_coord] == 'X' or field[xy_field_coord] == 'O':
                print('This cell is occupied! Choose another one!')
            else:
                field = field[:xy_field_coord] + 'X' + field[xy_field_coord + 1:]
                print(field)
                can_play = False
                
        
        
    






if __name__ == "__main__":
    main()
