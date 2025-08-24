import sys
import pygame

class AlienInvasion:
    '''Classe generale per gestire risorse e comportamenti del gioco'''
    
    def __init__(self):
        '''Inizializza il gioco e crea le risorse necessarie'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        '''Avvia il ciclo principale del gioco'''
        while True:
            # attendi eventi del mouse e della tastiera
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # rende visibile la schermata disegnata più recentemente
            pygame.display.flip()
            
            
if __name__ == '__main__':
    # crea un'istanza del gioco e lo esegue
    ai = AlienInvasion()
    ai.run_game()
        