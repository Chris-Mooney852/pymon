import pygame
from spritesheet import SpriteStripAnim
import random
from poop import poop_group

class Digimon(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()

        self.isEgg = True
        self.timeToDigivolve = 500
        self.timeSinceLastEvolution = 0
        self.timeToPoop = random.randint(2000, 3000)
        self.timeSinceLastPoop = 0
        self.hasPooped = False

        self.animation = SpriteStripAnim('./assets/eggs/egg.png', (0, 0, 64, 64), 2, (138, 111, 48), True, 20)

        self.image = self.animation.next()
        
        self.rect = self.image.get_rect(center=pos)
    
    def update(self, screen):
        self.image = self.animation.next()
        self.timeSinceLastEvolution += 1
        self.timeSinceLastPoop += 1

        if self.timeSinceLastEvolution == self.timeToDigivolve:
            self.animation = SpriteStripAnim('./assets/digimon/Chibomon.png', (0, 0, 64, 64), 2, (138, 111, 48), True, 20)
            self.timeSinceLastEvolution = 0

        if self.timeSinceLastPoop >= self.timeToPoop or self.hasPooped:
            self.poop(screen)
            self.timeSinceLastPoop = 0
            self.hasPooped = True

    def poop(self, screen):
        poop_group.draw(screen)