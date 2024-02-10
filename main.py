# Basic pygame "game loop"
import pygame

import random

# pygame setup
pygame.init()
screen_width_and_height = 720
screen = pygame.display.set_mode((screen_width_and_height, screen_width_and_height))
clock = pygame.time.Clock()
running = True
dt = 0

snake_sprite_wh = 20


def pick_snake_spawn():
    range = snake_sprite_wh // 2, screen_width_and_height - snake_sprite_wh // 2, snake_sprite_wh
    return [random.randrange(*range), random.randrange(*range)]


#snake config
snake_sprite = pygame.rect.Rect(((0, 0),(snake_sprite_wh,snake_sprite_wh)))
snake_sprite.center = pick_snake_spawn()
snake_final = [snake_sprite.copy()]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER THE GAME HERE

    # pygame.draw.square(screen, "red", player_pos, 40)
    # pygame.draw.square(screen, "yellow", player_pos1, 40)
    pygame.draw.rect(screen, "yellow", snake_sprite)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()