"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Constraints:
1 <= n <= 9
"""

def solveNQueens(n: int):
    def backtrack(row, diagonals, anti_diagonals, cols, state, solutions):
        if row == n:
            solution = []
            for queen_col in state:
                line = ['.'] * n
                line[queen_col] = 'Q'
                solution.append("".join(line))
            solutions.append(solution)
            return
        
        for col in range(n):
            current_diag = row - col
            current_anti_diag = row + col
            if (col in cols or
                current_diag in diagonals or
                current_anti_diag in anti_diagonals):
                continue
            
            cols.add(col)
            diagonals.add(current_diag)
            anti_diagonals.add(current_anti_diag)
            state.append(col)
            
            backtrack(row + 1, diagonals, anti_diagonals, cols, state, solutions)
            
            cols.remove(col)
            diagonals.remove(current_diag)
            anti_diagonals.remove(current_anti_diag)
            state.pop()
    
    solutions = []
    backtrack(0, set(), set(), set(), [], solutions)
    return solutions
