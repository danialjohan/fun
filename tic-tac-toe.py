board = [' ' for _ in range(9)]

def print_board():
    row1 = '|'.join([board[i] for i in range(3)])
    row2 = '|'.join([board[i] for i in range(3, 6)])
    row3 = '|'.join([board[i] for i in range(6, 9)])
    print(f'{row1}\n{"-" * 5}\n{row2}\n{"-" * 5}\n{row3}')

def is_winner(player):
    return (board[0] == board[1] == board[2] == player or
            board[3] == board[4] == board[5] == player or
            board[6] == board[7] == board[8] == player or
            board[0] == board[3] == board[6] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player)

def is_draw():
    return ' ' not in board

def get_player_move(player):
    valid_moves = [i for i in range(9) if board[i] == ' ']
    move = None
    while move not in valid_moves:
        move = int(input(f'Player {player}, enter a valid move (0-8): '))
    return move

def play_game():
    print_board()
    player = 'X'
    while not is_winner(player) and not is_draw():
        move = get_player_move(player)
        board[move] = player
        print_board()
        player = 'O' if player == 'X' else 'X'
    if is_winner(player):
        print(f'Player {player} wins!')
    else:
        print('It is a draw!')

play_game()
