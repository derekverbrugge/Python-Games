# Import necessary modules
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player's spaceship
player_image = pygame.image.load("player.png")
player_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
player_speed = 5

# Set up the enemy aliens
enemy_image = pygame.image.load("enemy.png")
enemy_pos = (random.randint(0, SCREEN_WIDTH - 50), 0)
enemy_speed = 3

# Set up the game loop
running = True
while running:
    # Check for player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos = (player_pos[0] - player_speed, player_pos[1])
            if event.key == pygame.K_RIGHT:
                player_pos = (player_pos[0] + player_speed, player_pos[1])
            if event.key == pygame.K_SPACE:
                pass  # TODO: Implement player shooting

    # Update the enemy's position
    enemy_pos = (enemy_pos[0], enemy_pos[1] + enemy_speed)
    if enemy_pos[1] > SCREEN_HEIGHT:
        enemy_pos = (random.randint(0, SCREEN_WIDTH - 50), 0)

    # TODO: Implement collision detection

    # Draw the game objects on the screen
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(player_image, player_pos)  # Draw the player's spaceship
    screen.blit(enemy_image, enemy_pos)  # Draw the enemy aliens
    pygame.display.flip()  # Update the screen

    # Limit the frame rate
    clock.tick(60)
    
# This program sets up a basic space shooter game, with a player's spaceship that can be controlled using the left and right arrow keys, 
# and enemy aliens that move down the screen. The program does not yet include features such as shooting or collision detection, 
# which you can add as needed.

# To use this program, you will need to install the pygame library and have an image file named player.png and enemy.png 
# in the same directory as the program. You can customize the game by changing the values of the various game variables, 
# such as the screen size, player and enemy speeds, and image files used.
