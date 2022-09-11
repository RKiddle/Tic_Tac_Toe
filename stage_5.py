

def main():
    global field
    field = '''
---------
|       |
|       |
|       |
---------
'''
    global turn
    turn = 1
    print(field)
    user_plays()
    state_play()

def X_wins():
    hor_1 = field[13] == field[15] == field[17] == 'X' 
    hor_2 = field[23] == field[25] == field[27] == 'X'
    hor_3 = field[33] == field[35] == field[37] == 'X'
    ver_1 = field[13] == field[23] == field[33] == 'X'
    ver_2 = field[15] == field[25] == field[35] == 'X'
    ver_3 = field[17] == field[27] == field[37] == 'X'
    dia_1 = field[13] == field[25] == field[37] == 'X' 
    dia_2 = field[17] == field[25] == field[33] == 'X'
    return any([hor_1, hor_2, hor_3, ver_1, ver_2, ver_3, dia_1, dia_2])    

def O_wins():
    hor_1 = field[13] == field[15] == field[17] == 'O' 
    hor_2 = field[23] == field[25] == field[27] == 'O'
    hor_3 = field[33] == field[35] == field[37] == 'O'
    ver_1 = field[13] == field[23] == field[33] == 'O'
    ver_2 = field[15] == field[25] == field[35] == 'O'
    ver_3 = field[17] == field[27] == field[37] == 'O'
    dia_1 = field[13] == field[25] == field[37] == 'O' 
    dia_2 = field[17] == field[25] == field[33] == 'O'
    return any([hor_1, hor_2, hor_3, ver_1, ver_2, ver_3, dia_1, dia_2])   

def game_not_finish():
    return '_' in field
        

def impossible():
    no_X = field.count('X')
    no_Y = field.count('O')
    return no_X - no_Y > 1 or no_Y - no_X > 1
        

def state_play():
    global turn
    while turn <= 9:
        X_winner = X_wins()
        O_winner = O_wins()
        if X_winner:
            print('X wins')
            break
        elif O_winner:
            print('O wins')
            break
        elif turn == 9 and X_winner == False and O_winner == False:
            print('Draw')
            break
        else: 
            user_plays()
        turn += 1
        
    
def user_plays():
    global field
    global token
    token = 'X'
    
    can_play = True
    while can_play == True:
        print('input 2 coordinate numbers that represent the cell where you want to place your X or O, for example, 1 1')
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

            if turn % 2 == 1:
                token = 'X'
            else: 
                token = 'O'
                
            x_field_coord = str((int(x_coordinate) * 2 )+ 1)
            y_field_coord = y_coordinate
            xy_field_coord = int(y_field_coord + x_field_coord)
            if field[xy_field_coord] == 'X' or field[xy_field_coord] == 'O':
                print('This cell is occupied! Choose another one!')
            else:
                field = field[:xy_field_coord] + token + field[xy_field_coord + 1:]
                print(field)
                can_play = False
                
        
        


if __name__ == "__main__":
    main()
