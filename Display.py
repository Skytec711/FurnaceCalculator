import pygame
import math
import sys
from GUI import GUI
import Colors

items = open("./items.txt")
itemslist = list(items)
itemsdict = {}
for item in itemslist:
    item = item [:len(item)-1]
    if item == "":
        pass
    elif item[0] == "#":
        pass
    else:
        vals = item.split("-")
        itemsdict[vals[0]] = {"xp": float(vals[1]), "image": pygame.image.load("./Images/" + vals[2])}

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 450), pygame.RESIZABLE)
size = screen.get_size()

pixelsize = 6

regularfont = pygame.font.Font("fonts/regular.otf", 25)
titlefont = pygame.font.Font("fonts/regular.otf", 75)

gui = GUI(size[0] - pixelsize * 2, size[1] - pixelsize * 2, size[0] // 2, size[1] // 2, pixelsize, screen)

page = 1

while page != 0:
    while page == 1:

        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                page = 0
            elif event.type == pygame.VIDEORESIZE:
                size = [event.w, event.h]
                size[0] = max(size[0], 800)
                size[1] = max(size[1], 450)
                screen = pygame.display.set_mode((size[0], size[1]), pygame.RESIZABLE)
                gui.resize(size[0] - pixelsize * 2, size[1] - pixelsize * 2, size[0] // 2, size[1] // 2)

        screen.fill(Colors.blue)
        gui.draw()

        pygame.display.update()
        clock.tick(60)