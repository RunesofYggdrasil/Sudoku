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


def get_board(n):
    """ Reads sudokuboards.txt and gets the board via the board number n. """
    file = open("sudokuboards.txt", "r")
    board_n = "Board #" + str(n)

    index = 0
    lines = file.readlines()
    for line in lines:
        if board_n in line:
            break
        else:
            index += 1
    
    board = lines[index:index + 12]
    file.close()

    name = board[0].strip().split(" by ")
    board_list = []
    for row in board[1:]:
        split_row = row.split()
        board_row = []
        for col in split_row:
            if col.isnumeric():
                board_row.append(int(col))
        if len(board_row) > 0:
            board_list.append(board_row)

    dict = {"title": name[0], "author": name[1], "board": board_list}
    return dict

board1 = get_board(1)
board2 = get_board(2)
board3 = get_board(3)
s1 = Sudoku(board1["title"], board1["author"], board1["board"])
s2 = Sudoku(board2["title"], board2["author"], board2["board"])
s3 = Sudoku(board3["title"], board3["author"], board3["board"])
