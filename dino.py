from display import *


#gravity = 0.6
#screen_size = (width, height) = (600, 150)
#screen = pygame.display.set_mode(screen_size)

class Dino():
    def __init__(self, size_x = -1, size_y = -1):
        # loads standing imagesaur sprites
        self.images, self.rect = load_sprites('dino.png', 5, 1, size_x, \
                                                 size_y)
        # loads ducking imagesaur sprites
        self.images1, self.rect1 = load_sprites('dino_ducking.png',\
                                                        2, 1, 59, size_y)
        self.rect.bottom = int(0.98*height) # sets bottom y-pos ?
        self.rect.left = width/15 # sets left pos of imagesaur

        self.image = self.images[0] # initial imagesaur sprite

        self.index = 0 # sprite index in sprite sheet
        self.counter = 0 # keeps track of time passed
        self.score = 0 # keeps track of score

        # initial state conditions
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.isBlinking = False

        self.movement = [0, 0] # x/y movement of imagesaur
        self.jumpSpeed = 11.5

        # stores width of ducking and standing dino
        self.standing_width = self.rect.width
        self.duck_width = self.rect1.width

    # draws out dino on screen
    def draw(self):
        screen.blit(self.image, self.rect)

    # prevents dino from jumping out of bounds
    def checkbounds(self):
        if self.rect.bottom > int(0.98*height):
            self.rect.bottom = int(0.98*height)
            self.isJumping = False

    def update(self):
        if self.isJumping: # accounts for gravity
            self.movement[1] = self.movement[1] + gravity
            self.index = 0

        elif self.isBlinking:
            if self.index == 0: # changes sprite to blinking dino
                if self.counter % 400 == 399:
                    self.index = (self.index + 1) % 2 # should be 1
            else: # changes back to eyes open dino
                if self.counter % 20 == 19:
                    self.index = (self.index + 1) % 2 # should be 0

        elif self.isDucking:
            if self.counter % 5 == 0: # changes sprite index to move feet
                self.index = (self.index + 1) % 2
        else: # if dino isn't ducking and just running
            if self.counter % 5 == 0: # changes sprite index to move feet
                self.index = (self.index +1) % 2 + 2

        if self.isDead: # changes sprite to dead dino
            self.index = 4

        if not self.isDucking:
            self.image = self.images[self.index] # adjusts sprite accordingly
            self.rect.width = self.standing_width
        else:
            # adjusts sprite to ducking sprite
            self.image = self.images1[(self.index) % 2]
            self.rect.width = self.duck_width

        self.rect = self.rect.move(self.movement) # moves dino accordingly # Changed dino to rect -Alan :)
        self.checkbounds() # ensures dino stays on screen

        if not self.isDead and self.counter % 7 == 6 \
                and self.isBlinking == False:
            self.score += 1 # score increases every update
            #if self.score % 100 == 0 and self.score != 0: # checkpoint reached
                #if pygame.mixer.get_init() != None:
                    # checkPoint_sound.play()

        self.counter += 1 # increases time counter by 1
