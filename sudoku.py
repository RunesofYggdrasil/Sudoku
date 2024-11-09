import os

class SudokuGame:
    def __init__(self, board=None, board_file="sudokuboards.txt", completed_file="completed_game.txt", saved_file="saved_game.txt"):
        self.board_file = board_file
        self.completed_file = completed_file
        self.saved_file = saved_file
        self.board = board
        self.difficulty_levels = self.get_difficulty_levels()
        print("Sudoku game initialized.")

    def get_difficulty_levels(self):
        """Scans the board file for available difficulties and board numbers."""
        if not os.path.exists(self.board_file):
            print(f"{self.board_file} not found. No difficulty levels available.")
            return {}

        difficulties = {}
        with open(self.board_file, "r") as f:
            lines = f.readlines()

        current_difficulty = None
        board_count = 0
        for line in lines:
            if line.startswith("Board #"):
                board_count += 1
                # Extract difficulty from the board title, e.g., "Board #1: Beginner Puzzle"
                difficulty = line.split(":")[1].strip() if ":" in line else f"Board {board_count}"
                if difficulty not in difficulties:
                    difficulties[difficulty] = []
                difficulties[difficulty].append(board_count)

        return difficulties

    def select_difficulty(self):
        """Prompts the user to select a difficulty level."""
        if not self.difficulty_levels:
            print("No available boards to load.")
            return None

        print("Select a difficulty level:")
        for i, (difficulty, boards) in enumerate(self.difficulty_levels.items(), start=1):
            print(f"{i}. {difficulty} ({len(boards)} board(s) available)")
        
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice < 1 or choice > len(self.difficulty_levels):
                raise ValueError("Invalid choice")

            selected_difficulty = list(self.difficulty_levels.keys())[choice - 1]
            print(f"You selected: {selected_difficulty}")
            board_num = self.difficulty_levels[selected_difficulty][0]  # Select the first board of that difficulty
            self.board = self.load_board(board_num)
        except (ValueError, IndexError):
            print("Invalid selection. Starting with an empty board.")
            self.board = self.create_empty_board()

    def load_board(self, board_num=1):
        """Loads a specific Sudoku board by number from the board file."""
        if not os.path.exists(self.board_file):
            print(f"{self.board_file} not found. Loading an empty board.")
            return self.create_empty_board()

        with open(self.board_file, "r") as f:
            lines = f.readlines()

        board = []
        current_board_num = 0
        board_start = False

        for line in lines:
            # Check for the start of a new board
            if line.startswith("Board #"):
                current_board_num += 1
                board_start = current_board_num == board_num
                board = []  # Reset board for new puzzle
                continue

            # If we have reached the desired board, collect the board's rows
            if board_start:
                # Ignore separator lines (those with '-')
                if '-' in line:
                    continue
                # Extract only the numbers, split by space
                row = [int(x) if x.isdigit() else 0 for x in line.split() if x.isdigit()]
                if len(row) == 9:  # Ensure it's a valid row of length 9
                    board.append(row)

            # Stop when we've collected 9 rows (a full board)
            if board_start and len(board) == 9:
                break

        if len(board) == 9:
            print(f"Board #{board_num} loaded successfully.")
            return board
        else:
            print("Error loading board. Creating an empty board.")
            return self.create_empty_board()

    def create_empty_board(self):
        """Creates an empty 9x9 Sudoku board and saves it."""
        board = [[0] * 9 for _ in range(9)]
        self.save_board(board)
        return board

    def save_board(self, board=None, file=None):
        """Saves the current board to a file."""
        board = board if board is not None else self.board
        file = file if file else self.saved_file

        with open(file, "w") as f:
            f.write("Current Board:\n")
            for i, row in enumerate(board):
                row_str = " ".join(str(num) if num != 0 else "." for num in row)
                f.write(row_str[:5] + " | " + row_str[6:11] + " | " + row_str[12:] + "\n")
                if (i + 1) % 3 == 0 and i != 8:
                    f.write("- - - - - - - - - - -\n")

        print(f"Board saved to {file}")

    def print_board(self):
        """Prints the board to the console for visualization."""
        print("   1 2 3   4 5 6   7 8 9")
        print("  -------------------------")
        for i, row in enumerate(self.board):
            row_label = chr(ord('A') + i)
            row_str = " ".join(str(num) if num != 0 else "." for num in row)
            print(f"{row_label} | {row_str[:5]} | {row_str[6:11]} | {row_str[12:]}")
            if (i + 1) % 3 == 0 and i != 8:
                print("  -------------------------")

    def is_valid_move(self, row, col, num):
        """Checks if a move is valid."""
        if num in self.board[row] or num in [self.board[r][col] for r in range(9)]:
            return False

        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True

    def make_move(self, row, col, num):
        """Makes a move if valid and saves it."""
        if self.is_valid_move(row, col, num):
            self.board[row][col] = num
            self.save_board()
            print(f"Move {num} placed at {chr(row + 65)}{col + 1}")
            return True
        print("Invalid move.")
        return False

    def is_complete(self):
        """Checks if the board is complete."""
        return all(0 not in row for row in self.board)

    def play_game(self):
        """Game loop for user moves."""
        self.select_difficulty()  # Prompt for difficulty at the start
        if not self.board:
            print("No board loaded. Exiting game.")
            return

        print("Enter your moves in 'A1 5' format (row A, column 1, number 5). Type 'exit' to quit.")
        while not self.is_complete():
            self.print_board()
            move = input("Your move: ")

            if move.lower() == "exit":
                print("Game saved and exited.")
                self.save_board()
                break

            try:
                pos, num = move.split()
                row = ord(pos[0].upper()) - ord('A')
                col = int(pos[1]) - 1
                num = int(num)

                if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                    print("Invalid input. Try again.")
                    continue

                if not self.make_move(row, col, num):
                    print("Invalid move.")
            except (ValueError, IndexError):
                print("Invalid format. Use 'A1 5'.")
        
        if self.is_complete():
            print("Congratulations! Game completed.")
            self.save_board(file=self.completed_file)
            print("Completed board saved.")
