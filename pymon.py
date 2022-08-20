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

from menu import menuIcons
from digimon import Digimon

# Set FPS
fps = pygame.time.Clock()

# Hide mouse
pygame.mouse.set_visible(False)

x = 64
y = 64

currently_active = -1



digimon = Digimon((64, 64))

digimon_group = pygame.sprite.RenderPlain()
menu_group = pygame.sprite.RenderPlain()

digimon_group.add(digimon)
menu_group.add(menuIcons)

def set_menu():
    global currently_active
    if currently_active == -1:
        for index, icon in enumerate(menuIcons):
                icon.activate(False)
    else:
        for index, icon in enumerate(menuIcons):
            if index == currently_active:
                icon.activate(True)
            else:
                icon.activate(False)


def increment_menu():
    global currently_active
    currently_active += 1
    if currently_active > 9:
        currently_active = 9

    set_menu()

def decrement_menu():
    global currently_active
    currently_active -= 1

    if currently_active < 0:
        currently_active = 0

    set_menu()

def clear_menu():
    global currently_active
    currently_active = -1

    set_menu()

def handle_input():
    # if right.is_pressed:
    #     active_index += 1
    # if left.is_pressed:
    #     active_index -= 1

    right.when_pressed = increment_menu
    left.when_pressed = decrement_menu
    key3.when_pressed = clear_menu

    
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
    digimon_group.draw(screen)
    menu_group.draw(screen)

    handle_input()

    digimon.update(screen)

    # Flip the display
    pygame.display.flip()

    fps.tick(30)

# Done! Time to quit.
pygame.quit()
