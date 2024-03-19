import pygame
import sys
from game import run_game
from menu import main_menu

pygame.init()

if __name__ == "__main__":
    current_screen = "menu"  # Démarre avec le menu principal

    # Charger la musique de fond
    pygame.mixer.music.load("sfx/music/game_music.wav")
    pygame.mixer.music.play(-1)  # Jouer la musique en boucle
    pygame.mixer.music.set_volume(0.2)

    while True:
        if current_screen == "menu":
            current_screen = main_menu()  # Affiche le menu principal et met à jour le statut du jeu

        elif current_screen == "game":
            enemies = []  # Initialise la liste des ennemis
            current_screen = run_game(enemies)  # Lance le jeu et met à jour le statut du jeu

    