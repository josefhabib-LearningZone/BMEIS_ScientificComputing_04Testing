import numpy as np

# Tic-Tac-Toe!

# Write a tic tac toe game. We have provided a large part of the Game class below which represents the game board during play.
# It has methods for adding a place to the board (ie. putting down an X or a O in a square) and for checking that the board
# is valid. These need to be implemented by you to pass the tests given to you. Watch out for bugs!


class Game:
    EX = 1
    OH = 2
    PLAYERS = (EX, OH)

    def __init__(self, randomize=False):
        if randomize:
            self.board = np.random.randint(0, 3, size=(3, 3), dtype=int)
        else:
            self.board = np.zeros((3, 3), dtype=int)

    def get_position(self, r, c):
        return self.board[r, c]

    def place(self, r, c, player):
        """Place the player's marker, where `player` is EX or OH, at row `r` and column `c`."""
        # your code here

    def is_valid_board(self):
        """
        Return True if this is a valid game board, it has to check for all the configurations that a valid game would
        be in. Eg. since X and O alternate during play the number of each token on the board has to reflect that.
        """
        # your code here

    def get_winning_player(self):
        """Returns the player number who has won the game, or None if no one has won."""
        # check rows and columns
        for r in range(3):
            row = self.board[r, :]
            col = self.board[:, r]

            for p in self.PLAYERS:
                if all(x == p for x in row):
                    return p

            for p in self.PLAYERS:
                if all(x == p for x in col):
                    return p

        # check diagonals
        for p in self.PLAYERS:
            if all(x == p for x in (self.board[0, 0], self.board[1, 1], self.board[2, 2])):
                return p

    def __str__(self):
        symbols = [".", "X", "O"]

        rows = ["+-------+"]
        for c in range(3):
            row = ["|"]
            for r in range(3):
                row.append(symbols[self.board[r, c]])

            row.append("|")
            rows.append(" ".join(row))

        rows.append("+-------+")

        return "\n".join(rows)


def play_random_game():
    """
    Plays tic tac toe by placing alternating markers randomly on the board until it's full or one of the players wins.
    """
    game = Game()
    positions = list(np.ndindex(3, 3))  # all valid positions on the board
    move = 0

    np.random.shuffle(positions)  # randomly re-arrange the order of positions played

    while move < len(positions) and game.get_winning_player() is None:
        r, c = positions[move]
        game.place(r, c, game.PLAYERS[move % 2])
        move += 1

    return game


if __name__ == "__main__":
    print(play_random_game())
