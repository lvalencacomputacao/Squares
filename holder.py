import pygame
from grid import Grid
from pincel import Pincel
from eraser import Eraser

pygame.init()

#screenDefinitions
width = 700
height = 700
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("SimplePixelArt")

#Music Loading
pygame.mixer_music.load("musica/Lullaby.mp3")
pygame.mixer_music.play(-1)

#Board Logic
rows = 100
columns = 100
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

screen.fill((255, 255, 255))

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
                                      screen, basicX, basicY)
            #board.printGrid()

        if event.type == pygame.MOUSEBUTTONUP:
            clicking = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("Now using Pincel")
                ferramenta = Pincel(color)
                board.ferramenta = ferramenta
            elif event.key == pygame.K_2:
                print("Now using Fill")
                pass
            elif event.key == pygame.K_3:
                print("Now using Eraser")
                ferramenta = Eraser(color)
                board.ferramenta = ferramenta

        if event.type == pygame.VIDEORESIZE:
            width = event.w
            height = event.h

            basicX = width // rows
            basicY = height // columns
            modifierX = width / columns
            modifierY = height / rows
            pygame.display.flip()


pygame.quit()
