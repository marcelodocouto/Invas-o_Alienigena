import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Iniciliza o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Invasão Alienigena")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._creat_fleet()
        # defini a cor do backgraund.
        self.bg_color = (self.settings.bg_color)
        
    def run_game(self):
        """Inicia loop principal do jogo"""
        while True:
            self._check_evets()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_evets(self):
         # Responde as teclas precionadas e eventos do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        # Responte as teclas pressionadas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        # Responde as teclas soltas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False    
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False    
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        """Cria um novo projetil e adiciona ao grupo de projeteis"""
        if len(self.bullets) < self.settings.bullet_allowed :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Atuliza a posição dos projeteis e descarta projeteis antigos"""
        # Atualiza as posições dos projeteis 
        self.bullets.update()

        # Descarta projeteis antigos
        for bullet in self.bullets.copy():
            if bullet.rect.top < 0 :
                self.bullets.remove(bullet)
    
    def _creat_fleet(self):
        """Cria a frota de alienigenas"""
        # Cria um aliengena e continua adicionando alienigenas
        # ate que não aja mais espaço
        # Odistanciamento entre alienigena e a distancia de um alienigena
        # O distanciamento entre os alenigenas é de uma largura
        # de alienigena e uma altura de alienigena
        alien = Alien(self)
        alien_widht,alien_heigth = alien.rect.size

        current_x, current_y = alien_widht, alien_heigth
        while current_y < (self.settings.screen_height - 3 *alien_heigth):
            while current_x < (self.settings.screen_width - 2 * alien_widht):
                self._creat_alien(current_x,current_y)
                current_x += 2 *alien_widht
            
            # Termina a fileira redefinindo o valor de x , e incremnta o valor y
            current_x = alien_widht
            current_y += 2 *alien_heigth

    def _creat_alien(self,x_position,y_position):
        """Cria um alienigena e posiciona na fileira"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """Atualiza as imagens na tela e muda para nova tela"""
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()  


if __name__ == '__main__':
    """Cria uma instacia do jogo e executa o jogo"""
    ai = AlienInvasion()
    ai.run_game()
