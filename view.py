import pygame as pg
import pygame.mouse
from pygame import QUIT

pg.init()

# constant
width, height = 800, 480
white = (255, 255, 255)

window = pg.display.set_mode((width, height), pg.NOFRAME)

background = pg.image.load('images/carbon.jpg')
background = pg.transform.scale(background, (width, height))
window.blit(background, (0, 0))
end = pg.image.load('images/end.png').convert_alpha()
arr = pg.PixelArray(end)
arr.replace((0, 0, 0), (184, 28, 17))
del arr

# label font
font = pg.font.Font('freesansbold.ttf', 50)


# label
class Label:
    def __init__(self, text, x, y, color, background_color, is_rect):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.backgroundColor = background_color
        self.isRect = is_rect

    def draw(self):
        if self.backgroundColor != None:
            label = font.render(self.text, True, self.color, self.backgroundColor)
        else:
            label = font.render(self.text, True, self.color)

        if self.isRect:
            box_surf = pygame.Surface(label.get_rect().inflate(20, 20).size).convert_alpha()

            box_surf.fill((255, 255, 255, 0))
            pygame.draw.rect(box_surf, [120, 0, 0], box_surf.get_rect(), 3)

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
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))

        return action


# button instances
end_btn = Button(end, 750, 50, 0.8)
test = Label("wielki test", 20, 40, white, None, True)

# game loop
running = True
while running:
    test.draw()

    if end_btn.draw():
        running = False

    # event handler
    for event in pg.event.get():
        # quit game
        if event.type == QUIT:
            running = False
    pg.display.update()
pg.quit()
