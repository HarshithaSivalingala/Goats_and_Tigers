import  pygame
import sys

pygame.init()
clock = pygame.time.clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(200, 200, 140, 32)
color = pygame.Color('Black')
active = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos)
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_BACKSPACE:
                user_text = user_text[: -1]
            else:
                user_text += event.unicode

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, input_rect, 3)
    text_surface = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()
    clock.tick(60)
