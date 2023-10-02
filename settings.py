class Settings:
    """Inicializa as configuracoes do jogo"""

    def __init__(self):
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0, 0, 50)

        # Configurções da espaçonave
        self.ship_speed = 5

        # Configurações do prejetil
        self.bullet_speed = 2.0
        self.bullet_width = 5
        self.bullet_heigth = 15
        self.bullet_color = (60,60,60)
    