import pygame
import time
pygame.init()


class gamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Goats and Tiger")

    def gameBoard(self):
        bg = pygame.image.load("notes and resources/brown_bg.jpg")
        self.screen.blit(bg, (0, 0))

        color = (255, 255, 255)
        pygame.draw.polygon(self.screen, color, [[300, 600], [700, 600], [500, 200]], 2)
        pygame.draw.lines(self.screen, color, True, [[300, 333.3], [700, 333.3], [700, 466.6], [300, 466.6]], 2)
        pygame.draw.line(self.screen, color, (300, 399.9), (700, 399.9), 2)
        pygame.draw.aalines(self.screen, color, False, [[433, 600], [500, 200], [566, 600]], 2)
        pygame.display.flip()

    def scoreBoard(self):
        BLACK = (0, 0, 0)
        fontT = pygame.font.SysFont("monospace", 45)
        text = fontT.render("Score Board", True, BLACK)
        self.screen.blit(text, (800, 100))
        font = pygame.font.SysFont("arial", 35)
        text1 = font.render("Goats Left : ", True, BLACK)
        self.screen.blit(text1, (750, 200))
        text2 = font.render("Goats Captured : ", True, BLACK)
        self.screen.blit(text2, (750, 300))
        text3 = font.render("Tigers Cornered : ", True, BLACK)
        self.screen.blit(text3, (750, 400))
        pygame.display.flip()

    def drawTiger(self, tx, ty):
        tiger = pygame.image.load('notes and resources/Tiger.png')
        tiger = pygame.transform.scale(tiger, (40, 40))
        rect = tiger.get_rect()
        rect = rect.move((tx, ty))
        self.screen.blit(tiger, rect)
        pygame.display.flip()
        pygame.time.delay(60)

game = gamePlay(1200, 800)

running = True
while running:
    game.gameBoard()
    game.scoreBoard()
    game.drawTiger(500, 200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(30)