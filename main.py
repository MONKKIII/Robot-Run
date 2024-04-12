import pygame
import sys
from game import run_game
from menu import main_menu

pygame.init()

if __name__ == "__main__":
    current_SCREEN = "menu"  # Démarre avec le menu principal

    while True:
        if current_SCREEN == "menu":
            current_SCREEN = main_menu()  # Affiche le menu principal et met à jour le statut du jeu

        elif current_SCREEN == "game":
            enemies = []  # Initialise la liste des ennemis
            current_SCREEN = run_game(enemies)  # Lance le jeu et met à jour le statut du jeu