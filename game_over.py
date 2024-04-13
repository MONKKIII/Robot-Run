import pygame
import sys
from utils import save_score

def game_over_SCREEN(SCREEN, score):
    """
    Affiche l'écran de fin de partie.

    Args:
        SCREEN (Surface): La surface Pygame sur laquelle afficher l'écran de fin de partie.
        score (int): Le score obtenu par le joueur.

    Returns:
        str: "game" si le joueur choisit de rejouer, "menu" s'il choisit de retourner au menu principal.
    """
    # Remplissage de l'écran avec une couleur noire
    SCREEN.fill((0, 0, 0))

    # Chargement des sons
    play_game_sound = pygame.mixer.Sound("sfx/sound/play.wav")

    # Texte "Game Over"
    game_over_font = pygame.font.SysFont(None, 72)
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 50))
    SCREEN.blit(game_over_text, game_over_rect)

    # Texte du score
    score_font = pygame.font.SysFont(None, 36)
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
    SCREEN.blit(score_text, score_rect)

    # Texte "Rejouer"
    play_again_font = pygame.font.SysFont(None, 36)
    play_again_text = play_again_font.render("Rejouer", True, (255, 255, 255))
    play_again_rect = play_again_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 100))
    SCREEN.blit(play_again_text, play_again_rect)

    # Texte "Retourner au Menu"
    return_to_menu_text = play_again_font.render("Retourner au Menu", True, (255, 255, 255))
    return_to_menu_rect = return_to_menu_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 150))
    SCREEN.blit(return_to_menu_text, return_to_menu_rect)

    # Texte "Sauvegarder le score"
    save_score_text = play_again_font.render("Sauvegarder le score", True, (255, 255, 255))
    save_score_rect = save_score_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 200))
    SCREEN.blit(save_score_text, save_score_rect)

    pygame.display.update()

    score_saved = False  # Variable pour suivre l'état de sauvegarde du score

    # Attente de l'entrée du joueur pour rejouer ou quitter
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Si le joueur ferme la fenêtre, quitte le jeu
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    # Si le joueur clique sur "Rejouer", retourne "game" pour relancer le jeu
                    waiting = False
                    play_game_sound.play()
                    return "game"
                elif return_to_menu_rect.collidepoint(event.pos):
                    # Si le joueur clique sur "Retourner au Menu", retourne "menu" pour revenir au menu principal
                    waiting = False
                    return "menu"
                elif save_score_rect.collidepoint(event.pos):
                    # Si le joueur clique sur "Sauvegarder le score"
                    if not score_saved:
                        # Si le score n'a pas encore été sauvegardé, le sauvegarde
                        save_score(score)
                        score_saved = True
                        print("Le score a bien été sauvegardé.")
                    else:
                        # Sinon, indique à l'utilisateur que le score a déjà été sauvegardé
                        print("Le score a déjà été sauvegardé.")
