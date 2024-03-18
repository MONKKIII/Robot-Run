import pygame
import sys
from game import run_game
from menu import main_menu

pygame.init()

if __name__ == "__main__":
    current_screen = "menu"  # Démarre avec le menu principal

    while True:
        if current_screen == "menu":
            current_screen = main_menu()  # Affiche le menu principal et met à jour le statut du jeu

        elif current_screen == "game":
            enemies = []  # Initialise la liste des ennemis
            current_screen = run_game(enemies)  # Lance le jeu et met à jour le statut du jeu

    