#!/usr/bin/env python

import pygame as pg
import pygame.mouse
from pygame import QUIT
import constants as cnst
import controller
import time

pg.init()

const = cnst.Constants()
car = cnst.Car_data()

controller.set_const(const)
controller.set_car_data(car)

# Connect obd
controller.obdThread()

# use led asyc
led = controller.ledThread()

#while not const.obd_ready:
time.sleep(1)

window = pg.display.set_mode((const.resolution.width, const.resolution.height), pg.FULLSCREEN)

background = pg.image.load('images/background.jpg')
background = pg.transform.scale(background, (const.resolution.width, const.resolution.height))
window.blit(background, (0, 0))

end = pg.image.load('images/end.png')
sport = pg.image.load('images/sport.png')
eco = pg.image.load('images/eco.png')
st = pg.image.load('images/stS.png')

# colors
white = (255,255,255)

# label font
font = pg.font.SysFont('freesansbold.ttf', 60)

# label
class Label:
    def __init__(self, text, x, y, color, background_color, is_rect, inflate_x=None, inflate_y=None):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.backgroundColor = background_color
        self.isRect = is_rect
        self.inflate_x = inflate_x if inflate_x is not None else 20
        self.inflate_y = inflate_y if inflate_y is not None else 20

    def draw(self):
        if self.backgroundColor is not None:
            label = font.render(self.text, True, self.color, self.backgroundColor)
        else:
            label = font.render(self.text, True, self.color)

        if self.isRect:
            box_surf = pygame.Surface(label.get_rect().inflate(self.inflate_x, self.inflate_y).size).convert_alpha()

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

    def update_image(self):
        if const.sport_mode is False:
            const.sport_mode = True
            image = sport

        else:
            const.sport_mode = False
            image = eco

        width_img = image.get_width()
        height_img = image.get_height()
        window.blit(background, (self.rect.x, self.rect.y))
        self.image = pg.transform.scale(image, (int(width_img), int(height_img)))
        window.blit(self.image, (self.rect.x, self.rect.y))


# button instances
end_btn = Button(end, 750, 50, 0.8)
mode_btn = Button(sport, 50, 50, 1)
st_label = Button(st, 750, 440, 1)

# label instances
engineLoadLabel = Label("Engine load", 470, 350, const.white, None, True, 27)
throttleLabel = Label("Throttle", 470, 170, white, None, True, 104)
oilTempLabel = Label("Oil", 40, 350, white, None, True, 205)
rpmLabel = Label("RPM", 40, 170, white, None, True, 165)

def renderLabels():
    engineLoadLabel.draw()
    #engineLoad.draw()
    throttleLabel.draw()
    #throttle.draw()
    oilTempLabel.draw()
    #oilTemp.draw()
    rpmLabel.draw()
    #rpm.draw()
    st_label.draw()


# game loop
running = True

#tmp
tmp = 500

def perfect_shifting():
    global running
    global tmp
    while running:
        window.blit(background, (0, 0))
        renderLabels()
        engineLoad = Label(str(car.engine_load) + " %", 580, 290, white, None, None)
        throttle = Label(str(car.throttle)+ " %", 580, 110, white, None, None)
        oilTemp = Label(str(car.oil_temp) + " °C", 150, 290, white, None, None)
        rpm = Label(str(car.rpm), 140, 110, white, None, None)
        engineLoad.draw()
        throttle.draw()
        oilTemp.draw()
        rpm.draw()

        if mode_btn.draw():
            mode_btn.update_image()

        if end_btn.draw():
            #led.pixels_off()
            const.thread_kill = True
            #led.pixels_off()
            running = False


        # event handler
        for event in pg.event.get():
            # quit game
            if event.type == QUIT:
                running = False
        pg.display.update()
    pg.quit()

perfect_shifting()
