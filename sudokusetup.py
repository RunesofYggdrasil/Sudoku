import random

def load_board(filename="sudokuboards.txt"):
    """Loads a random Sudoku board from the file containing multiple boards."""
    with open(filename, "r") as f:
        lines = f.readlines()

    # Split the lines into individual boards
    boards = []
    current_board = []

    for line in lines:
        if line.strip() == "":
            if current_board:
                boards.append(current_board)
                current_board = []
        elif "|" in line or "-" in line:
            continue
        else:
            row = [int(x) if x.isdigit() else 0 for x in line.split()]
            current_board.append(row)

    if current_board:
        boards.append(current_board)

    # Choose a random board from the list of boards
    chosen_board = random.choice(boards)
    print("A new Sudoku board has been loaded!")
    return chosen_board
