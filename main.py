import pygame
pygame.init()


class gamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Goats and Tiger")

    def gameBoard(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


game = gamePlay(1400, 800)
game.gameBoard()