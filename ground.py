from display import *


class Ground():
    def __init__(self,speed=-5):

        #loadimageandtherectanglearoundtheimage
        self.image,self.rect = load_image('ground.png')
        self.image1,self.rect1 = load_image('ground.png')

        #placethegrondatthebottomofthescreen
        self.rect.bottom = self.rect1.bottom = height
        self.rect1.left = self.rect.right#connect the two grounds

        #setthespeed
        self.speed = speed

    def draw(self):
        #renderthegroundontothescreen
        screen.blit(self.image,self.rect)
        screen.blit(self.image1,self.rect1)

    def update(self):
        #movethegroundacrossthescreen
        self.rect.left += self.speed
        self.rect1.left += self.speed

        #onceground1isoutofthescreenplaceitbehindground2
        if self.rect.right<0:
            self.rect.left = self.rect1.right

        #onceground2isoutofthescreen,placeitbehindground1
        if self.rect1.right<0:
            self.rect1.left = self.rect.right
