import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe apara gerencio os projeteis disparados da espaçonave"""

    def __init__(self,ai_game):
        """Cria um objeto bullet na posição atual da espaçponave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria um bullet rerct em (0,0) e, em seguida define a pisição correta
        self.rect = pygame.Rect(0,0, self.settings.bullet_heigth,
                                self.settings.bullet_width)
        self.rect.midright = ai_game.ship.rect.midright

        # Armazena a posiçãodo projetil como um float
        self.x = float(self.rect.x)

    def update(self):
            """Desloca o projetio verticalmente pela tela"""
            # Atualiza a posição exat do projetil
            self.x += self.settings.bullet_speed
            # Atualiza a posição do rect
            self.rect.x = self.x

    def draw_bullet(self):
            """Desenha o projetil na tela"""
            pygame.draw.rect(self.screen,self.color,self.rect)