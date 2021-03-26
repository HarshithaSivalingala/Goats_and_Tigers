import pygame
pygame.init()
clock = pygame.time.Clock()
text1 = "Play"
text2 = "Quit"

bgimage = pygame.image.load("game bg.png")
picture = pygame.transform.scale(bgimage, (1400, 700))

BLACK = (0, 0, 0)
lIGHT_GREEN = (50, 205, 50)
RED = (220, 20, 60)
LIGHT_YELLOW = (200, 200, 0)
YELLOW = (255, 255, 0)
GREEN = (34, 177, 76)
LIME = (0, 255, 0)
width = 1400
height = 800
screen = pygame.display.set_mode((width, height))


class GamePlay:
    def __init__(self):
        self.width = width
        self.height = height
        self.move = 0
        pygame.display.set_caption("Goats and Tiger")


    def gameBoard(self):
        bg = pygame.image.load("notes_and_resources/brown_bg.jpg")
        screen.blit(bg, (0, 0))

        self.color = (255, 255, 255)

        # creating A triangle
        pygame.draw.polygon(screen, self.color, [[300, 600], [700, 600], [500, 200]], 2)
        pygame.draw.lines(screen, self.color, True, [[300, 333.3], [700, 333.3], [700, 466.6], [300, 466.6]], 2)
        pygame.draw.line(screen, self.color, (300, 399.9), (700, 399.9), 2)
        pygame.draw.aalines(screen, self.color, False, [[433, 600], [500, 200], [566, 600]])

    def scoreBoard(self):
        BLACK = (0, 0, 0)
        # font for Title
        fontT = pygame.font.SysFont("monospace", 45)
        text = fontT.render("Score Board", True, BLACK)
        screen.blit(text, (800, 100))
        font = pygame.font.SysFont("arial.tff", 35)
        text1 = font.render("Goats Left : ", True, BLACK)
        screen.blit(text1, (750, 200))
        text2 = font.render("Goats Captured : ", True, BLACK)
        screen.blit(text2, (750, 300))
        text3 = font.render("Tigers Cornered : ", True, BLACK)
        screen.blit(text3, (750, 400))

    def drawTiger(self, tx, ty):
        # Inserting tiger
        tiger = pygame.image.load('notes_and_resources/Tiger.png')
        tiger = pygame.transform.scale(tiger, (40, 40))
        rect = tiger.get_rect()
        rect.center = (tx, ty)
        screen.blit(tiger, rect)
        return rect


    def textButton(self, text, color, x, y, width, height):
        if text == text1:
            text = pygame.font.SysFont("comicsansms", 25)
            textB = text.render(text1, True, color)
            # textB1 = text.render(text2, True, color)
            rect = textB.get_rect()
            rect.center = ((x + (width / 2)), (y + (height / 2)))
            screen.blit(textB, rect)

        elif text == text2:
            text = pygame.font.SysFont("comicsansms", 25)
            textB1 = text.render(text2, True, color)
            rect = textB1.get_rect()
            rect.center = ((x + (width / 2)), (y + (height / 2)))
            screen.blit(textB1, rect)

    def buttons(self, text, x, y, width, height, color1, color2, action=None):
        current = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > current[0] > x and y + height > current[1] > y:
            pygame.draw.rect(screen, color1, (x, y, width, height))
            if click[0] == 1 and action != None:
                if action == "Quit":
                    pygame.quit()
                    quit()
                    # game starts
        else:
            pygame.draw.rect(screen, color2, (x, y, width, height))



game = GamePlay()

menu = True
running = True
which = -1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu = True

        screen.fill((0, 0, 0))
        #clock.tick(15)

        screen.blit(picture, (0, 0))
        game.buttons("Play", 100, 150, 70, 50, LIME, GREEN, action="Play")
        game.buttons("Quit", 300, 150, 70, 50, YELLOW, LIGHT_YELLOW, action="Quit")

        game.textButton(text1, BLACK, 100, 150, 70, 50)
        game.textButton(text2, BLACK, 300, 150, 70, 50)

        pygame.display.update()

    game.gameBoard()
    game.scoreBoard()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)