import pygame as pg

BLACK = (0,0,0)

class Paddle(pg.sprite.Sprite):

    def __init__(self,color,width,height):
        super().__init__()

        self.image = pg.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw paddle

        pg.draw.rect(self.image,color,[0,0,width,height])


        self.rect = self.image.get_rect()

        #move functions

    def moveleft(self,pixels):
        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect.x = 0

    def moveright(self,pixels):
        self.rect.x += pixels

        if self.rect.x > 700:
            self.rect.x = 700
