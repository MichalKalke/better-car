import pygame as pg
from pygame import QUIT

pg.init()

width, height = 800, 480
window = pg.display.set_mode((width, height))
pg.display.set_caption('Perfect Shifting')

background = pg.image.load('images/carbon.jpg')
background = pg.transform.scale(background,(width, height))

# button


# game loop
running = True
while running:
    window.blit(background,(0,0))
    # event handler
    for event in pg.event.get():
        # quit game
        if event.type == QUIT:
            running = False
    pg.display.update()
pg.quit()
