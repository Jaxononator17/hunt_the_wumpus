import random


class Cell:
    def __init__(self):
        self.haswumpus = False
        self.haspit = False
        self.hasgold = False
        self.isplayer = False

    def __str__(self):
        if self.isplayer:
            return "P"
        elif self.haswumpus:
            return "W"
        elif self.haspit:
            return "O"
        elif self.hasgold:
            return "G"
        else:
            return "."


class HuntTheWumpusGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.player_position = (0, 0)
        self.game_over = False

        self.place_player()
        self.place_wumpus()

    def place_player(self):
        x, y = self.player_position
        self.grid[x][y].is_player = True

    def place_wumpus(self):
        """
        Randomly place the Wumpus in a cell that is not the player's starting position.
        """
        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if (x, y) != self.player_position:
                self.grid[x][y].haswumpus = True
                break

    def move_player(self, direction):
        """
        Moves the player in the specified direction (up, down, left, right).
        Displays the new coordinates after the move and checks for Wumpus collision.
        """
        if self.game_over:
            print("Game over! You cannot move.")
            return

        x, y = self.player_position
        self.grid[x][y].is_player = False

        if direction == "up" and x > 0:
            x -= 1
        elif direction == "down" and x < self.rows - 1:
            x += 1
        elif direction == "left" and y > 0:
            y -= 1
        elif direction == "right" and y < self.cols - 1:
            y += 1
        else:
            print("Invalid move. Try again.")
            return

        self.player_position = (x, y)
        self.grid[x][y].is_player = True

        # Display the new coordinates
        print(f"Player moved to coordinates: ({x}, {y})")

        # Check for Wumpus collision
        if self.grid[x][y].haswumpus:
            print("You encountered the Wumpus! Game over!")
            self.game_over = True
        else:
            # Check for proximity to the Wumpus
            if self.is_near_wumpus(x, y):
                print("It stinks nearby!")

    def is_near_wumpus(self, x, y):
        """
        Checks if the player is adjacent to the Wumpus.
        """
         # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if self.grid[nx][ny].haswumpus:
                    return True
        return False


def main():
    # Create a 5x5 grid for the game
    game = HuntTheWumpusGrid(5, 5)

    # Game loop
    while not game.game_over:
        # Display player position
        print(f"Player is at {game.player_position}.")
        # Get player input
        move = input("Enter your move (up, down, left, right): ").strip().lower()
        game.move_player(move)


main()