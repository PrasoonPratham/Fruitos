# import pygame
import pygame

# initialize game engine
pygame.init()

window_width=480
window_height=480

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Fruitos")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("assets/background.png").convert()

while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)