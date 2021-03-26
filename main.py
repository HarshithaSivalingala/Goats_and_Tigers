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


    def gameBoard(self):
        bg = pygame.image.load("notes_and_resources/brown_bg.jpg")
        self.screen.blit(bg, (0, 0))

        self.color = (255, 255, 255)

        # creating A triangle
        pygame.draw.polygon(self.screen, self.color, [[300, 600], [700, 600], [500, 200]], 2)
        pygame.draw.lines(self.screen, self.color, True, [[300, 333.3], [700, 333.3], [700, 466.6], [300, 466.6]], 2)
        pygame.draw.line(self.screen, self.color, (300, 399.9), (700, 399.9), 2)
        pygame.draw.aalines(self.screen, self.color, False, [[433, 600], [500, 200], [566, 600]])

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
        tiger = pygame.image.load('notes_and_resources/Tiger.png')
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
    tigerPositions = [(500, 200), (478, 331), (521, 332)]

    tiger1 = game.drawTiger(tigerPositions[0])
    tiger2 = game.drawTiger(tigerPositions[1])
    tiger3 = game.drawTiger(tigerPositions[2])

    tigerVect = [tiger1, tiger2, tiger3]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            which = game.whichPiece(x, y, 300, 600)


    game.tigerMove(300, 600, which)
    print(x,y)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)