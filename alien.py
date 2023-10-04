import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """Classe para representa um unico alienigena na frota"""

    def __init__(self,ai_game):
        self.settings = Settings()
        """Inicilizza o alienigena e define sua posição atual"""
        super().__init__()
        self.screen = ai_game.screen

        # Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load("img/alien.ship.png")
        self.rect = self.image.get_rect()

        # Iniciar cada alienigena novo 
        self.rect.x = self.rect.height
        self.rect.y = self.rect.height 

        # Armazena a posição horizontal ezata do alienigena
        self.x = float(self.rect.x)