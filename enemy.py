import pygame
import random
pygame.init()

class Enemy:
    def __init__(self, min_height, max_height):
        """
        Initialise un ennemi avec une position aléatoire en hauteur.

        Args:
            min_height (int): La hauteur minimale à laquelle l'ennemi peut apparaître.
            max_height (int): La hauteur maximale à laquelle l'ennemi peut apparaître.
        """
        # Chargement de l'image de l'ennemi et création de son rectangle de collision
        self.surface = pygame.transform.scale(pygame.image.load("images/enemy/saw.png"), (45, 45))
        self.rect = self.surface.get_rect(midleft=(random.randint(950, 1000), random.randint(min_height, max_height)))

    def update(self):
        """
        Met à jour la position de l'ennemi en le déplaçant vers la gauche.
        """
        self.rect.move_ip(-5, 0)

    def draw(self, SCREEN):
        """
        Dessine l'ennemi sur l'écran.

        Args:
            SCREEN (Surface): La surface sur laquelle dessiner l'ennemi.
        """
        SCREEN.blit(self.surface, self.rect)
