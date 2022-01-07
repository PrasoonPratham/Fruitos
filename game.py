# import pygame
import pygame

# initialize game engine
pygame.init()

window_width = 480
window_height = 480

animation_increment = 10
clock_tick_rate = 20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Fruitos")

dead = False

clock = pygame.time.Clock()
background_image = pygame.image.load("assets/background.png").convert()

font = pygame.font.SysFont("/assets/font.ttf", 30, True)
heart = pygame.image.load("assets/heart.png").convert_alpha()
hearts = 3

while dead == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])
    heart_x, heart_y = 380, 10

    if hearts == 3:
        screen.blit(heart, (heart_x, heart_y))
        screen.blit(heart, (heart_x + 30, heart_y))
        screen.blit(heart, (heart_x + 60, heart_y))

    if hearts == 2:
        screen.blit(heart, (heart_x + 30, heart_y))
        screen.blit(heart, (heart_x + 60, heart_y))

    if hearts == 1:
        screen.blit(heart, (heart_x + 60, heart_y))

    if hearts == 0:
        dead = True

    pygame.display.flip()
    clock.tick(clock_tick_rate)
