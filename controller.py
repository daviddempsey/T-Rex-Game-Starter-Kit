from cactus import *
from cloud import *
from dino import *
from ground import *
from ptera import *
from scoreboard import *

jump_sound = pygame.mixer.Sound('sprites/jump.wav')
die_sound = pygame.mixer.Sound('sprites/die.wav')
checkPoint_sound = pygame.mixer.Sound('sprites/checkPoint.wav')


def game_controller():

    global high_score #tracks highest score across multiple game plays
    gamespeed = 4 #initialize game speed
    playerDino = Dino(44,47) #creates a dino object
    new_ground = Ground(-1*gamespeed) #creates a ground, passing speed as the parameter
    scb = Scoreboard() #creates the scoreboard to display the score during the game
    highsc = Scoreboard(width*0.78) #creates a scoreboard to display the highest score
    counter = 0 #game environment counter that controls when different sprites will appear in the game

    #Initialize the state conditions
    ###TODO 1: Fill in the boolean values of these variables
    gameOver = ?
    gameQuit = ?

    

    # groups sprites together
    cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    last_obstacle = pygame.sprite.Group()

    # groups sprites into objects
    Cactus.containers = cacti
    Ptera.containers = pteras
    Cloud.containers = clouds

    retbutton_image,retbutton_rect = load_image('replay_button.png',35,31) #load replay image
    gameover_image,gameover_rect = load_image('game_over.png',190,11) #load gameover image

    # loads and display numbers for keeping score
    temp_images,temp_rect =load_sprites('numbers.png',12,1,11,int(11*6/5))#load the numbers
    HI_image = pygame.Surface((22,int(11*6/5))) #create the image of high score
    HI_rect = HI_image.get_rect() #get the rectangle around the high score image
    HI_image.fill(background_color) #fill in the background color
    HI_image.blit(temp_images[10],temp_rect) #draw the image onto the screen
    temp_rect.left += temp_rect.width #set the left position of the image
    HI_image.blit(temp_images[11],temp_rect) #draw the image onto the screen
    HI_rect.top = height*0.1 #position the high score image by aligning the top
    HI_rect.left = width*0.73 #position the high score image by aligning the left

    # runs while game is not quit
    while not gameQuit:

        #runs while game is not over

        while not gameOver:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                ###TODO 2: What should the boolean values of these variables be?
                gameQuit = ?
                gameOver = ?
            else:
                for event in pygame.event.get(): # quits game if necessary
                    ###TODO 3: What should the event pygame event type be?
                    if event.type == pygame.?:
                        gameQuit = True
                        gameOver = True

                    # when a key is pressed
                    if event.type == pygame.KEYDOWN:
                        #when user presses space
                        if event.key == pygame.K_SPACE:
                            #check if playerDino is on the ground
                            if playerDino.rect.bottom == int(0.98*height):

                                ###TODO 4: What should the boolean value this variable be?
                                playerDino.? = True

                                #check if pygame.mixer (sound module) is initialized
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()

                                ###TODO 5: Which direction should Dino move?
                                playerDino.movement[?] = -1*playerDino.jumpSpeed

                        ###TODO 6: Write the conditional for ducking dinosaur
                        if ?:
                            if not (playerDino.isJumping and playerDino.isDead):
                                ###TODO 7: What should the boolean value this variable be?
                                playerDino.isDucking = ?

                    # handles jump
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            playerDino.isDucking = False


            for c in cacti: # moves each cactus on the screen
                c.movement[0] = -1*gamespeed #moves cactus in the x direction

                #check if the cactus is colliding with playerDino
                if pygame.sprite.collide_mask(playerDino,c):

                    ##TODO 8: What happens when playerDino collides with cactus?
                    playerDino.? = True

                    #check if pygame.mixer (sound module) is initialized
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            for p in pteras: # moves pteradactyls on screen
                p.movement[0] = -1*gamespeed #moves pteradactyl in the x direction

                #check if the cactus is colliding with playerDino
                if pygame.sprite.collide_mask(playerDino,p):

                    ##TODO 9: What happens when playerDino collides with the pteradactyl?
                    playerDino.? = True

                    #check if pygame.mixer (sound module) is initialized
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            # keeps adding obstacles
            if len(cacti) < 2:
                if len(cacti) == 0:
                    last_obstacle.empty()
                    last_obstacle.add(Cactus(gamespeed,40,40))
                else:
                    for l in last_obstacle:
                        if l.rect.right < width*0.7 and random.randrange(0,50) == 10:
                            last_obstacle.empty()
                            last_obstacle.add(Cactus(gamespeed, 40, 40))

            # keeps adding pteradactyls
            if len(pteras) == 0 and random.randrange(0,200) == 10 and counter > 500:
                for l in last_obstacle:
                    if l.rect.right < width*0.8:
                        last_obstacle.empty()
                        last_obstacle.add(Ptera(gamespeed, 46, 40))

            # keeps adding clouds
            if len(clouds) < 5 and random.randrange(0,300) == 10:
                Cloud(width,random.randrange(height/5,height/2))

            scb.update(playerDino.score)#update score of current game
            highsc.update(high_score)#update high score
            ###TODO 10: Call updates

            #render the sprites onto the screen
            if pygame.display.get_surface() != None:
                screen.fill(background_color) #fill in the background color
                new_ground.draw() #render the ground onto the screen
                clouds.draw(screen) #render the cloud onto the screen
                scb.draw() #render the scoreboard onto the screen
                if high_score != 0:
                    highsc.draw() #render the high score scoreboard onto the screen
                    screen.blit(HI_image,HI_rect)
                cacti.draw(screen) #render the cactus onto the screen
                pteras.draw(screen) #render the pteradactyls onto the screen
                playerDino.draw() #render the dino onto the screen

                #update the display
                pygame.display.update()
            clock.tick(FPS)

            if playerDino.isDead:
                ###TODO 11: Fill in the boolean state of gameOver
                gameOver = ?

                ###TODO 12: What should the comparison operator be?
                if playerDino.score ? high_score:
                    high_score = playerDino.score

            if counter%700 == 699:
                new_ground.speed -= 1
                gamespeed += 1

            counter = (counter + 1)

        if gameQuit:
            break

        #handles gameover
        while gameOver:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = False #exit gameover loop
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameQuit = True
                        gameOver = False #exit gameover loop
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameQuit = True
                            gameOver = False #exit gameover loop

                        #when user wants to restart the game
                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            gameOver = False
                            game_controller() #run game_controller again to restart the game

            highsc.update(high_score) #updat the high score
            if pygame.display.get_surface() != None:
                disp_gameOver_msg(retbutton_image,gameover_image) #display gameover quiz
                if high_score != 0:
                    highsc.draw() #render high score onto the screen
                    screen.blit(HI_image,HI_rect)
                pygame.display.update() #update the display
            clock.tick(FPS)


    pygame.quit() #quit pygame
    quit() #quit the program



