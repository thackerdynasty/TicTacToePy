import os

from board import Board
import subprocess

def game(board, player, game_won, is_tie):
    while not game_won or not is_tie:
        print(f"Player {player}'s turn.")
        square = input("Type the square number you would like to place your symbol on: (type r to restart)\n")
        if square == "r":
            clear_console()
            board.reset()
            board.print_board()
            continue
        square = int(square)
        success = board.set_square(square, player)
        if not success:
            clear_console()
            board.print_board()
            board.set_square(square, player)
            continue
        game_won = board.check_win()
        is_tie = board.check_tie()
        if game_won:
            clear_console()
            board.print_board()
            print(f"Player {player} wins!")
            break
        elif is_tie:
            clear_console()
            board.print_board()
            print("It's a tie!")
            break
        clear_console()
        board.print_board()
        player = "O" if player == "X" else "X"

def main():
    clear_console()
    print("Welcome to the Tic Tac Toe Game! Press enter to begin.")
    input()
    current_player = "X"
    game_won = False
    is_tie = False
    clear_console()
    board = Board()
    board.print_board()
    game(board, current_player, game_won, is_tie)
    play_again = input("Would you like to play again? (y/n)\n")
    if play_again.lower() == "y":
        board.reset()
        main()
    elif play_again.lower() == "n":
        print("Thanks for playing!")
    else:
        print("Invalid input. Ending game.")


def clear_console():
    if os.environ.get("TERM") is not None:
        subprocess.run(["clear"])


if __name__ == "__main__":
    main()