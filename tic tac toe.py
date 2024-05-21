import random

def print_board(board):
    """Function to print the Tic Tac Toe board"""
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board):
    """Function to check if there is a winner"""
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True, row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True, board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True, board[0][2]
    return False, None

def is_board_full(board):
    """Function to check if the board is full"""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def player_move(board, symbol):
    """Function for player's move"""
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = symbol
                break
            else:
                print("Invalid move! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def computer_move(board, symbol):
    """Function for computer's move"""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = symbol
            break

def play_game():
    """Function to play the game"""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    players = ['X', 'O']
    while True:
        for player in players:
            print(f"Player {player}'s turn:")
            if player == 'X':
                player_move(board, player)
            else:
                computer_move(board, player)
            print_board(board)
            is_winner, winner = check_winner(board)
            if is_winner:
                print(f"Player {winner} wins!")
                return
            if is_board_full(board):
                print("It's a tie!")
                return

play_game()
