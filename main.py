import pygame
pygame.init()
clock = pygame.time.Clock()

move = 0


class GamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Goats and Tiger")

    def gameBoard(self):
        bg = pygame.image.load("notes and resources/brown_bg.jpg")
        self.screen.blit(bg, (0, 0))

        color = (255, 255, 255)
        # creating A triangle
        pygame.draw.polygon(self.screen, color, [[300, 600], [700, 600], [500, 200]], 2)
        pygame.draw.lines(self.screen, color, True, [[300, 333.3], [700, 333.3], [700, 466.6], [300, 466.6]], 2)
        pygame.draw.line(self.screen, color, (300, 399.9), (700, 399.9), 2)
        pygame.draw.aalines(self.screen, color, False, [[433, 600], [500, 200], [566, 600]], 2)

    def scoreBoard(self):
        BLACK = (0, 0, 0)
        # font for Title
        fontT = pygame.font.SysFont("monospace", 45)
        text = fontT.render("Score Board", True, BLACK)
        self.screen.blit(text, (800, 100))
        font = pygame.font.SysFont("arial.tff", 35)
        text1 = font.render("Goats Left : ", True, BLACK)
        self.screen.blit(text1, (750, 200))
        text2 = font.render("Goats Captured : ", True, BLACK)
        self.screen.blit(text2, (750, 300))
        text3 = font.render("Tigers Cornered : ", True, BLACK)
        self.screen.blit(text3, (750, 400))

    def drawTiger(self, tx, ty):
        # Inserting tiger
        tiger = pygame.image.load('notes and resources/Tiger.png')
        tiger = pygame.transform.scale(tiger, (40, 40))
        rect = tiger.get_rect()
        rect.center = (tx, ty)
        self.screen.blit(tiger, rect)
        return tiger

    def movePiece(self, x, y):
        if move % 2 != 0:
            self.goatTurn(x, y)
        self.tigerTurn(x, y)

    def tigerTurn(self, x, y):
        pass

    def goatTurn(self, x, y):
        pass


game = GamePlay(1200, 800)

running = True
while running:
    game.gameBoard()
    game.scoreBoard()
    tiger1 = game.drawTiger(500, 200)
    tiger2 = game.drawTiger(478, 331)
    tiger3 = game.drawTiger(521, 332)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            move += 1
            x, y = pygame.mouse.get_pos()
            game.movePiece(x, y)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)