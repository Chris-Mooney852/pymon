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

currently_active = 0

class Digimon(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()

        self.image = pygame.image.load('./assets/eggs/digitama_mem.gif')
        
        self.rect = self.image.get_rect(center=pos)

class MenuIcon(pygame.sprite.Sprite):
    def __init__(self, pos, imagePath) -> None:
        super().__init__()

        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image.set_alpha(10)
        
        self.rect = self.image.get_rect(center=pos)

    def activate(self, active):
        if active:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(10)


digimon = Digimon((64, 64))

# Top row icons
status_icon = MenuIcon((16, 16), './assets/menu/status.png')
meat_icon = MenuIcon((38, 16), './assets/menu/meat.png')
dumbbell_icon = MenuIcon((64, 16), './assets/menu/dumbbell.png')
trophy_icon = MenuIcon((88, 16), './assets/menu/trophy.png')
poop_icon = MenuIcon((112, 16), './assets/menu/poop.png')

# Bottom row icons
lightbulb_icon = MenuIcon((16, 112), './assets/menu/light-bulb.png')
bandaid_icon = MenuIcon((38, 112), './assets/menu/band-aid.png')
book_icon = MenuIcon((64, 112), './assets/menu/open-book.png')
link_icon = MenuIcon((88, 112), './assets/menu/link.png')
alert_icon = MenuIcon((112, 112), './assets/menu/bell.png')

digimon_group = pygame.sprite.RenderPlain()
menu_group = pygame.sprite.RenderPlain()

menu = [status_icon, meat_icon, dumbbell_icon, trophy_icon, poop_icon, lightbulb_icon, bandaid_icon, book_icon, link_icon, alert_icon]

digimon_group.add(digimon)
menu_group.add(menu)

status_icon.activate(True)

def increment_menu():
    global currently_active
    currently_active += 1
    if currently_active > 9:
        currently_active = 9

    for index, icon in enumerate(menu):
        if index == currently_active:
            icon.activate(True)
        else:
            icon.activate(False)

def decrement_menu():
    global currently_active
    currently_active -= 1

    if currently_active < 0:
        currently_active = 0

    for index, icon in enumerate(menu):
        if index == currently_active:
            icon.activate(True)
        else:
            icon.activate(False)


def handle_input():
    # if right.is_pressed:
    #     active_index += 1
    # if left.is_pressed:
    #     active_index -= 1

    right.when_pressed = increment_menu
    left.when_pressed = decrement_menu

    
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

    # Flip the display
    pygame.display.flip()

    fps.tick(30)

# Done! Time to quit.
pygame.quit()
