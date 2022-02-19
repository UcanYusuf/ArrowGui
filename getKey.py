import pygame
import sys

#pygame.init()
#win = pygame.display.set_mode((400, 140))

#font = pygame.font.SysFont('Arial', 50)

def getKey(win, font, keyInput):
    if keyInput[119]:  # W
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(70, 5, 60, 60))
        win.blit(font.render('W', True, (0, 0, 0)), (80, 10))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(70, 5, 60, 60))
        win.blit(font.render('W', True, (0, 0, 0)), (80, 10))

    if keyInput[97]:  # A
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(5, 70, 60, 60))
        win.blit(font.render('A', True, (0, 0, 0)), (20, 70))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(5, 70, 60, 60))
        win.blit(font.render('A', True, (0, 0, 0)), (20, 70))

    if keyInput[115]:  # S
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(70, 70, 60, 60))
        win.blit(font.render('S', True, (0, 0, 0)), (85, 70))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(70, 70, 60, 60))
        win.blit(font.render('S', True, (0, 0, 0)), (85, 70))

    if keyInput[100]:  # D
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(135, 70, 60, 60))
        win.blit(font.render('D', True, (0, 0, 0)), (150, 70))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(135, 70, 60, 60))
        win.blit(font.render('D', True, (0, 0, 0)), (150, 70))

    if keyInput[1073741906]:  # UP
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(270, 5, 60, 60))
        win.blit(font.render('▲', True, (0, 0, 0)), (282, 5))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(270, 5, 60, 60))
        win.blit(font.render('▲', True, (0, 0, 0)), (282, 5))

    if keyInput[1073741904]:  # LEFT
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(205, 70, 60, 60))
        win.blit(font.render('◄', True, (0, 0, 0)), (208, 73))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(205, 70, 60, 60))
        win.blit(font.render('◄', True, (0, 0, 0)), (208, 73))

    if keyInput[1073741905]:  # DOWN
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(270, 70, 60, 60))
        win.blit(font.render('▼', True, (0, 0, 0)), (282, 73))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(270, 70, 60, 60))
        win.blit(font.render('▼', True, (0, 0, 0)), (282, 73))

    if keyInput[1073741903]:  # RIGHT
        pygame.draw.rect(win, [220, 30, 30], pygame.Rect(335, 70, 60, 60))
        win.blit(font.render('►', True, (0, 0, 0)), (350, 73))
    else:
        pygame.draw.rect(win, [255, 100, 0], pygame.Rect(335, 70, 60, 60))
        win.blit(font.render('►', True, (0, 0, 0)), (350, 73))

    pygame.display.update()
