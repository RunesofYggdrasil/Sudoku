class Sudoku:
    """ 
    A class to represent a Sudoku board.

        Attributes:
            self.title (str): X.
            self.author (str): X.
            self.board (int list list): X.

        Methods:
            get_title() (-> str): X.
            get_author() (-> str): X.
    """
    def __init__(self, init_title, init_author, init_board):
        """ 
        Initializes a Sudoku board.
        
            Parameters:
                init_title (str): X.
                init_author (str): X.
                init_board (int list list): X.
        """
        self.title = init_title
        self.author = init_author
        self.board = init_board
        self.changes = []
        self.change_index = 0
    
    def __eq__(self, other):
        """ Returns True if the title, author, and entire board are equal, and False otherwise. """
        for i in range(len(self.board)):
            row = self.board[i]
            other_row = other.get_board()[i]
            for j in range(len(row)):
                if row[j] != other_row[j]:
                    return False
        return self.title == other.get_title() and self.author == other.get_author()
    
    def __str__(self):
        """ Converts the Sudoku board to a string. """
        sudoku_str = self.title + " by " + self.author
        board_str = ""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                board_str += "- - - - - - - - - - - -\n"
            row = self.board[i]
            for j in range(len(row)):
                col = row[j]
                if j % 3 == 0 and j != 0:
                    board_str += " | "
                board_str += str(col) + " "
            board_str = board_str.strip()
            board_str += "\n"
        sudoku_str += "\n" + board_str.strip()
        return sudoku_str
    
    def __repr__(self):
        """ Converts the Sudoku board to a representation. """
        sudoku_str = self.title + " by " + self.author
        board_str = ""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                board_str += "- - - - - - - - - - - -\n"
            row = self.board[i]
            for j in range(len(row)):
                col = row[j]
                if j % 3 == 0 and j != 0:
                    board_str += " | "
                board_str += str(col) + " "
            board_str = board_str.strip()
            board_str += "\n"
        sudoku_str += "\n" + board_str.strip()
        return sudoku_str
    
    def print_board(self):
        """ Prints the board to the console for visualization. """
        print("    1 2 3   4 5 6   7 8 9")
        print("  -------------------------")
        for i, row in enumerate(self.board):
            row_label = chr(ord('A') + i)
            row_str = " ".join(str(num) if num != 0 else "." for num in row)
            print(f"{row_label} | {row_str[:5]} | {row_str[6:11]} | {row_str[12:]}")
            if (i + 1) % 3 == 0 and i != 8:
                print("  -------------------------")

    def get_title(self):
        """ Returns the title of the Sudoku board. """
        return self.title
    
    def get_author(self):
        """ Returns the author of the Sudoku board. """
        return self.author
    
    def get_board(self):
        """ Returns the board of the Sudoku board. """
        return self.board
    
    def get_row(self, n):
        """ Returns row n of the Sudoku board. """
        return self.board[n]

    def get_col(self, n):
        """ Returns col n of the Sudoku board. """
        return [row[n] for row in self.board]
    
    def get_square(self, n):
        """ Returns square n of the Sudoku board. """
        row = (n // 3) * 3
        col = (n % 3) * 3
        return self.board[row][col:col + 3] + self.board[row + 1][col:col + 3] + self.board[row + 2][col:col + 3]
    
    def get_index(self, row, col):
        """ Returns the value at the row and column of the Sudoku board. """
        return self.board[row][col]
    
    def set_index(self, row, col, value):
        """ Sets the value at the row and column of the Sudoku board. """
        self.change_index += 1
        self.changes = self.changes[:self.change_index]
        self.changes.append({"index": [row, col], "before": self.board[row][col], "after": value})
        self.board[row][col] = value

    def undo(self):
        """ Undoes the previous move. """
        self.change_index -= 1
        change = self.changes[self.change_index]
        self.board[change["index"][0]][change["index"][1]] = change["before"]
    
    def redo(self):
        """ Redoes the previous move. """
        self.change_index += 1
        change = self.changes[self.change_index]
        self.board[change["index"][0]][change["index"][1]] = change["after"]
        
    def is_valid_move(self, row, col, value):
        """ Checks if a move is valid. """
        square = row // 3 + col % 3
        if (row >= 0 and row < 9) and (col >= 0 and col < 9) and (square >= 0 and square < 9) and (value > 0 and value <= 9):
            if value in self.get_row(row) or value in self.get_col(col) or value in self.get_square(square):
                return False
            else: 
                return True
        else: 
            return False

    def is_complete(self):
        """ Checks if the board is complete. """
        return all(0 not in row for row in self.board)
     
    def move(self, row, col, value):
        """ Checks if the move is valid and then makes the move. """
        if self.is_valid_move(row, col, value):
            self.set_index(row, col, value)
            print(f"{value} placed at {chr(row + 65)}{col + 1}")
        else: 
            print("Invalid Move.")

    def play(self):
        """ Loops game until board is complete. """
        print("Enter your moves in 'A1 5' format (row A, column 1, number 5). Type 'exit' to quit.")
        while not self.is_complete():
            self.print_board()
            move = input("Enter Move: ")
            if move.lower() == "exit":
                print("Game Saved and Exited.")
                break
            try:
                pos, value = move.split()
                row = ord(pos[0].upper()) - ord('A')
                col = int(pos[1]) - 1
                value = int(value)
                self.move(row, col, value)
            except (ValueError, IndexError):
                print("Invalid format. Use 'A1 5'.")
        if self.is_complete():
            print("Congratulations! Game Complete.")
