"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
  1. Each of the digits 1-9 must occur exactly once in each row.
  2. Each of the digits 1-9 must occur exactly once in each column.
  3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
  
The '.' character indicates empty cells.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

def solveSudoku(board) -> None:
    def fillOnlyChoice(board):
        number_added = True
        while number_added:
            number_added = False
            for row in range(9):
                for column in range(9):
                    if board[row][column] == ".":
                        invalid_numbers = getInvalidNumbers(row, column, board)
                        # If only one valid number remains, assign it to the cell
                        if len(invalid_numbers) == 8:
                            valid = (set("123456789") - invalid_numbers).pop()
                            board[row][column] = valid
                            number_added = True

                        
    def getInvalidNumbers(row, col, board):
        # Row numbers
        invalid = set(board[row])  
    
        # Column numbers
        invalid.update(board[r][col] for r in range(9))  

        # Numbers from the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        invalid.update(board[r][c] for r in range(start_row, start_row + 3) 
                               for c in range(start_col, start_col + 3))
    
        invalid.discard(".")  
        return invalid


    def findCellWithFewestChoices(board):
        max_invalid_count = 0
        target = None

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    invalid_numbers = getInvalidNumbers(row, col, board)
                    invalid_count = len(invalid_numbers)

                    # Update target if cell has more invalid numbers
                    if invalid_count > max_invalid_count:
                        max_invalid_count = invalid_count
                        target = (row, col, set("123456789") - invalid_numbers)

                        # Early exit if the cell has only one choice left
                        if max_invalid_count == 8:
                            return target
    
        # Return None if no empty cells are found
        return target  


    def fillNumber(board):
        # Find the cell with the fewest possible valid numbers
        cell = findCellWithFewestChoices(board)
        if cell is None:
            return True  # Board is fully filled
    
        row, col, valid_numbers = cell
        for num in valid_numbers:
            # Try placing a valid number
            board[row][col] = num
            # Recursive call to attempt filling the next spot
            if fillNumber(board):
                return True
            # Backtrack if no solution was found with this number
            board[row][col] = "."
    
        # No valid numbers worked, so backtracking is needed
        return False


    
    # Fill cells with only one possible choice
    fillOnlyChoice(board)
    
    # Backtracking to complete the solution
    fillNumber(board)
       
    return board
