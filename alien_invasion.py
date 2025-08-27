import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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
        
        # memorizza gruppo di proiettili sparati 
        self.bullets = pygame.sprite.Group()
        
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        
    def run_game(self):
        '''Avvia il ciclo principale del gioco'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            
            # elimina proiettili che escono dalla schermata
            for item in self.bullets.copy():
                if item.rect.bottom <= 0:
                    self.bullets.remove(item)
            #print(len(self.bullets))
            
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        '''Risponde a eventi della tastyiera e del mouse'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        '''Pisponde alla pressione dei tasti'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True # attiva metodo per spostare nave a destra
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        '''Crea un nuovo proiettile e lo aggiunge al gruppo'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self) #creiamo istanza di bullet
            self.bullets.add(new_bullet)
                
    
    def _update_screen(self):
        '''Aggiorna le immagini sulla schermata e passa a quella nuova'''
        # ridisegna la schermata a ogni iterazione del ciclo
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        
        # rende visibile la schermata disegnata più recentemente
        pygame.display.flip()


# CREAZIONE ISTANZA DEL GIOCO 
if __name__ == '__main__':
    # crea un'istanza del gioco e lo esegue
    ai = AlienInvasion()
    ai.run_game()
        