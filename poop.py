import pygame

class Poop(pygame.sprite.Sprite):
    def __init__(self, pos, imagePath) -> None:
        super().__init__()

        self.image = pygame.image.load(imagePath).convert_alpha()
        self.image.set_alpha(255)
        
        self.rect = self.image.get_rect(center=pos)



poop = Poop((112, 90), './assets/menu/poop.png')
poop_group = pygame.sprite.RenderPlain()
poop_group.add(poop)
