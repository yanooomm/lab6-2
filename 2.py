field=[['1','2','3'],
       ['4','5','6'],
       ['7','8','9']]

def print_field():
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            print(field[i][j], end = ' ')
        print()
    
def PlayerStep():
    step = int(input('Введите номер свободной ячейки: '))
    return step

def win():
    if field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X':
        return True
    elif field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X':
        return True
    elif field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X':
        return True
    elif field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X':
        return True
    elif field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X':
        return True
    elif field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X':
        return True
    elif field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X':
        return True
    elif field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X':
        return True
    
    elif field[0][0] == 'O' and field[0][1] == 'O' and field[0][2] == 'O':
        return True
    elif field[1][0] == 'O' and field[1][1] == 'O' and field[1][2] == 'O':
        return True
    elif field[2][0] == 'O' and field[2][1] == 'O' and field[2][2] == 'O':
        return True
    elif field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O':
        return True
    elif field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O':
        return True
    elif field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O':
        return True
    elif field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O':
        return True
    elif field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O':
        return True
    else:
        return False

def PlaceEmpty(place):
    if place == 1:
        if field[0][0] not in 'XO':
            return True
        else:
            return False
    if place == 2:
        if field[0][1] not in 'XO':
            return True
        else:
            return False
    if place == 3:
        if field[0][2] not in 'XO':
            return True
        else:
            return False
    if place == 4:
        if field[1][0] not in 'XO':
            return True
        else:
            return False
    if place == 5:
        if field[1][1] not in 'XO':
            return True
        else:
            return False
    if place == 6:
        if field[1][2] not in 'XO':
            return True
        else:
            return False
    if place == 7:
        if field[2][0] not in 'XO':
            return True
        else:
            return False
    if place == 8:
        if field[2][1] not in 'XO':
            return True
        else:
            return False
    if place == 9:
        if field[2][2] not in 'XO':
            return True
        else:
            return False

def switch_move(move: int, key: str):
    if move == 1:
        field[0][0] = key
    elif move == 2:
        field[0][1] = key
    elif move == 3:
        field[0][2] = key
    elif move == 4:
        field[1][0] = key
    elif move == 5:
        field[1][1] = key
    elif move == 6:
        field[1][2] = key
    elif move == 7:
        field[2][0] = key
    elif move == 8:
        field[2][1] = key
    elif move == 9:
        field[2][2] = key
        
def switch_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

move = 'X'
while not(win()):
    print_field()
    place = PlayerStep()
    if PlaceEmpty(place):
        switch_move(place, move)
        move = switch_player(move)
    if field[0][0] in 'XO' and field[0][1] in 'XO' and field[0][2] in 'XO' and field[1][0] in 'XO' and field[1][1] in 'XO' and field[1][2] in 'XO' and field[2][0] in 'XO' and field[2][1] in 'XO' and field[2][2] in 'XO':
        break
print_field()
if win():
    print('Победа игрока ', switch_player(move), '!')
else:
    print('Ничья!')


'''
1 2 3 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 1
X 2 3 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 2
X O 3 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 3
X O X 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 4
X O X 
O 5 6 
7 8 9 
Введите номер свободной ячейки: 5
X O X 
O X 6 
7 8 9 
Введите номер свободной ячейки: 6
X O X 
O X O 
7 8 9 
Введите номер свободной ячейки: 7
X O X 
O X O 
X 8 9 
Победа игрока  X !
'''

'''
1 2 3 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 1
X 2 3 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 2
X O 3 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 3
X O X 
4 5 6 
7 8 9 
Введите номер свободной ячейки: 5
X O X 
4 O 6 
7 8 9 
Введите номер свободной ячейки: 4
X O X 
X O 6 
7 8 9 
Введите номер свободной ячейки: 6
X O X 
X O O 
7 8 9 
Введите номер свободной ячейки: 8
X O X 
X O O 
7 X 9 
Введите номер свободной ячейки: 7
X O X 
X O O 
O X 9 
Введите номер свободной ячейки: 9
X O X 
X O O 
O X X 
Ничья!
'''