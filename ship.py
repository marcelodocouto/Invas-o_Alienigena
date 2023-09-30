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

        # Começa cada espaçonave nova no centro do canto esquerdo
        self.rect.centery= self.screen_rect.centery

        # flag de movimento ; começa com a espaçonave que não esta se movendo
        self.moving_right = False
        self.moving_Left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        if self.moving_right:
            self.rect.x +=1
        elif self.moving_Left:
            self.rect.x -=1
        elif self.moving_up:
            self.rect.y -=1
        elif self.moving_down:
            self.rect.y +=1

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image,self.rect)