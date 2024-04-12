import pygame
import sys
from utils import load_scores, delete_score_data

def score_board(SCREEN):
    # Display score board SCREEN
    SCREEN.fill((0, 0, 0))  # Fill the SCREEN with black color

    # Chargement des scores
    scores = load_scores()

    # Affichage des scores
    score_font = pygame.font.SysFont(None, 56)
    title_text = score_font.render("Scores", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 400))
    SCREEN.blit(title_text, title_rect)

    barre_text = score_font.render("_________________", True, (255, 255, 255))
    barre_rect = barre_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 380))
    SCREEN.blit(barre_text, barre_rect)

    board_font = pygame.font.SysFont(None, 48)
    y_offset = -300  # Décalage vertical initial pour afficher les scores
    for i, score in enumerate(scores):
        score_text = board_font.render(f"{i + 1}. Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + y_offset))
        SCREEN.blit(score_text, score_rect)
        y_offset += 50  # Augmenter le décalage pour afficher le score suivant

    # Chargement de l'image de la poubelle
    trash_image = pygame.transform.scale(pygame.image.load("images/trash.png"), (92, 106))
    trash_image_rect = trash_image.get_rect(center=(SCREEN.get_width() // 2 + 380, SCREEN.get_height() // 2 - 400))
    # Affichage de l'image de la poubelle
    SCREEN.blit(trash_image, trash_image_rect)  # Remplacez x_position et y_position par les coordonnées où vous souhaitez afficher l'image

    # Chargement de l'image de la croix
    close_image = pygame.transform.scale(pygame.image.load("images/close.png"), (106, 106))
    close_image_rect = close_image.get_rect(topleft=(20, 20))  # Position de la croix en haut à gauche
    # Affichage de l'image de la croix
    SCREEN.blit(close_image, close_image_rect)

    pygame.display.update()

    # Wait for player input to play again or quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if trash_image_rect.collidepoint(event.pos):
                    delete_score_data()
                    # Efface les scores et actualise l'affichage
                    scores = load_scores()
                    # Réaffichage des scores...
                elif close_image_rect.collidepoint(event.pos):
                    waiting = False  # Exit the loop to return to the menu
                    # Retour au menu principal
                    from menu import main_menu
                    return main_menu()

    
    # Après la boucle, si aucun événement n'a conduit à un retour au menu, retournez "continue"
    return "continue"
                
