import pygame
import sys

def game_over_screen(screen, score):
    # Display game over screen
    screen.fill((0, 0, 0))  # Fill the screen with black color

    # Game over text
    game_over_font = pygame.font.SysFont(None, 72)
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    screen.blit(game_over_text, game_over_rect)

    # Score text
    score_font = pygame.font.SysFont(None, 36)  # Define font for the score
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    screen.blit(score_text, score_rect)

    # Play again text
    play_again_font = pygame.font.SysFont(None, 36)
    play_again_text = play_again_font.render("Play Again", True, (255, 255, 255))
    play_again_rect = play_again_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
    screen.blit(play_again_text, play_again_rect)

    # Return to menu text
    return_to_menu_text = play_again_font.render("Return to Menu", True, (255, 255, 255))
    return_to_menu_rect = return_to_menu_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))
    screen.blit(return_to_menu_text, return_to_menu_rect)

    pygame.display.update()

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
                    return "game" # Retourne "game" pour relancer le jeu
                elif return_to_menu_rect.collidepoint(event.pos):
                    waiting = False  # Exit the loop to return to the menu
                    return "menu"  # Renvoyer "menu" pour indiquer à main.py de passer au menu principal

