import random
from display import *


class Cactus(pygame.sprite.Sprite):
    def __init__(self, speed=5, size_x = -1, size_y = -1):
        pygame.sprite.Sprite.__init__(self, self.containers) # creates sprite
        self.image, self.rect = load_sprites('cacti-small.png', 3,
                                                       1, size_x, size_y)
        self.rect.bottom = int(0.98*height) # positions cacti on ground
        self.rect.left = width + self.rect.width # pos off screen
        self.image = self.image[random.randrange(0,3)] # random sprite
        self.movement = [-1*speed, 0] # moves left

    def draw(self):
        screen.blit(self.image, self.rect) # draws cactus on screen

    def update(self):
        self.rect = self.rect.move(self.movement) # moves cactus

        if self.rect.right < 0: # deletes if moved off screen
            self.kill()
