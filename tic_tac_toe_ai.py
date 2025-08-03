import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def check_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(brd[i] == player for i in condition):
            return True
    return False

def is_draw():
    return ' ' not in board

def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'X'
                break
        print("Invalid move. Try again.")

def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    while True:
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

main()
