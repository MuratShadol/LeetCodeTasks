"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

"""

def isValidSudoku(board):
  for i in range(len(board)):
    hashrow = {}
    for j in range(len(board[0])):
      if board[i][j] != ".":
        if board[i][j] not in hashrow:
          hashrow[board[i][j]] = True
        else:
          return False

  for j in range(len(board[0])):
    hashcol = {}
    for i in range(len(board)):
      if board[i][j] != ".":
        if board[i][j] not in hashcol:
          hashcol[board[i][j]] = True
        else:
          return False

  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      hashsqr = {}
      for k in range(i, i+3):
        for v in range(j, j+3):
          if board[k][v] != ".":
            if board[k][v] not in hashsqr:
              hashsqr[board[k][v]] = True
            else:
              return False
  return True
