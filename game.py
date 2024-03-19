import pygame
import sys
import random
from player import Player
from enemy import Enemy
from menu import main_menu
from game_over import game_over_screen

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((900, 950))
pygame.display.set_caption("Robot Run")

game_over_sound = pygame.mixer.Sound("sfx/sound/game_over.wav")

BACKGROUND = pygame.image.load("images/background.jpeg")

player = Player()
enemies = []

score = 0
time_elapsed = 0

font = pygame.font.SysFont(None, 36)

def reset_game():
    global score, time_elapsed, enemies
    score = 0
    time_elapsed = 0
    enemies = []
    player.reset()

def run_game():
    global score, time_elapsed, player, enemies

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()

        SCREEN.blit(BACKGROUND, (0, 0))

        if keys_pressed[pygame.K_SPACE]:
            player.jump()

        if keys_pressed[pygame.K_LEFT]:
            player.move_left()

        if keys_pressed[pygame.K_RIGHT]:
            player.move_right()

        player.update()
        player.draw(SCREEN)

        if random.randint(0, 100) < 1:
            enemies.append(Enemy(780, 842))

        for enemy in enemies:
            enemy.update()
            enemy.draw(SCREEN)

        enemies = [enemy for enemy in enemies if enemy.rect.right > 0]

        if player.rect.collidelist([enemy.rect for enemy in enemies]) != -1:
            game_over_sound.play()
            game_over_action = game_over_screen(SCREEN, score)
            if game_over_action == "game":
                reset_game()
            elif game_over_action == "menu":
                reset_game()
                main_menu()
            continue  # Continuez directement à la prochaine itération de la boucle pour éviter d'afficher le score après game over

        time_elapsed += CLOCK.get_rawtime() / 100

        if time_elapsed >= 1:
            score += 10
            time_elapsed = 0

        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        SCREEN.blit(score_text, (10, 10))

        pygame.display.update()
        CLOCK.tick(60)

if __name__ == "__main__":
    main_menu()
