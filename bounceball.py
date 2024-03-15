import pygame
from pygame.draw import circle

pygame.init()

window_1 = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
dt = 1
speed = pygame.Vector2(0, 30)  # Set horizontal speed to 0
player_pos = pygame.Vector2(window_1.get_width() / 2, window_1.get_height() / 2)
running = True
ball_radius =  40
while running:
    window_1.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    player_pos += speed * dt
    ball = pygame.draw.circle(window_1, (150, 150, 200), (int(player_pos.x), int(player_pos.y)), ball_radius)

    # Check for collision with window boundaries and reverse the speed if needed
    if player_pos.y < ball_radius or player_pos.y > window_1.get_height() - ball_radius:
        speed.y *= -1

    pygame.display.flip()
    dt = clock.tick(60) / 100  # Use milliseconds instead of frames per second

pygame.quit()
