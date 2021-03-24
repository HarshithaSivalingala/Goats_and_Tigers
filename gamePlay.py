import pygame
pygame.init()
clock = pygame.time.Clock()

class GamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.move = 0
        pygame.display.set_caption("Goats and Tiger")
        self.boardPositions = [(400, 200),
                               (200, 334), (333, 333), (377, 334), (422, 334), (467, 333), (600, 333),
                               (200, 400), (300, 400), (366, 400), (433, 400), (500, 400), (600, 400),
                               (200, 468), (266, 466), (356, 467), (443, 467), (534, 466), (600, 466),
                               (200, 600), (333, 600), (467, 600), (600, 600)]

    def gameBoard(self):
        bg = pygame.image.load("notes and resources/brown_bg.jpg")
        self.screen.blit(bg, (0, 0))

        self.black = (0, 0, 0)
        self.brown = (139, 69, 19)
        self.chestnut = (221,173,175)

        # creating A triangle
        pygame.draw.polygon(self.screen, self.black, [[200, 600], [600, 600], [400, 200]], 3)
        pygame.draw.lines(self.screen, self.black, True, [[200, 333.3], [600, 333.3], [600, 466.6], [200, 466.6]], 3)
        pygame.draw.line(self.screen, self.black, (200, 399.9), (600, 399.9), 3)
        pygame.draw.aalines(self.screen, self.black, False, [[333, 600], [400, 200], [466, 600]])

        for i, point in enumerate(self.boardPositions):
            pygame.draw.circle(self.screen, self.brown, point, 10)
            fontnum = pygame.font.SysFont("monospace", 15, True)
            text = fontnum.render(str(i), True, self.chestnut)
            textRect = text.get_rect()
            textRect.center = point
            self.screen.blit(text, textRect)

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
        return rect

    def whichPiece(self, x, y, dx, dy):
        for i in range(3):
            if tigerVect[i].top < y and tigerVect[i].left < x:
                print("It's tiger 1")
                return i
            else:
                print("not tiger 1")

    def movePiece(self, dx, dy, piece):
        pass

    def tigerMove(self, dx, dy, tn):
        tigerPositions[tn] = (dx, dy)  # (500, 200) = (300, 600)

    def goatMove(self, x, y):
        pass


game = GamePlay(1200, 800)

running = True
which = -1

while running:
    game.gameBoard()
    game.scoreBoard()
    tiger1 = game.drawTiger(400, 200)
    tiger2 = game.drawTiger(378, 331)
    tiger3 = game.drawTiger(421, 332)

    tigerPositions = [(500, 200), (478, 331), (521, 332)]
    #tigerVect = [tiger1, tiger2, tiger3]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            print(x, y)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)