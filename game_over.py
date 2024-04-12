import pygame
import sys
from utils import save_score

def game_over_SCREEN(SCREEN, score):
    # Display game over SCREEN
    SCREEN.fill((0, 0, 0))  # Fill the SCREEN with black color

    play_game_sound = pygame.mixer.Sound("sfx/sound/play.wav")

    # Game over text
    game_over_font = pygame.font.SysFont(None, 72)
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 50))
    SCREEN.blit(game_over_text, game_over_rect)

    # Score text
    score_font = pygame.font.SysFont(None, 36)  # Define font for the score
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
    SCREEN.blit(score_text, score_rect)

    # Play again text
    play_again_font = pygame.font.SysFont(None, 36)
    play_again_text = play_again_font.render("Rejouer", True, (255, 255, 255))
    play_again_rect = play_again_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 100))
    SCREEN.blit(play_again_text, play_again_rect)

    # Return to menu text
    return_to_menu_text = play_again_font.render("Retourner au Menu", True, (255, 255, 255))
    return_to_menu_rect = return_to_menu_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 150))
    SCREEN.blit(return_to_menu_text, return_to_menu_rect)

    # Return to menu text
    save_score_text = play_again_font.render("Sauvegarder le score", True, (255, 255, 255))
    save_score_rect = save_score_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 200))
    SCREEN.blit(save_score_text, save_score_rect)

    pygame.display.update()

    score_saved = False  # Variable pour suivre l'état de sauvegarde du score

    # Wait for player input to play again or quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    waiting = False  # Exit the loop to restart the game
                    play_game_sound.play()
                    return "game" # Retourne "game" pour relancer le jeu
                elif return_to_menu_rect.collidepoint(event.pos):
                    waiting = False  # Exit the loop to return to the menu
                    return "menu"  # Renvoyer "menu" pour indiquer à main.py de passer au menu principal
                elif save_score_rect.collidepoint(event.pos):
                    if not score_saved:
                        save_score(score)
                        score_saved = True
                        print("Le score a bien été sauvegardé.")
                    else:
                        # Indiquer à l'utilisateur que le score a déjà été sauvegardé
                        print("Le score a déjà été sauvegardé.")

