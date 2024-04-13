import pygame
pygame.init()

class Player:
    def __init__(self):
        # Position initiale du joueur
        self.x_position = 250
        self.y_position = 842

        # État du saut
        self.jumping = False

        # Variables de saut
        self.y_gravity = 1
        self.jump_height = 20
        self.y_velocity = self.jump_height

        # Chargement des images du joueur
        self.standing_surface = pygame.transform.scale(pygame.image.load("images/player/standing.png"), (72, 96))
        self.jumping_surface = pygame.transform.scale(pygame.image.load("images/player/jumping.png"), (72, 96))

        # Rectangle de collision du joueur
        self.rect = self.standing_surface.get_rect(center=(self.x_position, self.y_position))

        # Son de saut
        self.jump_sound = pygame.mixer.Sound("sfx/sound/jump.wav")
        self.jump_sound.set_volume(0.1)

        # Variable pour suivre l'état du son de saut
        self.sound_playing = False

    def move_left(self):
        # Déplacement vers la gauche
        self.x_position -= 5  # Ajuster la valeur pour la vitesse
        self.x_position = max(0, self.x_position)

    def move_right(self):
        # Déplacement vers la droite
        self.x_position += 5  # Ajuster la valeur pour la vitesse
        self.x_position = min(self.x_position, 900 - self.standing_surface.get_width())

    def jump(self):
        # Fonction pour effectuer un saut
        if not self.sound_playing:  # Vérifier si le son est déjà en train d'être joué
            self.jumping = True
            self.jump_sound.play()
            self.sound_playing = True

    def update(self):
        # Mettre à jour la position du joueur en fonction de l'état du saut
        if self.jumping:
            self.y_position -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.y_velocity = self.jump_height
            self.rect = self.jumping_surface.get_rect(center=(self.x_position, self.y_position))
        else:
            self.rect = self.standing_surface.get_rect(center=(self.x_position, self.y_position))
        
        # Mettre à jour l'état du son de saut
        if not self.jumping and self.sound_playing:
            self.sound_playing = False

    def draw(self, SCREEN):
        # Dessiner le joueur sur l'écran
        if self.jumping:
            SCREEN.blit(self.jumping_surface, self.rect)
        else:
            SCREEN.blit(self.standing_surface, self.rect)

    def reset(self):
        # Réinitialiser la position du joueur
        self.rect.center = (250, 842)  # Position initiale
