import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Una classe per gestire i proiettili sparati dalla nave'''
    
    def __init__(self, ai_game):
        '''Crea un oggetto proiettile nella posizione corrente della nave'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # crea un rect del proiettile a (0, 0)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        
        # imposta la pos. corretta
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # memorizza la posizione del proiettile come float
        self.y = float(self.rect.y)
        
    def update(self):
        '''Fa salire il proiettile nella schermata'''
        # aggiorna la posizione esatta del proiettile
        self.y -= self.settings.bullet_speed
        
        #aggiorna il rect del proiettile
        self.rect.y = self.y
        
    def draw_bullet(self):
        '''Disegna il proiettile sulla schermata'''
        pygame.draw.rect(self.screen, self.color, self.rect)