import pygame
import sys
from utils import load_scores


def main_menu():
    pygame.init()

    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((900, 950))
    pygame.display.set_caption("Robot Run")

    # Chargement des scores
    scores = load_scores()

    play_game_sound = pygame.mixer.Sound("sfx/sound/play.wav")

    menu_font = pygame.font.SysFont(None, 48)
    title_text = menu_font.render("Robot Run", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 50))
    SCREEN.blit(title_text, title_rect)

    play_text = menu_font.render("Jouer", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
    SCREEN.blit(play_text, play_rect)

    # Chargement de l'image de la poubelle
    scoreboard_image = pygame.transform.scale(pygame.image.load("images/score_board.png"), (102, 116))
    scoreboard_image_rect = scoreboard_image.get_rect(center=(SCREEN.get_width() // 2 + 380, SCREEN.get_height() // 2 - 400))
    # Affichage de l'image de la poubelle
    SCREEN.blit(scoreboard_image, scoreboard_image_rect)  # Remplacez x_position et y_position par les coordonnées où vous souhaitez afficher l'image

    quitter_text = menu_font.render("Quitter", True, (255, 255, 255))
    quitter_rect = quitter_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() //2 + 150))
    SCREEN.blit(quitter_text, quitter_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    waiting = False
                    play_game_sound.play()
                    from game import run_game
                    run_game()
                elif scoreboard_image_rect.collidepoint(event.pos):
                    from scoreboard import score_board
                    score_board(SCREEN)
                elif quitter_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
