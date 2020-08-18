counter = 0


def Print_Board(board):
    """Prints the board in a readable way"""
    ticker = 0
    for row in board:
        row1 = row.copy()
        if ticker % 3 == 0 and ticker != 0:
            print("----|-----|-----")
        row1.insert(3, " | ")
        row1.insert(7, " | ")
        print("".join(map(str, row1)))

        ticker += 1
    print("\n")


def Valid_Square(board, pos, val):
    """Checks if the current square is valid with the given value and returns a bool"""
    # Check for row
    ticker = -1
    for square in board[pos[0]]:
        ticker += 1
        if square == val and ticker != pos[1]:
            return False

    # Check for column
    for i in range(0, 9):
        if i != pos[0]:
            if board[i][pos[1]] == val:
                return False

    # Divides and rounds down y coordinate resulting in one of 0, 1 or 2
    # Multiplies this number by 3 to get 0, 3 or 6 (the start of each section)
    # Adds 3 to get 3, 6 or 9 (the end of each section) and creates range from it
    for y in range(pos[0] // 3 * 3, pos[0] // 3 * 3 + 3):
        # Same for x coordinate
        for x in range(pos[1] // 3 * 3, pos[1] // 3 * 3 + 3):
            # Checks if the value in board at x, y coordinates == val and is not position of one being tested against
            if board[y][x] == val and (y, x) != pos:
                return False
    # If it passes all tests without returning False then return True
    return True


def Find_Empty(board):
    """Searches the board for the next square == 0 and returns it's coordinates.
    If there is none then it returns False"""
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return y, x  # row, col

    return False


def Solver(board):
    """Solves the board using backtracking algorithm and recursion"""
    # Uses, global variable, counter to stop any infinite loops for boards with multiple solutions
    global counter
    if counter < 1:
        current_square = Find_Empty(board)
        # If there is no more empty squares then update counter to stop repeat and print the board
        if not Find_Empty(board):
            Print_Board(board)
            counter += 1
            return False
        # Else create coordinates
        else:
            y, x = current_square
        # Loop through with values 1, 9 and test validity

        if counter < 1:
            for val in range(1, 10):

                # If True then insert the value and call function with new board
                if Valid_Square(board, current_square, val):
                    board[y][x] = val

                    Solver(board)
        # If looped through and nothing works then backtrack
        board[y][x] = 0
        return board


def Solve_Sudoku(board):
    global counter
    counter = 0
    print("Problem")
    Print_Board(board)
    print("Solution")
    Solver(board)


Solve_Sudoku([[0, 0, 5, 3, 0, 0, 0, 0, 0],
              [8, 0, 0, 0, 0, 0, 0, 2, 0],
              [0, 7, 0, 0, 1, 0, 5, 0, 0],
              [4, 0, 0, 0, 0, 5, 3, 0, 0],
              [0, 1, 0, 0, 7, 0, 0, 0, 6],
              [0, 0, 3, 2, 0, 0, 0, 8, 0],
              [0, 6, 0, 5, 0, 0, 0, 0, 9],
              [0, 0, 4, 0, 0, 0, 0, 3, 0],
              [0, 0, 0, 0, 0, 9, 7, 0, 0]])




