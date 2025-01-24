import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Gerencia comportamentos do jogo."""
    def __init__(self):
        """Inicia o game e recursos."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Iniciando o Loop principal."""
        while True:

            self._check_events()
            self.ship.update()
            self._update_screen()
            # Observa eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redesenha a tela
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # Deixa tela com desenho.
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()
        
if __name__ == '__main__':
    #Cria uma instancia do game e abre o jogo.
    ai = AlienInvasion()
    ai.run_game()