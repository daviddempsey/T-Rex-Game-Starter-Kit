from display import *

class Dino():
    def __init__(self, size_x = -1, size_y = -1):
        # This loads standing dinosaur sprites
        ### TODO 1: Fill in missing dinosaur sprite file
        self.images, self.rect = load_sprites('?.png', 5, 1, size_x, \
                                                 size_y)
        # This loads ducking dinosaur sprites
        ### TODO 2: Fill in missing ducking dinosaur sprite file
        self.images1, self.rect1 = load_sprites('?.png',\
                                                        2, 1, 59, size_y)

        self.rect.bottom = int(0.98*height) # sets bottom y-pos
        self.rect.left = width/15 # sets left pos of dinosaur

        self.image = self.images[0] # initial dinosaur sprite

        self.index = 0 # sprite index in sprite sheet
        self.counter = 0 # keeps track of time passed
        self.score = 0 # keeps track of score

        # Initial state conditions
        ### TODO 3: What should these boolean values be?
        self.isJumping = ?
        self.isDead = ?
        self.isDucking = ?
        self.isBlinking = ?

        self.movement = [0, 0] # x/y movement of dinosaur
        self.jumpSpeed = 11.5

        # Stores width of ducking and standing dino
        ### TODO 4: What attribute sets width for rect and rect1?
        self.standing_width = self.rect.?
        self.duck_width = self.rect1.?

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
            ### TODO 5: Which index dinosaur is the dead dinosaur in the spritesheet?
            self.index = ?

        if not self.isDucking:
            self.image = self.images[self.index] # adjusts sprite accordingly
            self.rect.width = self.standing_width
        else:
            # adjusts sprite to ducking sprite
            self.image = self.images1[(self.index) % 2]
            self.rect.width = self.duck_width

        self.rect = self.rect.move(self.movement) # moves dino accordingly
        self.checkbounds() # ensures dino stays on screen

        if not self.isDead and self.counter % 7 == 6 \
                and self.isBlinking == False:
            self.score += 1 # score increases every update
            if self.score % 100 == 0 and self.score != 0: # checkpoint reached
                if pygame.mixer.get_init() != None:
                     checkPoint_sound.play()

        self.counter += 1 # increases time counter by 1
