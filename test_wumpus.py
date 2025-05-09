import unittest
from unittest.mock import patch
from Wumpus import HuntTheWumpusGrid, Cell


class TestHuntTheWumpus(unittest.TestCase):
    def setUp(self):
        # Create a 5x5 grid for testing
        self.game = HuntTheWumpusGrid(5, 5)

    def test_player_initial_position(self):
        # Test that the player starts at (0, 0)
        self.assertEqual(self.game.player_position, (0, 0))
        self.assertTrue(self.game.grid[0][0].isplayer)

    def test_move_player(self):
        # Test player movement
        self.game.move_player("down")
        self.assertEqual(self.game.player_position, (1, 0))
        self.assertTrue(self.game.grid[1][0].isplayer)
        self.assertFalse(self.game.grid[0][0].isplayer)

        self.game.move_player("right")
        self.assertEqual(self.game.player_position, (1, 1))
        self.assertTrue(self.game.grid[1][1].isplayer)

    def test_invalid_move(self):
        # Test invalid movement (out of bounds)
        with patch("builtins.print") as mock_print:
            self.game.move_player("up")  # Can't move up from (0, 0)
            mock_print.assert_called_with("Invalid move. Try again.")
            self.assertEqual(self.game.player_position, (0, 0))

    def test_wumpus_collision(self):
        # Place the Wumpus at a known position
        self.game.grid[2][2].haswumpus = True
        self.game.player_position = (2, 1)
        self.game.move_player("right")
        self.assertTrue(self.game.game_over)

    def test_pit_collision(self):
        # Place a pit at a known position
        self.game.grid[3][3].haspit = True
        self.game.player_position = (3, 2)
        self.game.move_player("right")
        self.assertTrue(self.game.game_over)

    def test_near_wumpus_warning(self):
        # Place the Wumpus near the player
        self.game.grid[1][1].haswumpus = True
        self.game.player_position = (1, 0)
        with patch("builtins.print") as mock_print:
            self.game.move_player("right")
            mock_print.assert_any_call("It stinks nearby!")

    def test_near_pit_warning(self):
        # Place a pit near the player
        self.game.grid[2][2].haspit = True
        self.game.player_position = (2, 1)
        with patch("builtins.print") as mock_print:
            self.game.move_player("right")
            mock_print.assert_any_call("You feel a breeze!")

    def test_shoot_arrow_hit(self):
        # Place the Wumpus at a known position
        self.game.grid[2][2].haswumpus = True
        self.game.player_position = (2, 0)
        with patch("builtins.print") as mock_print:
            self.game.shoot_arrow("right")
            mock_print.assert_any_call("You shot the Wumpus! You win!")
            self.assertFalse(self.game.wumpus_alive)
            self.assertTrue(self.game.game_over)

    def test_shoot_arrow_miss(self):
        # Place the Wumpus at a known position
        self.game.grid[2][2].haswumpus = True
        self.game.player_position = (0, 0)
        with patch("builtins.print") as mock_print:
            self.game.shoot_arrow("right")
            mock_print.assert_any_call("You missed! The Wumpus is still alive!")
            self.assertTrue(self.game.wumpus_alive)

    def test_shoot_arrow_invalid_direction(self):
        # Test shooting in an invalid direction
        with patch("builtins.print") as mock_print:
            self.game.shoot_arrow("diagonal")
            mock_print.assert_any_call("Invalid direction. Try again.")


if __name__ == "__main__":
    unittest.main()