# Imports
import pygame
from gpiozero import Button
from time import sleep

# Initialise pygame
pygame.init()

# Configure Buttons
key1 = Button(21)
key2 = Button(20)
key3 = Button(16)

up = Button(6)
down = Button(19)
left = Button(5)
right = Button(26)
press = Button(13)

# Set up the drawing window
screen = pygame.display.set_mode([128, 128], pygame.FULLSCREEN);

# Set FPS
fps = pygame.time.Clock()

# Hide mouse
pygame.mouse.set_visible(False)

x = 64
y = 64

class Digimon(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()

        self.image = pygame.image.load('./assets/eggs/digitama_mem.gif').convert_alpha()
        
        self.rect = self.image.get_rect(center=pos)


egg = Digimon((64, 64))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (64, 64), 16)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
