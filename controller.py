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
    global high_score
    gamespeed = 4
    startMenu = False
    gameOver = False
    gameQuit = False
    playerDino = Dino(44,47)
    new_ground = Ground(-1*gamespeed)
    scb = Scoreboard()
    highsc = Scoreboard(width*0.78)
    counter = 0

    # groups sprites together
    cacti = pygame.sprite.Group()
    pteras = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    last_obstacle = pygame.sprite.Group()

    # groups sprites into objects
    Cactus.containers = cacti
    Ptera.containers = pteras
    Cloud.containers = clouds

    # loads replay/game over images
    retbutton_image,retbutton_rect = load_image('replay_button.png',35,31)
    gameover_image,gameover_rect = load_image('game_over.png',190,11)

    # loads in numbers for keeping score
    temp_images,temp_rect =load_sprites('numbers.png',12,1,11,int(11*6/5))
    HI_image = pygame.Surface((22,int(11*6/5)))
    HI_rect = HI_image.get_rect()
    HI_image.fill(background_color)
    HI_image.blit(temp_images[10],temp_rect)
    temp_rect.left += temp_rect.width
    HI_image.blit(temp_images[11],temp_rect)
    HI_rect.top = height*0.1
    HI_rect.left = width*0.73

    # runs while game is not quit
    while not gameQuit:
        while startMenu:
            pass
        while not gameOver:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = True
            else:
                for event in pygame.event.get(): # quits game if necessary
                    if event.type == pygame.QUIT:
                        gameQuit = True
                        gameOver = True

                    # handles ducking
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if playerDino.rect.bottom == int(0.98*height):
                                playerDino.isJumping = True
                                if pygame.mixer.get_init() != None:
                                    jump_sound.play()
                                playerDino.movement[1] = -1*playerDino.jumpSpeed

                        if event.key == pygame.K_DOWN:
                            if not (playerDino.isJumping and playerDino.isDead):
                                playerDino.isDucking = True

                    # handles jump
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            playerDino.isDucking = False
            for c in cacti: # moves cacti on screen
                c.movement[0] = -1*gamespeed
                if pygame.sprite.collide_mask(playerDino,c):
                    playerDino.isDead = True
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            for p in pteras: # moves pteradactyl on screen
                p.movement[0] = -1*gamespeed
                if pygame.sprite.collide_mask(playerDino,p):
                    playerDino.isDead = True
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

            # creates
            if len(clouds) < 5 and random.randrange(0,300) == 10:
                Cloud(width,random.randrange(height/5,height/2))

            playerDino.update()
            cacti.update()
            pteras.update()
            clouds.update()
            new_ground.update()
            scb.update(playerDino.score)
            highsc.update(high_score)

            if pygame.display.get_surface() != None:
                screen.fill(background_color)
                new_ground.draw()
                clouds.draw(screen)
                scb.draw()
                if high_score != 0:
                    highsc.draw()
                    screen.blit(HI_image,HI_rect)
                cacti.draw(screen)
                pteras.draw(screen)
                playerDino.draw()

                pygame.display.update()
            clock.tick(FPS)

            if playerDino.isDead:
                gameOver = True
                if playerDino.score > high_score:
                    high_score = playerDino.score

            if counter%700 == 699:
                new_ground.speed -= 1
                gamespeed += 1

            counter = (counter + 1)

        if gameQuit:
            break

        while gameOver:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                gameQuit = True
                gameOver = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameQuit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameQuit = True
                            gameOver = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            gameOver = False
                            game_controller()
            highsc.update(high_score)
            if pygame.display.get_surface() != None:
                disp_gameOver_msg(retbutton_image,gameover_image)
                if high_score != 0:
                    highsc.draw()
                    screen.blit(HI_image,HI_rect)
                pygame.display.update()
            clock.tick(FPS)

    pygame.quit()
    quit()


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
