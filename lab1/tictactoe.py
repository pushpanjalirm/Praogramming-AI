import math

# Create the board as a list of 9 spaces
# Positions:
#  0 | 1 | 2
# ---+---+---
#  3 | 4 | 5
# ---+---+---
#  6 | 7 | 8

def print_board(board):
    """Print the board in a nice format."""
    print()
    for row in range(3):
        print(" " + board[row*3] + " | " + board[row*3+1] + " | " + board[row*3+2])
        if row < 2:
            print("---+---+---")
    print()

def check_winner(board):
    """Return 'X', 'O', 'tie', or None (game still going)."""
    # All 8 winning lines (rows, columns, diagonals)
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]

    for line in win_lines:
        a, b, c = line
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]  # 'X' or 'O' wins

    if " " not in board:
        return "tie"

    return None  # game not finished

def minimax(board, depth, is_maximizing):
    """
    Recursively evaluate the board.
    AI is 'O' (maximizing player), Human is 'X' (minimizing player).
    Returns the best score for the current player.
    """
    result = check_winner(board)

    # Base cases: game is over
    if result == "O":
        return 10 - depth    # AI wins (prefer faster wins)
    elif result == "X":
        return depth - 10    # Human wins (prefer slower losses)
    elif result == "tie":
        return 0

    if is_maximizing:
        # AI's turn - try to get the highest score
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "  # undo the move
                best_score = max(best_score, score)
        return best_score
    else:
        # Human's turn - try to get the lowest score
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "  # undo the move
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    """Return the best move (0-8) for the AI ('O')."""
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "  # undo
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    """Main game loop."""
    board = [" "] * 9

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', the AI is 'O'.")
    print("Positions are numbered 0-8:")
    print(" 0 | 1 | 2")
    print("---+---+---")
    print(" 3 | 4 | 5")
    print("---+---+---")
    print(" 6 | 7 | 8")

    current = "X"  # Human goes first

    while True:
        print_board(board)

        if current == "X":
            # Human's turn
            try:
                move = int(input("Your move (0-8): "))
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move! Try again.")
                    continue
            except ValueError:
                print("Please enter a number 0-8.")
                continue
            board[move] = "X"
        else:
            # AI's turn
            print("AI is thinking...")
            move = best_move(board)
            board[move] = "O"
            print(f"AI chose position {move}")

        # Check if game is over
        result = check_winner(board)
        if result:
            print_board(board)
            if result == "tie":
                print("It's a tie!")
            elif result == "X":
                print("You win! 🎉")
            else:
                print("AI wins! 🤖")
            break

        # Switch turns
        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    play_game()
