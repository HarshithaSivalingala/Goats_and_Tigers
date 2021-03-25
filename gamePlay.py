import pygame

pygame.init()
BLACK = (0, 0, 0)
whichT = -1
whichG = -1

moves = 0

input_rect = pygame.Rect(800, 600, 200, 50)
clock = pygame.time.Clock()

pygame.mixer.music.load('notes_and_resources/BG2.mp3')
pygame.mixer.music.play(-1)
tiger_noise = pygame.mixer.Sound('notes_and_resources/sounds_tigersound.wav')
goat_noise = pygame.mixer.Sound('notes_and_resources/Goat-noise.mp3')

tiger = 1
goat = 0
boardState = [[(400, 200), 1],
              [(200, 334), -1], [(333, 333), -1], [(378, 331), 1], [(422, 334), 1], [(467, 333), -1], [(600, 333), -1],
              [(200, 400), -1], [(300, 400), -1], [(366, 400), -1], [(433, 400), -1], [(500, 400), -1], [(600, 400), -1],
              [(200, 468), -1], [(266, 466), -1], [(356, 467), -1], [(443, 467), -1], [(534, 466), -1], [(600, 466), -1],
              [(200, 600), -1], [(333, 600), -1], [(467, 600), -1], [(600, 600), -1]]

class GamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.tigersCornered = 0
        self.goatsLeft = 15
        self.goatsCaptured = 0

        self.phase1 = True
        self.goatOn = -1

        pygame.display.set_caption("Goats and Tiger")

    def gameBoard(self):
        bg = pygame.image.load("notes_and_resources/brown_bg.jpg")
        self.screen.blit(bg, (0, 0))

        self.black = (0, 0, 0)
        self.brown = (139, 69, 19)
        self.chestnut = (221,173,175)

        # creating A triangle
        pygame.draw.polygon(self.screen, self.black, [[200, 600], [600, 600], [400, 200]], 3)
        pygame.draw.lines(self.screen, self.black, True, [[200, 333.3], [600, 333.3], [600, 466.6], [200, 466.6]], 3)
        pygame.draw.line(self.screen, self.black, (200, 399.9), (600, 399.9), 3)
        pygame.draw.aalines(self.screen, self.black, False, [[333, 600], [400, 200], [466, 600]])

        self.boardPositions = [(400, 200),
                      (200, 334), (333, 333), (378, 331), (422, 334), (467, 333), (600, 333),
                      (200, 400), (300, 400), (366, 400), (433, 400), (500, 400), (600, 400),
                      (200, 468), (266, 466), (356, 467), (443, 467), (534, 466), (600, 466),
                      (200, 600), (333, 600), (467, 600), (600, 600)]

        for i, point in enumerate(self.boardPositions):
            pygame.draw.circle(self.screen, self.brown, point, 10)
            fontnum = pygame.font.SysFont("monospace", 15, True)
            text = fontnum.render(str(i), True, self.chestnut)
            textRect = text.get_rect()
            textRect.center = point
            self.screen.blit(text, textRect)

    def user_input(self):
        # input the text
        base_font = pygame.font.Font(None, 32) # text to be added
        text = base_font.render(user_text, True, BLACK)
        pygame.draw.rect(self.screen, BLACK, input_rect, 3)
        self.screen.blit(text, pygame.Rect(804, 604, 200, 50))
        # input_rect.w = max(100, text.get_width() + 10) # if the text is increased

    def scoreBoard(self):
        BLACK = (0, 0, 0)
        GREEN = (50,205,50)
        RED = (220,20,60)
        # font for Title
        fontT = pygame.font.SysFont("monospace", 45)
        text = fontT.render("Score Board", True, BLACK)
        self.screen.blit(text, (800, 100))
        font = pygame.font.SysFont("arial.tff", 35)
        text1 = font.render("Goats Left : ", True, BLACK)
        goatsLeft = font.render(str(self.goatsLeft), True, GREEN)
        self.screen.blit(text1, (750, 200))
        self.screen.blit(goatsLeft, (970, 200))
        text2 = font.render("Goats Captured : ", True, BLACK)
        goatsCaught = font.render(str(self.goatsCaptured), True, RED)
        self.screen.blit(text2, (750, 300))
        self.screen.blit(goatsCaught, (970, 300))
        text3 = font.render("Tigers Cornered : ", True, BLACK)
        tigersCornered = font.render(str(self.tigersCornered), True, RED)
        self.screen.blit(text3, (750, 400))
        self.screen.blit(tigersCornered, (970, 400))

    def drawTiger(self, coord):
        tiger = pygame.image.load('notes_and_resources/Tiger.png')
        tiger = pygame.transform.scale(tiger, (40, 40))
        rect = tiger.get_rect()
        rect.center = (coord[0], coord[1])
        self.screen.blit(tiger, rect)
        return rect

    def drawGoat(self, coord):
        goat = pygame.image.load('notes_and_resources/goat.png')
        goat = pygame.transform.scale(goat, (40, 40))
        rect = goat.get_rect()
        rect.center = (coord[0], coord[1])
        self.screen.blit(goat, rect)
        return rect

    def display(self, move):
        font2 = pygame.font.SysFont("comicsansms", 35)
        font3 = pygame.font.SysFont("comicsansms", 30)
        gTurn = font2.render("Goat's Turn", True, BLACK)
        tTurn = font2.render("Tiger's Turn", True, BLACK)
        Text = font3.render("Enter the position (From, To)", True, BLACK)
        gText = font3.render("Enter the position", True, BLACK)

        if moves % 2 == 0:
            if moves < 31:
                self.screen.blit(gTurn, (800, 500))
                self.screen.blit(gText, (770, 550))

            else:
                self.screen.blit(gTurn, (800, 500))
                self.screen.blit(Text, (740, 550))
        else:
            self.screen.blit(tTurn, (800, 500))
            self.screen.blit(Text, (740, 550))

    def whichPiece(self, pos):
        if boardState[pos][1] == 1:
            for i in range(3):
                if tigerVect[i].center == boardState[pos][0]:
                    return i
        elif boardState[pos][1] == 0:
            for j in range(15):
                if goatsVect[j].center == boardState[pos][0]:
                    return j

    def movePiece(self, inp):
        global moves
        moves += 1

        if moves == 30:
            self.phase1 = False

        if moves % 2 != 0 and self.phase1:
                self.goatMove1(inp)

        elif self.phase1 == False:
            text = inp.strip().split(',')
            curr, des = int(text[0]), int(text[1])
            whichG = self.whichPiece(curr)
            self.goatMove(curr, des, whichG)

        else:
            text = inp.strip().split(',')
            curr, des = int(text[0]), int(text[1])
            whichT = self.whichPiece(curr)
            self.tigerMove(curr, des, whichT)


    def tigerMove(self, curr, des, whichT):
        tigerPositions[whichT] = boardState[des][0]
        boardState[curr][1] = -1
        boardState[des][1] = 1
        tiger_noise.play()

    def goatMove(self, curr, des, whichG):
        goatPositions[whichG] = boardState[des][0]
        goat_noise.play()
        boardState[curr][1] = -1
        boardState[des][1] = 0

    def goatMove1(self, inp):
        self.goatOn += 1
        goatPositions[self.goatOn] = boardState[int(inp)][0]
        goat_noise.play()
        boardState[int(inp)][1] = 0


game = GamePlay(1200, 800)

running = True

tigerPositions = [(400, 200), (378, 331), (422, 334)]
goatPositions = []

user_text = ''

while running:
    game.gameBoard()
    game.scoreBoard()
    game.user_input()

    tiger0 = game.drawTiger(tigerPositions[0])
    tiger1 = game.drawTiger(tigerPositions[1])
    tiger2 = game.drawTiger(tigerPositions[2])

    tigerVect = [tiger0, tiger1, tiger2]
    goatsVect = []

    for i in range(300, 600, 20):
        goatPositions.append((100, i))

    for j in range(15):
        goatsVect.append(game.drawGoat(goatPositions[j]))

    game.display(moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                game.movePiece(user_text)
                user_text = ''

            else:
                user_text += event.unicode

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)