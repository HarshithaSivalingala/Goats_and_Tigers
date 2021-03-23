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
            pygame.draw.polygon(self.screen, color, [[300,600],[700,600],[500,200]] , 2)
            pygame.display.flip()
            pygame.draw.lines(self.screen, color, True, [[300, 333.3], [700, 333.3],[700, 466.6],[300,466.6]], 2)
            pygame.draw.line(self.screen,color,(300,399.9),(700,399.9), 2)
            pygame.draw.aalines(self.screen, color, False,[[433, 600], [500,200],[566, 600], [500, 200]],2)



game = gamePlay(1400, 800)
game.gameBoard()