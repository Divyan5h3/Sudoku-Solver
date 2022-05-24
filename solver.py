import numpy

def find_row_col(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row,col
    return None, None

def valid_move(puzzle, row, col, number):
    row_array = []
    col_array = []
    for i in range(9):
        row_array.append(puzzle[row][i]) 
        col_array.append(puzzle[i][col])
    if number in row_array or number in col_array:
        return False

    start_row = (row//3) * 3
    start_col = (col//3) * 3

    for row in range(start_row, start_row+3):
        for col in range(start_col, start_col+3):
            if puzzle[row][col] == number:
                return False
    return True
    
def solve_sudoku(puzzle):
    row, col = find_row_col(puzzle)

    if row == None:
        return True

    for number in range(1,10):
        if valid_move(puzzle, row, col, number):
            puzzle[row][col] = number
            if (solve_sudoku(puzzle)):
                return True
        
        puzzle[row][col] = -1
    return False


# test solver, add values to test

if __name__ == '__main__':
    example_board = [
        [7, 8, 2, -1, -1, -1, 1, 4, 9],
        [-1, -1, 9, -1, -1, -1, -1, -1, -1],
        [-1, -1, 1, -1, 4, 9, -1, -1, -1],
        [-1, -1, -1, 9, -1, -1, -1, -1, 3],
        [-1, 2, 6, 4, -1, -1, 5, 9, -1],
        [9, -1, -1, -1, -1, 1, -1, 7, 2],
        [2, -1, 8, -1, -1, -1, -1, 3, 6],
        [-1, -1, -1, 6, -1, 7, 2, -1, 8],
        [1, 6, -1, 2, -1, -1, -1, -1, -1]
    ]

print(solve_sudoku(example_board))
arr = numpy.array(example_board)
print(arr)