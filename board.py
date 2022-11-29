class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_board(self):
        top_row = f' {self.board[0]} | {self.board[1]} | {self.board[2]} '
        middle_row = f' {self.board[3]} | {self.board[4]} | {self.board[5]} '
        bottom_row = f' {self.board[6]} | {self.board[7]} | {self.board[8]} '
        line = '-----------'
        print(top_row)
        print(line)
        print(middle_row)
        print(line)
        print(bottom_row)

    def check_if_three_symbols_connect(self, placement):
        """Check if there are three symbols connecting"""
        place = int(placement) - 1


        if place in (0, 3, 6):  # left column
            if self.board[place] == self.board[place + 1] == self.board[place + 2]:  # check horizontally ->
                return True
        if place in (2, 5, 8):  # right column
            if self.board[place] == self.board[place - 1] == self.board[place - 2]:  # check horizontally <-
                return True
        if place in (0, 1, 2):  # top row
            if self.board[place] == self.board[place + 3] == self.board[place + 6]:  # check vertically downwards
                return True
        if place in (6, 7, 8):  # bottom row
            if self.board[place] == self.board[place - 3] == self.board[place - 6]:  # check vertically upwards
                return True
        if place in (3, 4, 5):  # middle row
            if self.board[place] == self.board[place - 3] == self.board[place + 3]:  # check above and below
                return True
        if place in (1, 4, 7):  # middle row
            if self.board[place] == self.board[place - 1] == self.board[place + 1]:  # check left and right
                return True
        if place in (0, 2, 6, 8):  # diagonal corners
            if place == 0:
                if self.board[place] == self.board[place + 4] == self.board[place + 8]:  # top left to bottom right
                    return True
            elif place == 8:
                if self.board[place] == self.board[place - 4] == self.board[place - 8]:  # bottom right to top left
                    return True
            elif place == 2:
                if self.board[place] == self.board[place + 2] == self.board[place + 4]:  # top right to bottom left
                    return True
            elif place == 6:
                if self.board[place] == self.board[place - 2] == self.board[place - 4]:  # bottom left to top right
                    return True
        if place == 4:  # center
            if self.board[place] == self.board[place - 4] == self.board[place + 4] or \
                    self.board[place] == self.board[place - 2] == self.board[place + 2]:
                return True
