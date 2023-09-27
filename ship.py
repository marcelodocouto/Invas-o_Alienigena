import pygame

class Ship:
    """Classe para cuida da espaconave"""

    def __init__(self,ai_game):
        """Inicializa a espacoanave e define a sua posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Sobe a imagem da espaconave e obtém seu rect
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image,self.rect)