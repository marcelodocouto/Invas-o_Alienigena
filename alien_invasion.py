import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Iniciliza o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Invasão Alienigena")
        self.ship = Ship(self)
        # defini a cor do backgraund.
        self.bg_color = (self.settings.bg_color)
        
    def run_game(self):
        """Inicia loop principal do jogo"""

        while True:
            # Observar evento do teclado e mouse

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redesenha a tela durante cada passagem pelo loop
            self.screen.fill(self.bg_color)
            self.ship.blitme()    
            # Deixa a tela desenhada mais recente visivel
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    """Cria uma instacia do jogo e executa o jogo"""
    ai = AlienInvasion()
    ai.run_game()
            