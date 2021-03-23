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

            #diagonal lines
            pygame.draw.line(self.screen, color, (300, 200), (700, 600), 2)
            pygame.draw.line(self.screen, color, (700, 200), (300, 600), 2)

            #horizontal lines

            initTopXleft = 300
            initBottomXright = 700

            for y in range(300, 600, 100):
                pygame.draw.line(self.screen, color, (initTopXleft, y), (initBottomXright, y), 2)

            # vertical lines
            initTopYv = 200
            initBottomYv = 600

            for x in range(400, 700, 100):
                pygame.draw.line(self.screen, color, (x, initTopYv), (x, initBottomYv), 2)


game = gamePlay(1400, 800)
game.gameBoard()