import matplotlib.pyplot as plt
import numpy as np


class Ant:
    def __init__(self, width):
        self.coordinate_max = width
        self.x = int(width / 2)
        self.y = int(width / 2)
        self.dir = 0


    def turn(self, c: str):
        # turn nothing
        if c == "N":
            pass

        # turn left
        if c == "L":
            self.dir = (self.dir + 1) % 4

        # turn back
        if c == "U":
            self.dir = (self.dir + 2) % 4

        # turn right
        if c == "R":
            self.dir = (self.dir + 3) % 4

    def move_forward(self):
        # Note: the plus or minus are depending on the definition of 2D array
        # move up
        if self.dir == 0:
            self.y = self.y - 1

        # move left
        if self.dir == 1:
            self.x = self.x - 1

        # move down
        if self.dir == 2:
            self.y = self.y + 1

        # move right
        if self.dir == 3:
            self.x = self.x + 1

        # check if ant is out of board
        if (
            (self.x >= self.coordinate_max)
            or (self.y >= self.coordinate_max)
            or (self.x <= 0)
            or self.y <= 0
        ):
            raise IndexError(f"Ant is moving out of board at ({self.x}, {self.y})")





class Board:
    def __init__(self, width: int, colors: int):
        """
        Args:
            width (int): define the size of the board
            colors (int): define the number of colors
        """
        self.width = width
        self.cells = np.zeros((width, width))
        self.colors = colors

    def change_color(self, x, y):
        self.cells[x][y] = (self.cells[x][y] + 1) % self.colors
    
    def plot(self, file_name: str, color_map: str = "Greys"):
        plt.imshow(self.cells, cmap=color_map)
        plt.axis("off")
        plt.savefig(f"./figures/{file_name}.png", bbox_inches="tight", pad_inches=0.1, dpi=300)

 


if __name__ == "__main__":

    # define the size of board
    SIZE = 200
    STEP = 1000000
    RULE = "LRRRRRLLR"
    NUMBER_OF_COLOR = len(RULE)

    # Create objects
    ant = Ant(SIZE)
    board = Board(SIZE, NUMBER_OF_COLOR)

    # Play several steps
    for _ in range(STEP):

        try:
            state = int(board.cells[ant.x][ant.y])
            ant.turn(RULE[state])
            board.change_color(ant.x, ant.y)
            ant.move_forward()
        except IndexError as e:
            print(e)
            break

    # plot the board
    file_name = f"Square ({RULE})"
    board.plot(file_name, "rainbow")
        
