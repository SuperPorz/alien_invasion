import sys
import pygame

class AlienInvasion:
    '''Classe generale per gestire risorse e comportamenti del gioco'''
    
    def __init__(self):
        '''Inizializza il gioco e crea le risorse necessarie'''
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        # Imposta il colore di sfondo
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        '''Avvia il ciclo principale del gioco'''
        while True:
            # attendi eventi del mouse e della tastiera
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # ridisegna la schermata a ogni iterazione del ciclo
            self.screen.fill(self.bg_color)
            
            # rende visibile la schermata disegnata più recentemente
            pygame.display.flip()
            self.clock.tick(60)
            
            
if __name__ == '__main__':
    # crea un'istanza del gioco e lo esegue
    ai = AlienInvasion()
    ai.run_game()
        