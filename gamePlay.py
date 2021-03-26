import pygame

pygame.init()

whichT = -1
whichG = -1

moves = 0
width = 1400
height = 800
screen = pygame.display.set_mode((width, height))

text1 = "Start Game"
text2 = "Quit"

 # colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREEN = (50, 205, 50)
RED = (139, 0, 0)
LIGHT_YELLOW = (200, 200, 0)
YELLOW = (255, 255, 0)
GREEN = (34, 177, 76)
LIME = (0, 255, 0)

input_rect = pygame.Rect(800, 600, 200, 50)

bgimage = pygame.image.load("notes_and_resources/menubg.jpg")
picture = pygame.transform.scale(bgimage, (1400, 800))

clock = pygame.time.Clock()


pygame.mixer.music.load('notes_and_resources/bgmusic.mp3')
pygame.mixer.music.play(-1)
tiger_noise = pygame.mixer.Sound('notes_and_resources/tiger-roar4.mp3')
goat_noise = pygame.mixer.Sound('notes_and_resources/Goat-noise.mp3')
coin_sound = pygame.mixer.Sound('notes_and_resources/coin_sound.wav')
tiger = 1
goat = 0

icon = pygame.image.load('notes_and_resources/icon.png')
pygame.display.set_icon(icon)

boardState = [[(400, 200), 1],
              [(200, 334), -1], [(333, 333), -1], [(378, 331), 1], [(422, 334), 1], [(467, 333), -1], [(600, 333), -1],
              [(200, 400), -1], [(300, 400), -1], [(366, 400), -1], [(433, 400), -1], [(500, 400), -1], [(600, 400), -1],
              [(200, 468), -1], [(266, 466), -1], [(356, 467), -1], [(443, 467), -1], [(534, 466), -1], [(600, 466), -1],
              [(200, 600), -1], [(333, 600), -1], [(467, 600), -1], [(600, 600), -1]]

neighbours = [[2, 3, 4, 5], [7, 2], [0, 1, 3, 8], [0, 2, 4, 9], [0, 3, 5, 10], [0, 4, 6, 11], [5, 12],
              [1, 8, 13], [2, 7, 9, 14], [3, 8, 10, 15], [4, 9, 11, 16], [5, 10, 12, 17], [6, 11, 18],
              [7, 14], [8, 13, 15, 19], [9, 14, 16, 20], [10, 15, 17, 21], [11, 16, 18, 22], [12, 17]]

tigerJumps = [[8, 9, 10, 11], [13, 3], [14, 4], [1, 5, 15], [2, 6, 16], [3, 17], [4, 18],
              [9], [0, 19, 10], [0, 7, 11, 20], [0, 8, 12, 21], [0, 9, 22], [10],
              [1, 15], [2, 16], [3, 13, 17], [4, 14, 18], [5, 15], [6, 16],
              [8, 21], [9, 22], [10, 19], [11, 20]]

class GamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.tigersCornered = 0
        self.goatsLeft = 15
        self.goatsCaptured = 0
        self.v = 1
        self.phase1 = True
        self.goatOn = -1
        self.goatOffx = 150
        self.goatOffy = 100

        pygame.display.set_caption("Goats and Tigers")


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
        # bg image
        image = pygame.image.load("notes_and_resources/scorebg.jpeg")
        image = pygame.transform.scale(image, (430, 370))
        sprite = pygame.sprite.Sprite()
        sprite.image = image

        sprite.rect = image.get_rect()
        #pygame.display.flip()
        sprite.rect.center = (950, 270)
        sprite.image.blit(image, sprite.rect)
        group = pygame.sprite.Group()
        group.add(sprite)
        group.draw(self.screen)

        # font for Title
        fontT = pygame.font.SysFont("forte", 47)
        text = fontT.render("Score Board", True, (77, 0, 13))
        self.screen.blit(text, (820, 100))
        font = pygame.font.SysFont("cooperblack", 28)
        text1 = font.render("Goats Left : ", True, BLACK)
        goatsLeft = font.render(str(self.goatsLeft), True, GREEN)
        self.screen.blit(text1, (750, 200))
        self.screen.blit(goatsLeft, (1000, 200))
        text2 = font.render("Goats Captured : ", True, BLACK)
        goatsCaught = font.render(str(self.goatsCaptured), True, RED)
        self.screen.blit(text2, (750, 300))
        self.screen.blit(goatsCaught, (1000, 300))
        text3 = font.render("Tigers Cornered : ", True, BLACK)
        tigersCornered = font.render(str(self.tigersCornered), True, RED)
        self.screen.blit(text3, (750, 400))
        self.screen.blit(tigersCornered, (1000, 400))

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

    def isValid(self, inp):
        self.v = 1
        if ',' in inp:
            [curr, des] = list(map(int, inp.strip().split(',')))
            if boardState[curr][1] == 1 and boardState[des][1] == 1:
                self.v = 0
                return False
            elif boardState[curr][1] != -1 and boardState[des][1] != -1:
                self.v = 0
                return False
            return True
        else:
            if boardState[int(inp)][1] == -1:
                return True
            self.v = 0
            return False

    def invalid(self):
        fontIn = pygame.font.SysFont("serif", 45)
        text = fontIn.render("Invalid Move", True, RED)
        self.screen.blit(text, (780, 660))

    def movePiece(self, inp):
        global moves
        coin_sound.play()
        if self.isValid(inp):
            moves += 1
        else:
            return

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

    def checkGoat(self, checkPos):
        if boardState[checkPos][1] == 0:
            for i in range(15):
                if goatsVect[i].center == self.boardPositions[checkPos]:
                    goatPositions[i] = (self.goatOffx, self.goatOffy)
                    self.goatOffx += 30
                    return True

    def goatKilled(self, curr, des):
        if (curr == 0 and des >= 2) or (curr >= 2 and des == 0):
            return self.verticalMove(curr, des)
        elif abs(curr - des) > 2:
            return self.verticalMove(curr, des)
        else:
            return self.horizontalMove(curr, des)

    def horizontalMove(self, curr, des):
        if abs(curr - des) == 1:
            return False
        else:
            checkPos = min(curr, des) + 1
            if self.checkGoat(checkPos):
                boardState[checkPos][1] = -1
                return True
            return False

    def verticalMove(self, curr, des):
        if curr != 0 and des != 0:
            checkPos = min(curr, des) + 6
            if self.checkGoat(checkPos):
                boardState[checkPos][1] = -1
                return True
            return False

        else:
            checkPos = max(curr, des) - 6
            if checkPos < 0:
                return False
            if self.checkGoat(checkPos):
                boardState[checkPos][1] = -1
                return True
            return False

    def tigerMove(self, curr, des, whichT):
        if self.goatKilled(curr, des):
           tiger_noise.play()
           self.goatsCaptured += 1
           self.goatsLeft -= 1

        tigerPositions[whichT] = boardState[des][0]
        boardState[curr][1] = -1
        boardState[des][1] = 1

    def goatMove(self, curr, des, whichG):
        goatPositions[whichG] = boardState[des][0]
        boardState[curr][1] = -1
        boardState[des][1] = 0
        self.isTigerCornered()

    def goatMove1(self, inp):
        self.goatOn += 1
        goatPositions[self.goatOn] = boardState[int(inp)][0]
        boardState[int(inp)][1] = 0
        self.isTigerCornered()

    def isTigerCornered(self):
        tc = 0
        for i in range(3):
            ind = boardState.index([tigerVect[i].center, 1])
            if self.checkNeighbours(ind) and self.checkTigerJump(ind):
                tc += 1
                goat_noise.play()
        self.tigersCornered = tc

    def goatsWon(self):
        fontW = pygame.font.SysFont("serif", 50)
        text = fontW.render("Goats Won!", True, BLACK)
        trect = text.get_rect()
        trect.center = (100, 400)
        self.screen.blit(text, trect)

    def tigerWon(self):
        fontW = pygame.font.SysFont("serif", 50)
        text = fontW.render("Tigers Won!", True, WHITE, BLACK)
        trect = text.get_rect()
        trect.center = (400, 400)
        self.screen.blit(text, trect)

    def checkNeighbours(self, pos):
        count = 0
        for n in neighbours[pos]:
            if boardState[n][1] != -1:
                count += 1
        return count == len(neighbours[pos])

    def checkTigerJump(self, pos):
        count = 0
        for n in tigerJumps[pos]:
            if boardState[n][1] != -1:
                count += 1
        return count == len(tigerJumps[pos])

    def textButton(self, text, color, x, y, width, height):
        if text == text1:
            text = pygame.font.SysFont("comicsansms", 30)
            textB = text.render(text1, True, color)
            rect = textB.get_rect()
            rect.center = ((x + (width / 2)), (y + (height / 2)))
            screen.blit(textB, rect)

        elif text == text2:
            text = pygame.font.SysFont("comicsansms", 30)
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
        else:
            pygame.draw.rect(screen, color2, (x, y, width, height))


game = GamePlay(1200, 800)

menu = True
running = True

tigerPositions = [(400, 200), (378, 331), (422, 334)]
goatPositions = []

user_text = ''

while running:

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

        screen.blit(picture, (0, 0))


        game.buttons("Start Game", 560, 500, 168, 50, LIME, GREEN, action="Play")
        game.buttons("Quit", 600, 570, 80, 50, YELLOW, LIGHT_YELLOW, action="Quit")

        game.textButton(text1, BLACK, 610, 500, 70, 50)
        game.textButton(text2, BLACK, 600, 570, 70, 50)
        pygame.display.update()

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

    if not game.v:
        game.invalid()

    if game.tigersCornered == 3:
        game.goatsWon()

    if game.goatsCaptured == 5:
        game.tigerWon()

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