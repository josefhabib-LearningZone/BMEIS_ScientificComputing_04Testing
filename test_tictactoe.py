"""
These are the pre-defined unit tests. All should pass once your implementation is complete. 
"""

import unittest
from tictactoe import Game, play_random_game


class BasicTests(unittest.TestCase):
    """Basic validity tests for the game board."""

    def test_create(self):
        """Test creating a game object with blank or randomized board."""
        _ = Game(False)  # blank board
        _ = Game(True)  # randomized board

    def test_print(self):
        """Checks that __str__ does something valid, doesn't check string contents."""
        g = Game()
        self.assertGreater(len(str(g)), 0)

    def test_initial_board_valid(self):
        """Ensure the initial blank board is valid."""
        g = Game()
        self.assertTrue(g.is_valid_board())

    def test_single_move(self):
        """Ensure a single move doesn't create an error."""
        g = Game()
        g.place(1, 1, g.EX)

    def test_no_winner_yet(self):
        """Check that no winner exists for the initial blank board."""
        g = Game()
        self.assertIsNone(g.get_winning_player())

    def test_position1(self):
        g = Game()
        g.place(1, 1, g.EX)

        self.assertEqual(g.get_position(1, 1), g.EX)

    def test_random_game(self):
        self.assertIsNotNone(play_random_game())

    def test_random_game_valid(self):
        g = play_random_game()

        self.assertTrue(g.is_valid_board())


class WinnerTests(unittest.TestCase):
    """Check that winners are correctly identified, this doesn't need to check for valid boards, just valid winners."""

    def test_row_win(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(0, 1, g.EX)
        g.place(0, 2, g.EX)
        self.assertEqual(g.get_winning_player(), g.EX)

    def test_col_win(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(1, 0, g.EX)
        g.place(2, 0, g.EX)
        self.assertEqual(g.get_winning_player(), g.EX)

    def test_diag_win1(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(1, 1, g.EX)
        g.place(2, 2, g.EX)
        self.assertEqual(g.get_winning_player(), g.EX)

    def test_diag_win2(self):
        g = Game()
        g.place(0, 2, g.EX)
        g.place(1, 1, g.EX)
        g.place(2, 0, g.EX)
        self.assertEqual(g.get_winning_player(), g.EX)

    def test_row_win_oh(self):
        g = Game()
        g.place(0, 0, g.OH)
        g.place(0, 1, g.OH)
        g.place(0, 2, g.OH)
        self.assertEqual(g.get_winning_player(), g.OH)


class ValidTests(unittest.TestCase):
    """Check for valid and invalid board states."""

    def test_valid_single_move(self):
        g = Game()
        g.place(0, 0, g.EX)
        self.assertTrue(g.is_valid_board())

    def test_invalid_two_moves(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(0, 1, g.EX)
        self.assertFalse(g.is_valid_board())

    def test_valid_three_moves(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(1, 0, g.OH)
        g.place(0, 1, g.EX)
        self.assertTrue(g.is_valid_board())

    def test_invalid_four_moves(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(1, 0, g.OH)
        g.place(0, 1, g.EX)
        g.place(2, 1, g.EX)
        self.assertFalse(g.is_valid_board())

    def test_two_winners(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(0, 1, g.EX)
        g.place(0, 2, g.EX)
        g.place(1, 0, g.OH)
        g.place(1, 1, g.OH)
        g.place(1, 2, g.OH)

        self.assertFalse(g.is_valid_board())

    def test_won_twice_sides(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(0, 1, g.EX)
        g.place(0, 2, g.EX)
        g.place(1, 0, g.EX)
        g.place(2, 0, g.EX)

        g.place(1, 1, g.OH)
        g.place(1, 2, g.OH)
        g.place(2, 1, g.OH)
        g.place(2, 2, g.OH)

        self.assertFalse(g.is_valid_board())

    def test_won_twice_x(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(1, 1, g.EX)
        g.place(2, 2, g.EX)
        g.place(0, 2, g.EX)
        g.place(2, 0, g.EX)

        g.place(0, 1, g.OH)
        g.place(1, 0, g.OH)
        g.place(1, 2, g.OH)
        g.place(2, 1, g.OH)

        self.assertFalse(g.is_valid_board())

    def test_won_twice_plus(self):
        g = Game()
        g.place(0, 1, g.EX)
        g.place(1, 0, g.EX)
        g.place(1, 1, g.EX)
        g.place(1, 2, g.EX)
        g.place(2, 1, g.EX)

        g.place(0, 0, g.OH)
        g.place(0, 2, g.OH)
        g.place(2, 0, g.OH)
        g.place(2, 2, g.OH)

        self.assertFalse(g.is_valid_board())


class ErrorTests(unittest.TestCase):
    """Check error detection."""

    def test_double_move(self):
        g = Game()
        g.place(0, 0, g.EX)

        with self.assertRaises(ValueError):
            g.place(0, 0, g.EX)

    def test_invalid_placement1(self):
        g = Game()

        with self.assertRaises(ValueError):
            g.place(-1, 0, g.EX)

    def test_invalid_placement2(self):
        g = Game()

        with self.assertRaises(ValueError):
            g.place(3, 0, g.EX)

    def test_invalid_position1(self):
        g = Game()

        with self.assertRaises(ValueError):
            g.get_position(-1, 0)

    def test_invalid_position2(self):
        g = Game()

        with self.assertRaises(ValueError):
            g.get_position(3, 0)

    def test_bogus_player(self):
        g = Game()

        with self.assertRaises(ValueError):
            g.place(0, 0, 42)


class TestValidGame(unittest.TestCase):
    """Test fully played out valid games."""

    def test_winner_ex(self):
        g = Game()

        g.place(1, 1, Game.EX)
        self.assertTrue(g.is_valid_board())
        g.place(0, 0, Game.OH)
        self.assertTrue(g.is_valid_board())
        g.place(2, 1, Game.EX)
        self.assertTrue(g.is_valid_board())
        g.place(2, 2, Game.OH)
        self.assertTrue(g.is_valid_board())
        g.place(0, 1, Game.EX)
        self.assertTrue(g.is_valid_board())

        self.assertEqual(g.get_winning_player(), g.EX)

    def test_winner_oh(self):
        g = Game()

        g.place(0, 0, g.OH)
        self.assertTrue(g.is_valid_board())
        g.place(1, 0, g.EX)
        self.assertTrue(g.is_valid_board())
        g.place(0, 1, g.OH)
        self.assertTrue(g.is_valid_board())
        g.place(1, 1, g.EX)
        self.assertTrue(g.is_valid_board())
        g.place(0, 2, g.OH)
        self.assertTrue(g.is_valid_board())

        self.assertEqual(g.get_winning_player(), g.OH)

    def test_winner_disordered(self):
        g = Game()
        g.place(0, 0, g.EX)
        g.place(1, 1, g.EX)
        g.place(2, 2, g.EX)

        g.place(1, 0, g.OH)
        g.place(0, 1, g.OH)

        self.assertTrue(g.is_valid_board())

        self.assertEqual(g.get_winning_player(), g.EX)
