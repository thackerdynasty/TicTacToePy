from square import Square

class Board:
    _board = [] # 2d array [[1,2,3],[4,5,6]] for all the squares
    def __init__(self):
        for i in range(3):
            self._board.append([])
            for j in range(3):
                self._board[i].append(Square())

    def print_board(self):
        for i in range(3):
            print(" " + self._board[i][0].get_symbol() + " | " + self._board[i][1].get_symbol() + " | " + self._board[i][2].get_symbol())
            if i < 2:
                print("---|---|---")

    def get_square(self, square):
        if 4 > square > 0:
            return self._board[1][square - 1].get_symbol()
        elif 7 > square > 3:
            return self._board[2][square - 4].get_symbol()
        elif 10 > square > 6:
            return self._board[3][square - 7].get_symbol()
        else:
            return "Invalid square."

    def set_square(self, square, player):
        if 4 > square > 0:
            row = 0
            col = square - 1
            if self._board[row][col].get_symbol() == " ":
                self._board[row][col].set_symbol(player)
                return True
            else:
                print("Square is already taken.")
                return False
        elif 7 > square > 3:
            row = 1
            col = square - 4
            if self._board[row][col].get_symbol() == " ":
                self._board[row][col].set_symbol(player)
                return True
            else:
                print("Square is already taken.")
                return False
        elif 10 > square > 6:
            row = 2
            col = square - 7
            if self._board[row][col].get_symbol() == " ":
                self._board[row][col].set_symbol(player)
                return True
            else:
                print("Square is already taken.")
                return False
        else:
            print("Invalid square.")
            return False

    def check_win(self):
        for i in range(3):
            # check rows
            if (self._board[i][0].get_symbol() == self._board[i][1].get_symbol()
                    and self._board[i][1].get_symbol() == self._board[i][2].get_symbol()
                    and self._board[i][0].get_symbol() != " "):
                return True

            # check columns
            if (self._board[0][i].get_symbol() == self._board[1][i].get_symbol()
                    and self._board[1][i].get_symbol() == self._board[2][i].get_symbol()
                    and self._board[0][i].get_symbol() != " "):
                return True

        # check diagonals
        if (self._board[0][0].get_symbol() == self._board[1][1].get_symbol()
                and self._board[1][1].get_symbol() == self._board[2][2].get_symbol()
                and self._board[0][0].get_symbol() != " "):
            return True
        if (self._board[0][2].get_symbol() == self._board[1][1].get_symbol()
                and self._board[1][1].get_symbol() == self._board[2][0].get_symbol()
                and self._board[0][2].get_symbol() != " "):
            return True

        return False

    # call ONLY AFTER calling check_win()
    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self._board[i][j].get_symbol() == " ":
                    return False

        return True

    def reset(self):
        for i in range(3):
            for j in range(3):
                self._board[i][j].set_symbol(" ")