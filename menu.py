import pygame
import sys

def main_menu():
    pygame.init()

    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((900, 950))
    pygame.display.set_caption("Robot Run")

    play_game_sound = pygame.mixer.Sound("sfx/sound/play.wav")

    menu_font = pygame.font.SysFont(None, 48)
    title_text = menu_font.render("Robot Run", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 50))
    SCREEN.blit(title_text, title_rect)

    play_text = menu_font.render("Jouer", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
    SCREEN.blit(play_text, play_rect)

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
