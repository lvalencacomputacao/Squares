import pygame
from grid import Grid
from pincel import Pincel
from eraser import Eraser
from fill import Fill
from dualPincel import *
from mirror import Mirror
from musica import Musica

pygame.init()

#screenDefinitions
width = 700
height = 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Squares")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Music Loading
pygame.mixer_music.load("musica/Lullaby.mp3")
pygame.mixer_music.play(-1)

#Board Logic
rows = 70
columns = 70
basicX = width // rows
basicY = height // columns
board = Grid(rows, columns)
modifierX = width / columns
modifierY = height / rows

#fsm
running = 1

#other logic
clicking = 0
color = 1
rgb = {1: (0, 0, 0), 2: (255, 0, 0), 3: (0, 255, 0), 4: (0, 0, 255)}

screen.fill((255, 255, 255))


def draw(screen, matrix, rows, columns, basicX, basicY, modifierX, modifierY, color):
    screen.fill((255, 255, 255))
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]:
                pygame.draw.rect(screen, rgb[color], (j * modifierX, i * modifierY, basicX, basicY))

#Main loop
while running:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = 0

        if event.type == pygame.MOUSEBUTTONDOWN or clicking:
            clicking = 1

            # Simply gets the x and y position, pixelwise
            xMouse, yMouse = pygame.mouse.get_pos()

            # Aproximates the position to the corner of the cell, pixelWise
            xToDraw = int(xMouse // modifierX * modifierX)
            yToDraw = int(yMouse // modifierY * modifierY)

            # Uses the tool main function. That is, pincel paints it, eraser takes It off and fill fills It
            board.ferramenta.markCell(board.board, int(yMouse // modifierY), int(xMouse // modifierX), xToDraw, yToDraw,
                                      screen, basicX, basicY, width, height)
            # board.printGrid()

        if event.type == pygame.MOUSEBUTTONUP:
            clicking = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Now using Pincel")
                ferramenta = Pincel(color)
                board.ferramenta = ferramenta
            elif event.key == pygame.K_2:
                print("Now using Fill")
                ferramenta = Fill(color)
                board.ferramenta = ferramenta
                pass
            elif event.key == pygame.K_3:
                print("Now using Eraser")
                ferramenta = Eraser(color)
                board.ferramenta = ferramenta
            elif event.key == pygame.K_4:
                print("Now using dualPencil1")
                ferramenta = DualPincel(color)
                board.ferramenta = ferramenta
            elif event.key == pygame.K_5:
                print("Now using dualPencil2")
                ferramenta = DualPincel2(color)
                board.ferramenta = ferramenta
            elif event.key == pygame.K_6:
                print("Now using Mirror")
                ferramenta = Mirror(color)
                board.ferramenta = ferramenta
            elif event.key == pygame.K_DELETE:
                board.board = [[0 for i in range(rows)] for j in range(columns)]
                screen.fill((255, 255, 255))
                pygame.display.flip()
            # Código abaixo pode ser simplificado, com um único dicionário
            # É um pouco trabalhoso, mas mude se tiver paciência
            elif event.key == pygame.K_r:
                color = 2
            elif event.key == pygame.K_g:
                color = 3
            elif event.key == pygame.K_b:
                if color == 1:
                    color = 4
                else:
                    color = 1
            elif event.key == pygame.K_0:
                Musica.mute(pygame.mixer_music.get_busy())
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Musica.ChangeVolume(event.key)

        if event.type == pygame.VIDEORESIZE:
            width = event.w
            height = event.h

            basicX = width // rows
            basicY = height // columns
            modifierX = width / columns
            modifierY = height / rows

            draw(screen, board.board, rows, columns, basicX, basicY, modifierX, modifierY, color)
            pygame.display.flip()


pygame.quit()
