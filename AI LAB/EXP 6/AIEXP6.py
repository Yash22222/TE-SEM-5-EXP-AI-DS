# Define the game board and players
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player1 = 'X'
player2 = 'O'

# Function to print the current state of the board
def print_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}\n---------\n{board[3]} | {board[4]} | {board[5]}\n---------\n{board[6]} | {board[7]} | {board[8]}\n')

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (a tie)
def is_board_full(board):
    return ' ' not in board

# Min-Max algorithm with alpha-beta pruning
def minimax(board, depth, maximizing_player):
    if check_winner(board, player1):
        return -1
    if check_winner(board, player2):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player2
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player1
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Find the best move for the AI (player2)
def find_best_move(board):
    best_move = -1
    best_eval = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = player2
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    print_board(board)

    # Player1's turn
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player1
    else:
        print("Invalid move! Try again.")
        continue

    # Check if Player1 wins or it's a tie
    if check_winner(board, player1):
        print_board(board)
        print("Player1 (X) wins!")
        break
    if is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break

    # Player2's turn (AI)
    best_move = find_best_move(board)
    board[best_move] = player2

    # Check if Player2 wins or it's a tie
    if check_winner(board, player2):
        print_board(board)
        print("Player2 (O) wins!")
        break
    if is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break
