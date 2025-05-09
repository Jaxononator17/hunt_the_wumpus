import random


##implementing cell class like i used for my ant colony
class Cell:
    def init(slef):

        self.haswumpus = False

        self.haspit = False

        self.hasgold = False

        self.isplayer = False

    def str(self):

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

        self.place_player()

    def place_player(self):

        x, y = self.player_position

        self.grid[x][y].is_player = True

    def move_player(self, direction):
        """
        Moves the player in the specified direction (up, down, left, right).
        Displays the new coordinates after the move.
        """
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

        self.player_position = (x, y)

        self.grid[x][y].is_player = True

        # Display the new coordinates
        print(f"Player moved to coordinates: ({x}, {y})")


##I am going to turn this into my first test case after this push to ensure that the playter can mover after every test before pushing
def main(): 

    # Create a 5x5 grid for the game
    game = HuntTheWumpusGrid(5, 5)

    # Simulate player movement
    game.move_player("down")

    game.move_player("right")
    
    game.move_player("up")