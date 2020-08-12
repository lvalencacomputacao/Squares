import pygame

class Mirror:

    rgb = {1: (0, 0, 0), 2: (255, 0, 0), 3: (0, 255, 0), 4: (0, 0, 255)}

    def __init__(self, color):
        self.color = color

    # MarkCell is the main method of Pincel. It marks the cell on the board with a "color"(index of the color)
    # Later, on main.py, the draw function takes the board and actually draw the screen
    def markCell(self, matrix, line, column, xToDraw, yToDraw, screen, basicX, basicY, width, height):
        # print('h')
        rows = len(matrix)
        columns = len(matrix[0])

        revLine = rows - 1 - line
        revColumn = columns - 1 - column

        matrix[line][column] = self.color
        matrix[revLine][revColumn] = self.color

        xToDrawRev = width - xToDraw - basicX
        yToDrawRev = height - yToDraw - basicY

        # print(xToDraw, xToDrawRev)
        # print(yToDraw, yToDrawRev)

        pygame.draw.rect(screen, self.rgb[self.color], (xToDraw, yToDraw, basicX, basicY))
        pygame.draw.rect(screen, self.rgb[self.color], (xToDrawRev, yToDrawRev, basicX, basicY))
        pygame.display.flip()