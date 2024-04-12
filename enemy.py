import pygame
import random
pygame.init()

class Enemy:
    def __init__(self, min_height, max_height):
        self.surface = pygame.transform.scale(pygame.image.load("images/enemy/saw.png"), (45, 45))
        self.rect = self.surface.get_rect(midleft=(random.randint(950, 1000), random.randint(min_height, max_height)))

    def update(self):
        self.rect.move_ip(-5, 0)

    def draw(self, SCREEN):
        SCREEN.blit(self.surface, self.rect)
