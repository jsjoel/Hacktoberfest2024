board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board1 =\
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]




class Solution(object):
    def isValidSudoku(self, board):
        rows = [[False]*9 for _ in range(9)]
        col =  [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    c= int(board[i][j])
                    boxes_index = (i//3)*3 + j//3
                    if rows[i][c-1] or col[j][c-1] or box[boxes_index][c-1]:
                        return False
                    rows[i][c-1] = True
                    col[j][c-1] = True
                    box[boxes_index][c-1] = True
        return True
        
solve = Solution()
print(solve.isValidSudoku(board))
print(solve.isValidSudoku(board1))