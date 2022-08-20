import pygame

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

menuIcons = [
    status_icon, 
    meat_icon, 
    dumbbell_icon, 
    trophy_icon, 
    poop_icon, 
    lightbulb_icon, 
    bandaid_icon, 
    book_icon, 
    link_icon, 
    alert_icon
]