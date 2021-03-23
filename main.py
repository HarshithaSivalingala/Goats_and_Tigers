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
            rectangle = pygame.Rect(400, 400, 400, 400)
            rectangle.center = (500, 400)
            pygame.draw.rect(self.screen, color, rectangle, 2)
            pygame.display.flip()
            pygame.draw.lines(self.screen, color, True, [[500, 200], [700, 400], [500, 600], [300, 400]], 2)
            # horizontal lines
            pygame.draw.lines(self.screen, color, True, [(300, 300), (700, 300)], 2)
            pygame.draw.lines(self.screen, color, True, [(700, 400), (300, 400)], 2)
            pygame.draw.lines(self.screen, color, True, [(300, 500), (700, 500)], 2)

# vertical lines
            pygame.draw.lines(self.screen, color, True, [(400, 200), (400, 600)], 2)
            pygame.draw.lines(self.screen, color, True, [(500, 200), (500, 600)], 2)
            pygame.draw.lines(self.screen, color, True, [(600, 200), (600, 600)], 2)


game = gamePlay(1400, 800)
game.gameBoard()