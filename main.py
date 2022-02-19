import pygame
import sys
from getKey import getKey

pygame.init()
win = pygame.display.set_mode((400, 140))

keyList = [97, 100, 115, 119, 1073741904, 1073741906, 1073741905, 1073741903]
reset = True

font = pygame.font.SysFont('Arial', 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keyInput = pygame.key.get_pressed()
    flag = [True if keyInput[i] == 1 else False for i in keyList]

    if True in flag:
        reset = True
        getKey(win, font, keyInput)
    else:
        if reset:
            getKey(win, font, keyInput)
            reset = False
        else:
            pass