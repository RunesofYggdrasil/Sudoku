from sudoku import Sudoku

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