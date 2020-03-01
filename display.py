import os
import pygame
from pygame import *


pygame.init() # Initialize pygame

background_color = (235, 235, 235)
screen_size = (width, height) = (600, 150)
screen = pygame.display.set_mode(screen_size) # Sets screen width/height
pygame.display.set_caption("T-Rex-Run") # Sets window caption/title

FPS = 60
clock = pygame.time.Clock()
gravity = 0.6
high_score = 0

def load_image(filename, width = -1, height = -1):
    path = os.path.join('sprites', filename) # Gets path of sprites in its directory
    image = pygame.image.load(path).convert() # Loads image from file name and convert it into pixel format

    colorkey = image.get_at((0, 0)) # Gets background color

    # Set background to transparent
    # RLEACCEL is a flag that makes the image render faster
    image.set_colorkey(colorkey, RLEACCEL)

    # Scales the image if needed
    if width != -1 or height != -1:
        image = pygame.transform.scale(image, (width, height))

    # Returns the image and the image rectangle
    return (image, image.get_rect())

def load_sprites(filename, sprites_horiz, sprites_vert, width = -1, height = -1):
    path = os.path.join('sprites', filename) # Gets path of sprites in its directory
    spritesheet = pygame.image.load(path).convert() # Loads image from file name and convert it into pixel format

    sheet_rect = spritesheet.get_rect() # Stores width/height of sprite sheet

    sprites = [] # Creates an array of sprites

    sizex = sheet_rect.width / sprites_horiz # Width of each sprite
    sizey = sheet_rect.height / sprites_vert # Height of each sprite

    # Loops through each sprite
    for i in range(0, sprites_vert):
        for j in range(0, sprites_horiz):
            vert_pos = i * sizey # y-position in sheet
            horiz_pos = j * sizex # x-position in sheet
            # Stores sprite position, width, and height
            sprite_rect = pygame.Rect((horiz_pos, vert_pos, sizex, sizey))
            sprite = pygame.Surface(sprite_rect.size).convert() # Gets surface for sprite and convert it into pixel format
            sprite.blit(spritesheet, (0,0), sprite_rect) # Draws sprite out

            colorkey = sprite.get_at((0,0)) # Color at bottom right
            sprite.set_colorkey(colorkey, RLEACCEL)

            if width != -1 or height != -1: # Scales appropriately
                sprite = pygame.transform.scale(sprite, (width, height))

            sprites.append(sprite) # Appends sprite to sprite array

    sprite_size = sprites[0].get_rect() # width/height of a single sprite

    return sprites, sprite_size # Returns all sprites and size of each sprite


def disp_gameOver_msg(retry_btn_image, gameover_image):
    retry_btn_rect = retry_btn_image.get_rect()
    retry_btn_rect.centerx = width / 2
    retry_btn_rect.top = height * 0.52

    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx = width / 2
    gameover_rect.centery = height * 0.35

    screen.blit(retry_btn_image, retry_btn_rect)
    screen.blit(gameover_image, gameover_rect)
