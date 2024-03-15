import pygame
import random

pygame.init()

window_size = (500, 500)
window_1 = pygame.display.set_mode(window_size)
clock_bhai = pygame.time.Clock()
dt = 0
speed = pygame.Vector2(90, 150)  
running = True
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ball_radius = 40

player_position = pygame.Vector2(window_size[0] / 2, window_size[1] / 2)

while running:
    window_1.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_position += speed * dt

    if player_position.x <= ball_radius or player_position.x >= window_size[0] - ball_radius:
        speed.x = -speed.x
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if player_position.y <= ball_radius or player_position.y >= window_size[1] - ball_radius:
        speed.y = -speed.y
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pygame.draw.circle(window_1, color, (int(player_position.x), int(player_position.y)), ball_radius)

    pygame.display.flip()
    dt = clock_bhai.tick(60) / 500

pygame.quit()