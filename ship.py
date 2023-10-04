import pygame


class Ship:
    """Classe para cuida da espaconave"""

    def __init__(self,ai_game):
        """Inicializa a espacoanave e define a sua posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Sobe a imagem da espaconave e obtém seu rect
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro do canto esquerdo
        self.rect.midbottom= self.screen_rect.midbottom

        # Armazena um float para posição exata da espaçonave
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # flag de movimento ; começa com a espaçonave que não esta se movendo
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -=self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -=self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y +=self.settings.ship_speed

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image,self.rect)