from tictactoe import TicTacToe

# Simulate AI (O) vs Random (X) for a non-interactive demo
import random

def simulate():
    game = TicTacToe()
    # Let X be random player, O be minimax AI
    while not game.game_over:
        if game.current_player == 'X':
            moves = game.available_moves()
            move = random.choice(moves)
            game.make_move(move, 'X')
            print(f"X (random) chooses {move}")
        else:
            move = game.ai_move()
            game.make_move(move, 'O')
            print(f"O (AI) chooses {move}")
        res = game.check_winner()
        if res:
            game.game_over = True
            game.winner = res
            game.print_board()
            if res == 'Draw':
                print('Result: Draw')
            else:
                print(f'Result: {res} wins')
        else:
            game.current_player = 'O' if game.current_player == 'X' else 'X'

if __name__ == '__main__':
    simulate()
