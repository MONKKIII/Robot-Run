import pygame
import sys
import random
import pickle
from player import Player  # Importer la classe Player depuis le module player
from enemy import Enemy  # Importer la classe Enemy depuis le module enemy
from menu import main_menu  # Importer la fonction main_menu depuis le module menu
from game_over import game_over_SCREEN  # Importer la fonction game_over_SCREEN depuis le module game_over
from scoreboard import score_board  # Importer la fonction score_board depuis le module scoreboard

pygame.init()

CLOCK = pygame.time.Clock()
FPS = 60

SCREEN = pygame.display.set_mode((900, 950))  # Définir la taille de l'écran du jeu
pygame.display.set_caption("Robot Run")  # Définir le titre de la fenêtre du jeu

game_over_sound = pygame.mixer.Sound("sfx/sound/game_over.wav")  # Charger le son de game over

# Charger la musique de fond
pygame.mixer.music.load("sfx/music/game_music.wav")
pygame.mixer.music.play(-1)  # Jouer la musique en boucle
pygame.mixer.music.set_volume(0.2)

BACKGROUND = pygame.image.load("images/background.jpeg")  # Charger l'image de fond du jeu

player = Player()  # Créer une instance de la classe Player
enemies = []  # Liste pour stocker les ennemis qui apparaissent dans le jeu

score = 0  # Initialiser le score du joueur
time_elapsed = 0  # Initialiser le temps écoulé

SCORE_FILE = "score.dat"  # Nom du fichier pour enregistrer le score

font = pygame.font.SysFont(None, 36)  # Charger la police pour afficher le score

def reset_game():
    """
    Réinitialise les variables du jeu pour recommencer une nouvelle partie.
    """
    global score, time_elapsed, enemies
    score = 0
    time_elapsed = 0
    enemies = []
    player.reset()  # Appeler la méthode reset de l'objet player pour le remettre à sa position initiale

def run_game():
    """
    Fonction principale pour exécuter le jeu.
    """
    global score, time_elapsed, player, enemies

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()

        SCREEN.blit(BACKGROUND, (0, 0))  # Afficher l'image de fond à la position (0, 0) de l'écran

        if keys_pressed[pygame.K_SPACE]:
            player.jump()

        if keys_pressed[pygame.K_LEFT]:
            player.move_left()

        if keys_pressed[pygame.K_RIGHT]:
            player.move_right()

        player.update()  # Mettre à jour la position du joueur
        player.draw(SCREEN)  # Dessiner le joueur sur l'écran

        if random.randint(0, 100) < 1:
            enemies.append(Enemy(780, 842))  # Ajouter un nouvel ennemi à la liste

        for enemy in enemies:
            enemy.update()  # Mettre à jour la position de chaque ennemi
            enemy.draw(SCREEN)  # Dessiner chaque ennemi sur l'écran

        enemies = [enemy for enemy in enemies if enemy.rect.right > 0]  # Supprimer les ennemis qui sortent de l'écran

        if player.rect.collidelist([enemy.rect for enemy in enemies]) != -1:
            game_over_sound.play()  # Jouer le son de game over
            game_over_action = game_over_SCREEN(SCREEN, score)  # Afficher l'écran de game over et récupérer l'action du joueur
            if game_over_action == "game":
                reset_game()  # Réinitialiser le jeu si le joueur choisit de rejouer
            elif game_over_action == "menu":
                reset_game()  # Réinitialiser le jeu si le joueur choisit de retourner au menu principal
                main_menu()  # Afficher le menu principal
            continue  # Passer à l'itération suivante de la boucle pour éviter d'afficher le score après game over

        time_elapsed += CLOCK.get_rawtime() / 100  # Mettre à jour le temps écoulé

        if time_elapsed >= 1:
            score += 10  # Augmenter le score toutes les secondes
            time_elapsed = 0

        score_text = font.render("Score: " + str(score), True, (255, 255, 255))  # Créer un texte pour afficher le score
        SCREEN.blit(score_text, (10, 10))  # Afficher le texte du score en haut à gauche de l'écran

        pygame.display.update()  # Mettre à jour l'écran
        CLOCK.tick(FPS)  # Limiter le jeu à un certain nombre de FPS

if __name__ == "__main__":
    main_menu()  # Appeler la fonction main_menu pour commencer le jeu
