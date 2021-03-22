import pygame
pygame.init()


class gamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Goats and Tiger")

    def gameBoard(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            color = (255, 255, 255)
            rectangle = pygame.Rect(400,400,400,400)
            rectangle.center = (500,400)

            pygame.draw.rect(self.screen, color, rectangle, 2)

            pygame.display.flip()
game = gamePlay(1400, 800)
game.gameBoard()