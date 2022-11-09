#!/usr/bin/env python

import pygame as pg
import pygame.mouse
from pygame import QUIT
import constants as cnst

pg.init()

const = cnst.Constants()

window = pg.display.set_mode((const.resolution.width, const.resolution.height), pg.NOFRAME)

background = pg.image.load('images/background.jpg')
background = pg.transform.scale(background, (const.resolution.width, const.resolution.height))
window.blit(background, (0, 0))
end = pg.image.load('images/end.png')

# colors
white = (255,255,255)

# label font
font = pg.font.SysFont('freesansbold.ttf', 40)

# label
class Label:
    def __init__(self, text, x, y, color, background_color, is_rect):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        print(self.color)
        self.backgroundColor = background_color
        self.isRect = is_rect

    def draw(self):
        if self.backgroundColor is not None:
            label = font.render(self.text, True, self.color, self.backgroundColor)
        else:
            label = font.render(self.text, True, self.color)

        if self.isRect:
            box_surf = pygame.Surface(label.get_rect().inflate(20, 20).size).convert_alpha()

            box_surf.fill((255, 255, 255, 1))
            pygame.draw.rect(box_surf, white, box_surf.get_rect(), 3)

            box_surf.blit(label, label.get_rect(center=box_surf.get_rect().center))
            label = box_surf

        window.blit(label, (self.x, self.y))


# button
class Button:
    def __init__(self, image, x, y, scale):
        width_img = image.get_width()
        height_img = image.get_height()
        self.image = pg.transform.scale(image, (int(width_img * scale), int(height_img * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pg.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))

        return action


# button instances
end_btn = Button(end, 750, 50, 0.8)

# label instances
test = Label("Switch mode", 20, 20, white, None, None)
engineLoadLabel = Label("Engine load", 500, 350, const.white, None, True)
engineLoad = Label(str(53) + " %", 600, 290, white, None, None)
acceleratorLabel = Label("accelerator", 500, 170, white, None, True)
accelerator = Label(str(60)+ " %", 600, 110, white, None, None)
turbochargerTempLabel = Label("Turbocharger", 40, 350, white, None, True)
turbochargerTemp = Label(str(80) + " °C", 20, 290, white, None, None)
rpmLabel = Label("RPM", 20, 170, white, None, True)
rpm = Label(str(2500), 20, 100, white, None, None)

# game loop
running = True
while running:
    #test.draw()
    engineLoadLabel.draw()
    engineLoad.draw()
    acceleratorLabel.draw()
    accelerator.draw()
    turbochargerTempLabel.draw()
    turbochargerTemp.draw()
    rpmLabel.draw()
    rpm.draw()

    if end_btn.draw():
        running = False

    # event handler
    for event in pg.event.get():
        # quit game
        if event.type == QUIT:
            running = False
    pg.display.update()
pg.quit()
