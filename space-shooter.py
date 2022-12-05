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

# Set up the player's bullets
bullet_image = pygame.image.load("bullet.png")
bullet_speed = 10
bullets = []

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
                # Create a new bullet and add it to the list of bullets
                bullet = {
                    "pos": (player_pos[0] + 25, player_pos[1]),  # Center the bullet horizontally
                    "vel": bullet_speed,
                }
                bullets.append(bullet)

    # Update the enemy's position
    enemy_pos = (enemy_pos[0], enemy_pos[1] + enemy_speed)
    if enemy_pos[1] > SCREEN_HEIGHT:
        enemy_pos = (random.randint(0, SCREEN_WIDTH - 50), 0)

    # Update the position of each bullet
    for bullet in bullets:
        bullet["pos"] = (bullet["pos"][0], bullet["pos"][1] - bullet["vel"])

    # Check for collisions between bullets and the enemy
    for bullet in bullets:
        if (
            bullet["pos"][0] >= enemy_pos[0]
            and bullet["pos"][0] <= enemy_pos[0] + 50
            and bullet["pos"][1] >= enemy_pos[1]
            and bullet["pos"][1] <= enemy_pos[1] + 50
        ):
            # Remove the bullet and the enemy when they collide
            bullets.remove(bullet)
            enemy_pos = (random.randint(0, SCREEN_WIDTH - 50), 0)

    # Draw the game objects on the screen
        screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(player_image, player_pos)  # Draw the player's spaceship
    screen.blit(enemy_image, enemy_pos)  # Draw the enemy aliens

    # Draw each bullet
    for bullet in bullets:
        screen.blit(bullet_image, bullet["pos"])

    pygame.display.flip()  # Update the screen

    # Limit the frame rate
    clock.tick(60)
    

