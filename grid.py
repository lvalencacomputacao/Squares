from pincel import Pincel

class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [[0 for i in range(rows)] for j in range(columns)]
        self.ferramenta = Pincel(1)

    # Using this method, the user can set a tool in the middle of the game. Default one is "Pincel"
    # There are 3 tools, "Pincel", "Fill" and "Eraser"
    def setFerramenta(self, ferramenta):
        self.ferramenta = ferramenta

    # Debugging tool to print grid. Not to be mistaken with the drawing method in "main.py"
    def printGrid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i][j], end=' ')
            print('')