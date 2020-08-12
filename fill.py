import pygame

class Fill:

    rgb = {1: (0, 0, 0), 2: (255, 0, 0), 3: (0, 255, 0), 4: (0, 0, 255)}

    def __init__(self, color):
        self.color = color

    # MarkCell is the main method of Pincel. It marks the cell on the board with a "color"(index of the color)
    # Later, on main.py, the draw function takes the board and actually draw the screen
    def markCell(self, matrix, line, column, xToDraw, yToDraw, screen, basicX, basicY, width, height):
        firstCell = (line, column)
        toTry = [firstCell]
        visited = []
        rows = len(matrix)
        columns = len(matrix[0])

        width, height = pygame.display.get_surface().get_size()
        modifierX = width / columns
        modifierY = height / rows

        while toTry:
            #print(toTry)
            ##print('')
            cellToPaint = toTry.pop()
            matrix[cellToPaint[0]][cellToPaint[1]] = self.color
            visited.append(cellToPaint)
            #print(matrix)

            if ((cellToPaint[0] + 1 <= rows - 1) and ((cellToPaint[0] + 1, cellToPaint[1]) not in visited)
                                                      and (matrix[cellToPaint[0] + 1][cellToPaint[1]] == 0)):
                #print('h')
                toTry.append((cellToPaint[0] + 1, cellToPaint[1]))

            if ((cellToPaint[0] - 1 >= 0) and ((cellToPaint[0] - 1, cellToPaint[1]) not in visited)
                                                      and (matrix[cellToPaint[0] - 1][cellToPaint[1]] == 0)):
                #print('h')
                toTry.append((cellToPaint[0] - 1, cellToPaint[1]))

            if ((cellToPaint[1] + 1 <= columns - 1) and ((cellToPaint[0], cellToPaint[1] + 1) not in visited)
                                                      and (matrix[cellToPaint[0]][cellToPaint[1] + 1] == 0)):
                #print('h')
                toTry.append((cellToPaint[0], cellToPaint[1] + 1))

            if ((cellToPaint[1] - 1 >= 0) and ((cellToPaint[0], cellToPaint[1] - 1) not in visited)
                                                      and (matrix[cellToPaint[0]][cellToPaint[1] - 1] == 0)):
                #print('h')
                toTry.append((cellToPaint[0], cellToPaint[1] - 1))


        for i in range(rows):
            for j in range(columns):
                if (matrix[i][j]):
                    pygame.draw.rect(screen, self.rgb[matrix[i][j]], (j * modifierX, i * modifierY, basicX, basicY))