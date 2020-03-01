import random
from display import *





class Ptera(pygame.sprite.Sprite):
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_sprites('ptera.png', 2, 1, sizex,sizey)
        # various possible heights for pteradactyl
        self.ptera_height = [height*0.82, height*0.75, height*0.60]
        self.rect.centery = self.ptera_height[random.randrange(0,3)]

        self.rect.left = width + self.rect.width # pos off screen
        self.image = self.images[0] # sets initial ptera sprite
        self.movement = [-1*speed, 0] # sets movement speed
        self.index = 0
        self.counter = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index+1)%2
        # makes wings flap by changing sprite
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter += 1
        if self.rect.right < 0:
            self.kill() # removes ptera if out of bounds
