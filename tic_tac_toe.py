import numpy as np


game_map = np.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])
allowed_moves = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

def add_map_values(player_moves: str, player_symbol: str):

    valid_move = True

    allowed_values = ['X', 'Y']
    
    if player_moves in allowed_moves:
        player_moves = list(player_moves)
        if game_map[int(player_moves[0])-1][int(player_moves[1])-1] != allowed_values[0] and game_map[int(player_moves[0])-1][int(player_moves[1])-1] != allowed_values[1]:
            game_map[int(player_moves[0])-1][int(player_moves[1])-1] = player_symbol
            player_moves = ''.join(player_moves)
            allowed_moves.remove(player_moves)
    else:
        valid_move = False
        print('Invalid moves')

    return valid_move


def play_game(turn: int):
    player1_symbol = 'X'
    player2_symbol = 'O'

    if turn % 2 != 0:
        player1_input = input('\nPlayer1 Turn, pick your block position : ')
        if add_map_values(player1_input, player1_symbol) == False:
            play_game(turn)
    else:
        player2_input = input('\nPlayer2 Turn, pick your block position : ')
        if add_map_values(player2_input, player2_symbol) == False:
            play_game(turn)
    
    return(check_winner(turn))
    

def check_winner(player_moves: int):

    end_game = True
    winner = False
    
    win_pattern = [(game_map[0][0], game_map[0][1], game_map[0][2]), 
                   (game_map[1][0], game_map[1][1], game_map[1][2]), 
                   (game_map[2][0], game_map[2][1], game_map[2][2]),  
                   (game_map[0][0], game_map[1][0], game_map[2][0]), 
                   (game_map[0][1], game_map[1][1], game_map[2][1]),  
                   (game_map[0][2], game_map[1][2], game_map[2][2]),  
                   (game_map[0][0], game_map[1][1], game_map[2][2]), 
                   (game_map[0][2], game_map[1][1], game_map[2][0])]
    
    for pattern in win_pattern:
        if pattern[0] == 'X' and pattern[1] == 'X' and pattern[2] == 'X':
            winner = True
            print("The Winner is player 1")
            break
        elif pattern[0] == 'O' and pattern[1] == 'O' and pattern[2] == 'O':
            winner = True
            print("The Winner is player 2")
            break

    if player_moves != 0 and winner:
        pass
    elif winner:
        pass
    else:
        end_game = False

    return end_game    


info = 'can only insert block 11, 12, 13, 21, 22, 23, 31, 32, 33'
info2 = 'first number is refers to row and second number is column'
print(game_map)
print(info)
print(info2)

for i in range(1, 10):
    if play_game(turn=i) != True:
        print(game_map)
        continue
    else:
        print(game_map)
        break
