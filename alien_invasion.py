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
            self._check_evets()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_evets(self):
         # Responde as teclas precionadas e eventos do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move a espaçonave para direita
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    # Move a espaçonave para esquerda
                    self.ship.moving_Left = True

                elif event.key == pygame.K_UP:
                    # Move a espaçonave para esquerda
                    self.ship.moving_up = True

                elif event.key == pygame.K_DOWN:
                    # Move a espaçonave para esquerda
                    self.ship.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_Left = False
                
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
    
    def _update_screen(self):
        """Atualiza as imagens na tela e muda para nova tela"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        pygame.display.flip()  


if __name__ == '__main__':
    """Cria uma instacia do jogo e executa o jogo"""
    ai = AlienInvasion()
    ai.run_game()
            