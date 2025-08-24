import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Classe generale per gestire risorse e comportamenti del gioco'''
    
    def __init__(self):
        '''Inizializza il gioco e crea le risorse necessarie'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                              self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        '''Avvia il ciclo principale del gioco'''
        while True:
            # attendi eventi del mouse e della tastiera
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # ridisegna la schermata a ogni iterazione del ciclo
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # rende visibile la schermata disegnata più recentemente
            pygame.display.flip()
            self.clock.tick(60)
            
            
if __name__ == '__main__':
    # crea un'istanza del gioco e lo esegue
    ai = AlienInvasion()
    ai.run_game()
        