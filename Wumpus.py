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
        self.wumpus_alive = True

        self.place_player()
        self.place_wumpus()
        self.place_pits()

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

    def place_pits(self, num_pits=3):
        """
        Randomly place pits in the grid, avoiding the player's starting position and the Wumpus.
        """
        for _ in range(num_pits):
            while True:
                x = random.randint(0, self.rows - 1)
                y = random.randint(0, self.cols - 1)
                if (x, y) != self.player_position and not self.grid[x][y].haswumpus:
                    self.grid[x][y].haspit = True
                    break

    def move_player(self, direction):
        """
        Moves the player in the specified direction (up, down, left, right).
        Displays the new coordinates after the move and checks for hazards.
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

        # Check for hazards
        if self.grid[x][y].haswumpus:
            print("You encountered the Wumpus! Game over!")
            self.game_over = True
        elif self.grid[x][y].haspit:
            print("You fell into a pit! Game over!")
            self.game_over = True
        else:
            # Check for proximity to hazards
            if self.is_near_wumpus(x, y):
                print("It stinks nearby!")
            if self.is_near_pit(x, y):
                print("You feel a breeze!")

    def shoot_arrow(self, direction):
        """
        Shoots an arrow in the specified direction (up, down, left, right).
        If the arrow hits the Wumpus, the Wumpus is killed, and the player wins.
        """
        if not self.wumpus_alive:
            print("The Wumpus is already dead!")
            return

        x, y = self.player_position

        if direction == "up":
            for i in range(x - 1, -1, -1):
                if self.grid[i][y].haswumpus:
                    print("You shot the Wumpus! You win!")
                    self.wumpus_alive = False
                    self.game_over = True
                    return
        elif direction == "down":
            for i in range(x + 1, self.rows):
                if self.grid[i][y].haswumpus:
                    print("You shot the Wumpus! You win!")
                    self.wumpus_alive = False
                    self.game_over = True
                    return
        elif direction == "left":
            for j in range(y - 1, -1, -1):
                if self.grid[x][j].haswumpus:
                    print("You shot the Wumpus! You win!")
                    self.wumpus_alive = False
                    self.game_over = True
                    return
        elif direction == "right":
            for j in range(y + 1, self.cols):
                if self.grid[x][j].haswumpus:
                    print("You shot the Wumpus! You win!")
                    self.wumpus_alive = False
                    self.game_over = True
                    return
        else:
            print("Invalid direction. Try again.")
            return

        print("You missed! The Wumpus is still alive!")

    def is_near_wumpus(self, x, y):
        """
        Checks if the player is adjacent to the Wumpus.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if self.grid[nx][ny].haswumpus:
                    return True
        return False

    def is_near_pit(self, x, y):
        """
        Checks if the player is adjacent to a pit.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if self.grid[nx][ny].haspit:
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
        action = input("Enter your action (move/shoot): ").strip().lower()
        if action == "move":
            move = input("Enter your move (up, down, left, right): ").strip().lower()
            game.move_player(move)
        elif action == "shoot":
            direction = input("Enter direction to shoot (up, down, left, right): ").strip().lower()
            game.shoot_arrow(direction)
        else:
            print("Invalid action. Try again.")


if __name__ == "__main__":
    main()
