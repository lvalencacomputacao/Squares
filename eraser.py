import pygame

class Eraser:

    def __init__(self, color):
        self.color = color

    # MarkCell is the main method of Pincel. It marks the cell on the board with a "color"(index of the color)
    # Later, on main.py, the draw function takes the board and actually draw the screen
    def markCell(self, matrix, line, column, xToDraw, yToDraw, screen, basicX, basicY, width, height):
        matrix[line][column] = 0

        pygame.draw.rect(screen, (255, 255, 255), (xToDraw, yToDraw, basicX, basicY))
        pygame.display.flip()