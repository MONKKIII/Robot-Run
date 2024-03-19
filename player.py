import pygame
pygame.init()

class Player:
    def __init__(self):
        self.x_position = 250
        self.y_position = 842
        self.jumping = False
        self.y_gravity = 1
        self.jump_height = 20
        self.y_velocity = self.jump_height

        self.standing_surface = pygame.transform.scale(pygame.image.load("images/player/standing.png"), (72, 96))
        self.jumping_surface = pygame.transform.scale(pygame.image.load("images/player/jumping.png"), (72, 96))

        self.rect = self.standing_surface.get_rect(center=(self.x_position, self.y_position))

        self.jump_sound = pygame.mixer.Sound("sfx/sound/jump.wav")
        self.jump_sound.set_volume(0.1)

        # Variable pour garder une trace de l'état du saut
        self.sound_playing = False

    def move_left(self):
        self.x_position -= 5  # Adjust the value for speed
        self.x_position = max(0, self.x_position)

    def move_right(self):
        self.x_position += 5  # Adjust the value for speed
        self.x_position = min(self.x_position, 900 - self.standing_surface.get_width())

    def jump(self):
        if not self.sound_playing:  # Vérifier si le son est déjà en train d'être joué
            self.jumping = True
            self.jump_sound.play()
            self.sound_playing = True

    def update(self):
        if self.jumping:
            self.y_position -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.y_velocity = self.jump_height
            self.rect = self.jumping_surface.get_rect(center=(self.x_position, self.y_position))
        else:
            self.rect = self.standing_surface.get_rect(center=(self.x_position, self.y_position))
        # Mettre à jour l'état du saut
        if not self.jumping and self.sound_playing:
            self.sound_playing = False

    def draw(self, screen):
        if self.jumping:
            screen.blit(self.jumping_surface, self.rect)
        else:
            screen.blit(self.standing_surface, self.rect)

    def reset(self):
        # Reset player position
        self.rect.center = (250, 842)  # Initial position
