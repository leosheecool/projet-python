#!/user/bin/python3.7
import numpy as np

class CheckVictory():
    def checkRows(self, board):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0

    def checkDiagonals(self, board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return 0

    def checkWin(self, board):
        for newBoard in [board, np.transpose(board)]:
            result = self.checkRows(newBoard)
            if result:
                return result
        return self.checkDiagonals(board)