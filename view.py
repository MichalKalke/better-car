import pygame as pg
import pygame.mouse
from pygame import QUIT

pg.init()

width, height = 800, 480
window = pg.display.set_mode((width, height))
pg.display.set_caption('Perfect Shifting')

background = pg.image.load('images/carbon.jpg')
background = pg.transform.scale(background, (width, height))
window.blit(background, (0, 0))
end = pg.image.load('images/end.png').convert_alpha()


# button
class Button():
    def __init__(self, image, x, y, scale):
        width_img = image.get_width()
        height_img = image.get_height()
        self.image = pg.transform.scale(image, (int(width_img * scale), int(height_img * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        # get mouse position
        pos = pg.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("eo")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))


# button instances
end_btn = Button(end, 750, 50,0.8)

# game loop
running = True
while running:

    end_btn.draw()

    # event handler
    for event in pg.event.get():
        # quit game
        if event.type == QUIT:
            running = False
    pg.display.update()
pg.quit()
