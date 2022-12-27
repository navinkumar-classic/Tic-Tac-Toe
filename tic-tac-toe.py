import random

m = [['-','-','-'], ['-','-','-'], ['-','-','-']]
d = {(0,0): 0, (0,1): 0, (0,2): 0, (1,0): 0, (1,1): 0, (1,2): 0, (2,0): 0, (2,1): 0, (2,2): 0}

player_symbol = 'X'
ai_symbol = 'O'

def winner(m):
    for row in range(3):
        if m[row][0] == m[row][1] == m[row][2] == 'X' or m[0][row] == m[1][row] == m[2][row] == 'X': return 'X'
        elif m[row][0] == m[row][1] == m[row][2] == 'O' or m[0][row] == m[1][row] == m[2][row] == 'O': return '0'
    if m[0][0] == m[1][1] == m[2][2] == 'X' or m[0][-1] == m[1][-2] == m[2][-3] == 'X': return 'X'
    elif m[0][0] == m[1][1] == m[2][2] == 'O' or m[0][-1] == m[1][-2] == m[2][-3] == 'O': return 'O'
    else: return ''

def printing_the_board(m):
    for row in m:
        print(end = '| ')
        for sym in row:
            print(sym, end = ' | ')
        print()

def player(m,d):
    print('*****PLAYER TURN*****')
    while True:
        t = eval(input('Enter the co-ordinates of ur play (x,y): '))
        if d[t] == 0:
            d[t] = 1
            m[t[0]][t[1]] = player_symbol
            printing_the_board(m)
            break
        else: print('That position is already taken')  
    print()

def ai(m,d):
    print('*****AI TURN*****')
    unplayed_positions = []
    for tup,val in d.items():
        if val == 0: unplayed_positions.append(tup)
    if len(unplayed_positions) > 0: 
        choice = random.choice(unplayed_positions) 
        d[choice] = 1
        m[choice[0]][choice[1]] = ai_symbol
        printing_the_board(m)
        print()
    else: navin = 'hmmm'    

def game(m,d):
    printing_the_board(m)
    while True:
        player(m,d)
        if winner(m) == 'X': 
            print('!!X is the winner!!')
            break
        elif winner(m) == 'O':
            print('!!O is the winner!!')
            break
        ai(m,d)
        if winner(m) == 'X': 
            print('!!X is the winner!!')
            break
        elif winner(m) == 'O':
            print('!!O is the winner!!')
            break  
        for i in d.values():
            if i == 0: break
        else:
            print('!!This game is a draw!!')
            break
                
        
game(m,d)
