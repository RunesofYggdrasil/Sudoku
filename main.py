from sudokusetup import load_board
from sudoku import SudokuGame

def main():
    board = load_board()
    game = SudokuGame(board)
    game.play_game()

if __name__ == "__main__":
    main()

# ~Shamar Richards

# Key Changes & Comments:
# 1. **get_board function**: This function reads from the file "sudokuboards.txt" and retrieves the board based on the board number 'n'.
# 2. **File Handling**: Proper file handling is used to read the text file, split the rows, and extract the board into a 2D list.
# 3. **Parsing the Sudoku Grid**: The function ensures that only numeric values are added to the board and skips over any separators.
# 4. **Sudoku Class Integration**: The board data is passed into the `Sudoku` class, which provides methods like `set_index`, `undo`, and `redo` for interacting with the puzzle.
# 5. **Gameplay Logic**: I implemented some basic gameplay logic to set values, undo actions, and redo them, along with tracking changes.
# 6. **Error Handling**: The board is correctly parsed, and I ensured that only valid numeric values are processed from the file.
# 7. **README**: Added instructions for installation.