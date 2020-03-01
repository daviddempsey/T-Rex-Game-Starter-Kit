from display import *




class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image, self.rect = load_image('cloud.png', int(90*30/42), 30)
        self.speed = 1 # sets cloud speed attribute
        self.rect.left = x # x-pos of cloud
        self.rect.top = y # y-pos of cloud
        self.movement = [-1*self.speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect) # draws cloud on screen

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill() # removes cloud if out of bounds
