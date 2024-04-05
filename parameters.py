import pygame
import sys

# Charger la musique de fond
pygame.mixer.music.load("sfx/music/game_music.wav")
pygame.mixer.music.play(-1)  # Jouer la musique en boucle
pygame.mixer.music.set_volume(0.2)

# Fonction pour dessiner un curseur
def draw_slider(screen, x, y, width, height, value):
    # Dessiner la barre du curseur
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 2)
    # Dessiner le curseur
    cursor_pos = (x + int(value * width), y + height // 2)
    pygame.draw.circle(screen, (255, 0, 0), cursor_pos, 10)

# Fonction pour mettre à jour la valeur du curseur en fonction de la position de la souris
def update_slider_value(mouse_pos, slider_rect):
    slider_width = slider_rect.width
    relative_pos = mouse_pos[0] - slider_rect.left
    value = max(0, min(1, relative_pos / slider_width))
    return value

def parameters_screen(screen):
    running = True
    slider_value_music = 0.2  # Valeur initiale du curseur "Musique"
    volume = 0.2  # Volume initial de la musique
    slider_value_sound_effects = 0.3  # Valeur initiale du curseur "Effets sonores"

    dragging_slider = None  # Variable pour suivre quel curseur est en train d'être déplacé

    while running:
        screen.fill((0, 0, 0))  # Remplir l'écran en noir

        parameter_label = pygame.font.SysFont(None, 48).render("Parametre", True, (255, 255, 255))
        parameter_rect = parameter_label.get_rect(center=(screen.get_width() // 2, 50))  # Centrer le texte horizontalement
        screen.blit(parameter_label, parameter_rect)

        # Afficher les curseurs et les libellés
        slider_rect_music = pygame.Rect(250, 150, 250, 30)  # Curseur "Musique"
        draw_slider(screen, 250, 150, 250, 30, slider_value_music)
        music_label = pygame.font.SysFont(None, 36).render("Musique", True, (255, 255, 255))
        screen.blit(music_label, (50, 150))

        slider_rect_sound_effects = pygame.Rect(250, 250, 250, 30)  # Curseur "Effets sonores"
        draw_slider(screen, 250, 250, 250, 30, slider_value_sound_effects)
        sound_effects_label = pygame.font.SysFont(None, 36).render("Effets sonores", True, (255, 255, 255))
        screen.blit(sound_effects_label, (50, 250))

        # Afficher les pourcentages des curseurs à droite
        font = pygame.font.SysFont(None, 36)
        music_text = font.render("{:.0%}".format(slider_value_music), True, (255, 255, 255))
        screen.blit(music_text, (550, 150))
        sound_effects_text = font.render("{:.0%}".format(slider_value_sound_effects), True, (255, 255, 255))
        screen.blit(sound_effects_text, (550, 250))

        close_parameters_image = pygame.transform.scale(pygame.image.load("images/close.png"), (62, 62))
        close_parameters_rect = close_parameters_image.get_rect()
        screen.blit(close_parameters_image, (820, 10))

        # Mettre à jour le volume de la musique en fonction de la valeur du curseur
        pygame.mixer.music.set_volume(slider_value_music)

        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if slider_rect_music.collidepoint(mouse_pos):
                dragging_slider = "music"  # Définir le curseur à déplacer sur "Musique"
            elif slider_rect_sound_effects.collidepoint(mouse_pos):
                dragging_slider = "sound_effects"  # Définir le curseur à déplacer sur "Effets sonores"
            elif close_parameters_rect.collidepoint(event.pos):  # Vérifier si l'image de fermeture est cliquée
                return "menu"  # Retourner "menu" pour indiquer que vous souhaitez revenir au menu principal
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_slider = None  # Arrêter de déplacer le curseur lorsque le bouton de la souris est relâché
        elif event.type == pygame.MOUSEMOTION and dragging_slider is not None:
            mouse_pos = pygame.mouse.get_pos()
            if dragging_slider == "music":
                slider_value_music = update_slider_value(mouse_pos, slider_rect_music)
            elif dragging_slider == "sound_effects":
                slider_value_sound_effects = update_slider_value(mouse_pos, slider_rect_sound_effects)

# Exemple d'utilisation dans votre programme principal :
# parameters_screen(SCREEN)
