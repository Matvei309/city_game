import pygame

pygame.init()

def print_text_pygame(string, size, win, coords, color):
    font_txt = pygame.font.SysFont('sfnsmonoitalic', size * 20)
    text     = font_txt.render(string, 1, color)
    x = coords[0] - text.get_width()  // 2
    y = coords[1] - text.get_height() // 2
    win.blit(text, (x, y))

