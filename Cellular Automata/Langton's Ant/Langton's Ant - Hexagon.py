import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection


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

        # turn 60 degree
        if c == "L1":
            self.dir = (self.dir + 1) % 6

        # turn 120 degree
        if c == "L2":
            self.dir = (self.dir + 2) % 6

        # turn 180 degree
        if c == "U":
            self.dir = (self.dir + 3) % 6

        # turn 240 degree
        if c == "R2":
            self.dir = (self.dir + 4) % 6

        # turn 300 degree
        if c == "R1":
            self.dir = (self.dir + 5) % 6


    def move_forward(self):
        if self.dir == 0:
            self.x = self.x + 1
            self.y = self.y + 0

        if self.dir == 1:
            self.x = self.x + 0
            self.y = self.y + 1

        if self.dir == 2:
            self.x = self.x - 1
            self.y = self.y + 1

        if self.dir == 3:
            self.x = self.x - 1
            self.y = self.y + 0

        if self.dir == 4:
            self.x = self.x + 0
            self.y = self.y - 1

        if self.dir == 5:
            self.x = self.x + 1
            self.y = self.y - 1

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
            radius (int): radius of the hexagonal board
            colors (int): number of the colors 
        """
        self.cells = np.zeros((width, width))
        self.width = width
        self.colors = colors


    def change_color(self, x, y):
        self.cells[x][y] = (self.cells[x][y] + 1) % self.colors


    def plot(self, file_name: str, color_map: str = "Greys", hex_size: float = 5.0):
        self._make_hex_polygons(hex_size)

        # fig, ax = plt.subplots(figsize=(8, 7))
        fig, ax = plt.subplots()  # noqa: RUF059

        collection = PolyCollection(
            self.polygons,
            array=np.array(self.states),
            cmap=color_map,
            edgecolors="none",
            linewidths=0.0001,
            antialiased=False,
        )

        ax.add_collection(collection)
        ax.set_aspect("equal")
        ax.autoscale_view()
        ax.axis("off")

        plt.savefig(f"./figures/{file_name}.png", bbox_inches="tight", pad_inches=0.1, dpi=600)


    def _make_hex_polygons(self, hex_size: float):

        # angle (in degree) of vertices of hexagon
        angles = np.array([30, 90, 150, 210, 270, 330])

        self.polygons = []
        self.centers = []
        self.states = []

        for i in range(self.width):
            for j in range(self.width):
                # shift board center
                x = j - int(self.width / 2)
                y = i - int(self.width / 2)

                # calculate the center of each hexagon
                center_x = (x + y / 2.0) * hex_size
                center_y = y * hex_size * np.sqrt(3) / 2.0
                centers = (center_x, center_y)

                # calculate the vertices of each hexagon
                vertices_x = center_x + np.sqrt(3) / 4.0 * hex_size * np.cos(angles * np.pi / 180)
                vertices_y = center_y + np.sqrt(3) / 4.0 * hex_size * np.sin(angles * np.pi / 180)
                vertices = np.column_stack([vertices_x, vertices_y])

                # append the coordinates and states into lists
                self.centers.append(centers)
                self.polygons.append(vertices)
                self.states.append(self.cells[j, i])





def rule_str_to_list(rule: str) -> list[str]:
    new_rule = []
    for c in rule:
        if c.isnumeric():
            new_rule[-1] = new_rule[-1] + c
        else:
            new_rule.append(c)

    return new_rule

if __name__ == "__main__":
    # define the size of board
    SIZE = 120
    STEP = 10000
    RULE = "R1R2NUR2R1L2"

    N_RULE = rule_str_to_list(RULE)
    NUMBER_OF_COLOR = len(N_RULE)

    # Create objects
    ant = Ant(SIZE)
    board = Board(SIZE, NUMBER_OF_COLOR)

    # Play several steps
    for _ in range(STEP):
        try:
            state = int(board.cells[ant.x, ant.y])
            ant.turn(N_RULE[state])
            board.change_color(ant.x, ant.y)
            ant.move_forward()
        except IndexError:
            break

    # plot the board
    file_name = f"Hexagon ({RULE})"
    board.plot(file_name, "Blues")