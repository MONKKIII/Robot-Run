import pygame
import sys
from utils import load_scores

def main_menu():
    """
    Affiche le menu principal du jeu.

    Returns:
        bool: True si le joueur choisit de quitter le jeu, False sinon.
    """
    pygame.init()

    # Initialisation de Pygame
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((900, 950))
    pygame.display.set_caption("Robot Run")

    # Chargement des scores
    scores = load_scores()

    # Chargement des sons
    play_game_sound = pygame.mixer.Sound("sfx/sound/play.wav")

    # Création de la police de texte pour le menu
    menu_font = pygame.font.SysFont(None, 48)

    # Texte du titre
    title_text = menu_font.render("Robot Run", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 50))
    SCREEN.blit(title_text, title_rect)

    # Texte pour jouer
    play_text = menu_font.render("Jouer", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
    SCREEN.blit(play_text, play_rect)

    # Chargement de l'image de la poubelle
    scoreboard_image = pygame.transform.scale(pygame.image.load("images/score_board.png"), (102, 116))
    scoreboard_image_rect = scoreboard_image.get_rect(center=(SCREEN.get_width() // 2 + 380, SCREEN.get_height() // 2 - 400))
    # Affichage de l'image de la poubelle
    SCREEN.blit(scoreboard_image, scoreboard_image_rect)

    # Texte pour quitter
    quitter_text = menu_font.render("Quitter", True, (255, 255, 255))
    quitter_rect = quitter_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 150))
    SCREEN.blit(quitter_text, quitter_rect)
    pygame.display.update()

    # Attente des actions de l'utilisateur
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Si l'utilisateur ferme la fenêtre, quitte le jeu
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Si l'utilisateur clique sur l'un des boutons du menu
                if play_rect.collidepoint(event.pos):
                    # L'utilisateur a choisi de jouer, lance le jeu
                    waiting = False
                    play_game_sound.play()
                    from game import run_game
                    run_game()
                elif scoreboard_image_rect.collidepoint(event.pos):
                    # L'utilisateur a cliqué sur l'image du tableau des scores, affiche le tableau des scores
                    from scoreboard import score_board
                    score_board(SCREEN)
                elif quitter_rect.collidepoint(event.pos):
                    # L'utilisateur a choisi de quitter le jeu
                    pygame.quit()
                    sys.exit()
