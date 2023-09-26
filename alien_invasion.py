import sys

import pygame

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Iniciliza o jogo e cria recursos do jogo"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Invasão Alienigena")
        
        def run_game(self):
            """Inicia loop principal do jogo"""

            while True:
                # Observar evento do teclado e mouse

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                
                # Deixa a tela desenhada mais recente visivel
                pygame.display.flip()
            