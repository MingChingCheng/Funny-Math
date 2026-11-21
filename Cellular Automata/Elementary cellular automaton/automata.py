import os

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


def rule(n: int) -> list[int]:
    """
    Transfer a decimal number (0~255) into 8 bits binary code
    Example:
        input: 90
        output: [0, 1, 0, 1, 1, 0, 1, 0]
    """
    binary = []

    for _ in range(8):
        if n % 2 == 0:
            binary.append(0)
            n = int(n / 2)
        else:
            binary.append(1)
            n = int((n-1) / 2)

    binary.reverse()
    return binary



def seed(width: int, random: bool = False) -> list[int]:
    """
    Generate a seed for Elementary cellular automata
    """
    seed = []

    if random is False:
        for i in range(width):
            if i == int((width-1) / 2):
                seed.append(1)
            else:
                seed.append(0)

    else:
        for i in range(width):
            seed.append(np.random.randint(0, 2))

    return seed



def automata(a0: int, a1: int, a2: int, rule_number: int) -> int:
    """
    Example: Rule 90
    | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    |  0  |  1  |  0  |  1  |  1  |  0  |  1  |  0  |
    """
    RULE = rule(rule_number)
    previous_state = 7 - int(a0 * 4 + a1 * 2 + a2 * 1)
    return RULE[previous_state]


def cellular_automata(width: int, height: int, seed: list[int], rule_number: int) -> np.ndarray:

    # Create a 2D array, filled with 0
    cells = np.zeros((height, width))

    # Set first row as seed
    cells[0] = seed

    # Do the automata
    print("Precessing row:")
    for j in tqdm(range(1, height)):
        for i in range(1, width-1):
            # if i == 0:
            #     a0 = 0
            # else:
            #     a0 = cells[j-1, i-1]

            # a1 = cells[j-1, i]

            # if i == (width-1):
            #     a2 = 0
            # else:
            #     a2 = cells[j-1, i+1]


            a0 = cells[j-1, i-1]
            a1 = cells[j-1, i]
            a2 = cells[j-1, i+1]

            cells[j, i] = automata(a0, a1, a2, rule_number)

    return cells



def save_fig(cells: np.ndarray, rule_number: int, path: str) -> None:
    """
    Since the edge of cells will influence some unwanted effect
    Because we assume all the edge part is '0'

    Here, only render the half part of all cells
    """

    # Plot the diagram
    print("Saving figure ...")

    # Check the path is exist
    if os.path.exists(path) is False:
        os.mkdir(path)

    # Define path to save the file
    file_name = f"Rule_{rule_number}.png"
    path = os.path.join(path, file_name)

    # Set the figure size
    cell_width = cells.shape[1]
    cell_height = cells.shape[0]
    fig_w, fig_h = figure_size(cell_width, cell_height)
    plt.figure(figsize=(fig_w, fig_h))

    # slice the cells
    w_start = int(np.floor(cell_width / 4))
    w_end = int(np.floor(cell_width * 3 / 4) + 1)
    h_start = 0
    h_end = int(cell_height / 2) + 1
    cells_sliced = cells[h_start:h_end, w_start:w_end]

    # Saving the file
    plt.imshow(cells_sliced, cmap="Greys")
    plt.axis("off")
    plt.savefig(path, bbox_inches="tight", pad_inches=0.1, dpi=300)
    plt.clf()     # clear current figure
    plt.close()   # close current figure

    
def figure_size(width: int, height: int) -> tuple:
    # set figure dpi=300
    h = np.ceil(height / 30)
    w = np.ceil(width / 30)

    return (w, h)


if __name__ == "__main__":

    # Define the canvas
    WIDTH = 513
    HEIGHT = 256
    RANDOM_SEED = False

    # Create a seed
    my_seed = seed(WIDTH, RANDOM_SEED)

    # Calculate and plot/save cells
    for rule_number in range(256):
        print(f"Rule: {rule_number}")
        cells = cellular_automata(WIDTH, HEIGHT, my_seed, rule_number)
        save_fig(cells, rule_number, "./figures/1_cell")