def intro_screen():
    """
    What you'll need for a basic intro screen:
        - Initialize your dino and position it on the screen
        - Display static images of the ground, logo, and callout image
        - Keep track of whether the game has started
    """
    ### TODO #1: Displaying the dinosaur ###
    temp_dino = ? # Initialize your T-Rex with a sizex of 44 and sizey of 47
    gameStart = ? #Should this be T/F?

    ### TODO #2: Loading the call out image ###
    callout, callout_rect = ? # width = 196 height = 45

    # Set the left property to scale the width by 0.05
    # Set the top property to scale the height by 0.4
    
    ### TODO #3: Loading the ground sprite ###
    temp_ground, temp_ground_rect = ? # horizontal = 15, vertical = 1, width = -1, height = -1
    
    # Set the left property to scale the width by 0.05
    # Set the bottom property to equal the height of the sprite

    ### TODO #4: Loading the logo image ###
    logo, logo_rect = ? # width = 240, height = 40
    
    # Set the centerx property to scale the width by 0.06
    # Set the centery property to scale the height by 0.06
    
    ### WHILE THE GAME HASN'T STARTED YOU'LL WANT TO DISPLAY IMAGES/SPRITES ON THE SCREEN ###
    while not gameStart:
        if pygame.display.get_surface() == None:
            print("Couldn't load display surface")
            return True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    ### TODO #5: Make the T-Rex jump on a key press to start the game ###
                    # Write an if statement to make your dino jump on a keypress of your choice
                    temp_dino.isJumping = ? # Should this be T/F?
                    temp_dino.movement = -1 * temp_dino.jumpSpeed


        # Update your dino to show it jumping/transitioning to the gameplay screen



        ### TODO #6: Load the game screen ###
        if pygame.display.get_surface() != None:





        clock.tick(FPS)

        # Write an if statement under this comment to start the game when your dino lands after jumping
            gameStart = ? # Should this be T/F?

def main():
    isGameQuit = intro_screen()
    if not isGameQuit:
        game_controller()

main()
