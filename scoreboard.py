import pygame
import sys
from utils import load_scores, delete_score_data

def score_board(SCREEN):
    """
    Affiche le tableau des scores.

    Args:
        SCREEN (Surface): La surface Pygame sur laquelle afficher le tableau des scores.

    Returns:
        str: "continue" si le joueur choisit de ne pas revenir au menu principal, sinon retourne le résultat de main_menu().
    """
    # Remplissage de l'écran avec une couleur noire
    SCREEN.fill((0, 0, 0))

    # Chargement des scores
    scores = load_scores()

    # Affichage du titre "Scores"
    score_font = pygame.font.SysFont(None, 56)
    title_text = score_font.render("Scores", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 400))
    SCREEN.blit(title_text, title_rect)

    # Affichage de la barre de séparation
    barre_text = score_font.render("_________________", True, (255, 255, 255))
    barre_rect = barre_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 380))
    SCREEN.blit(barre_text, barre_rect)

    # Affichage des scores
    board_font = pygame.font.SysFont(None, 48)
    y_offset = -300  # Décalage vertical initial pour afficher les scores
    for i, score in enumerate(scores):
        score_text = board_font.render(f"{i + 1}. Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + y_offset))
        SCREEN.blit(score_text, score_rect)
        y_offset += 50  # Augmenter le décalage pour afficher le score suivant

    # Chargement de l'image de la poubelle pour supprimer les scores
    trash_image = pygame.transform.scale(pygame.image.load("images/trash.png"), (92, 106))
    trash_image_rect = trash_image.get_rect(center=(SCREEN.get_width() // 2 + 380, SCREEN.get_height() // 2 - 400))
    # Affichage de l'image de la poubelle
    SCREEN.blit(trash_image, trash_image_rect)

    # Chargement de l'image de la croix pour fermer la fenêtre
    close_image = pygame.transform.scale(pygame.image.load("images/close.png"), (106, 106))
    close_image_rect = close_image.get_rect(topleft=(20, 20))  # Position de la croix en haut à gauche
    # Affichage de l'image de la croix
    SCREEN.blit(close_image, close_image_rect)

    pygame.display.update()

    # Attente de l'entrée du joueur pour supprimer les scores ou revenir au menu principal
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Si le joueur ferme la fenêtre, quitte le jeu
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if trash_image_rect.collidepoint(event.pos):
                    # Si le joueur clique sur l'image de la poubelle, supprime les scores et actualise l'affichage
                    delete_score_data()
                    scores = load_scores()
                elif close_image_rect.collidepoint(event.pos):
                    # Si le joueur clique sur l'image de la croix, retourne au menu principal
                    waiting = False
                    from menu import main_menu
                    return main_menu()

    # Après la boucle, si aucun événement n'a conduit à un retour au menu, retourne "continue"
    return "continue"
